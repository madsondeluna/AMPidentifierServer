# amp_identifier/core.py

import os
import glob
import pandas as pd
from . import data_io, feature_extraction, prediction, reporting

# Define the location of internal models
MODEL_DIR = "model_training/saved_model"
SCALER_PATH = os.path.join(MODEL_DIR, "feature_scaler.pkl")

def print_progress_bar(step, total_steps, description=""):
    """Print a simple progress bar."""
    percentage = (step / total_steps) * 100
    bar_length = 40
    filled = int(bar_length * step / total_steps)
    bar = '█' * filled + '░' * (bar_length - filled)
    print(f"\r{description} [{bar}] {percentage:.1f}% ({step}/{total_steps})", end='', flush=True)
    if step == total_steps:
        print()  # New line when complete

def run_prediction_pipeline(input_file: str, output_dir: str, internal_model_type: str, use_ensemble: bool, external_model_paths: list):
    """Orchestrates the full prediction pipeline with model selection and ensemble options."""
    total_steps = 4
    current_step = 0
    
    print("=" * 80)
    print("AMP IDENTIFICATION PIPELINE")
    print("=" * 80)

    # Step 1: Load sequences
    current_step += 1
    print(f"\nStep {current_step}/{total_steps}: Loading sequences from {input_file}...")
    print_progress_bar(0, 1, "Loading")
    sequences, seq_ids = data_io.load_fasta_sequences(input_file)
    print_progress_bar(1, 1, "Loading")
    
    if not sequences:
        print("No sequences loaded. Exiting pipeline.")
        return
    print(f"✓ Found {len(sequences)} sequences.")

    # Step 2: Calculate features
    current_step += 1
    print(f"\nStep {current_step}/{total_steps}: Calculating physicochemical features...")
    print_progress_bar(0, len(sequences), "Processing sequences")
    
    features_df = feature_extraction.calculate_physicochemical_features(sequences, seq_ids)
    features_df.fillna(0, inplace=True)
    print_progress_bar(len(sequences), len(sequences), "Processing sequences")
    
    features_report_path = os.path.join(output_dir, "physicochemical_features.csv")
    reporting.save_features_report(features_df, features_report_path)
    print(f"✓ Features calculated and saved to {features_report_path}")

    # Step 3: Run predictions
    current_step += 1
    print(f"\nStep {current_step}/{total_steps}: Running predictions...")
    
    # Load the scaler for feature normalization
    print("  → Loading feature scaler...")
    scaler = prediction.load_scaler(SCALER_PATH)
    if scaler is None:
        print("  ⚠ Warning: Could not load scaler. Predictions may be inaccurate.")
    
    all_predictions = {}
    
    # --- Ensemble Voting Logic ---
    if use_ensemble:
        print("  → Mode: Ensemble Voting")
        internal_model_paths = glob.glob(os.path.join(MODEL_DIR, "amp_model_*.pkl"))
        if not internal_model_paths:
            print("  ⚠ Warning: No internal models found for ensemble mode.")
        
        total_models = len(internal_model_paths)
        for idx, model_path in enumerate(internal_model_paths, 1):
            model_name = os.path.splitext(os.path.basename(model_path))[0].replace('amp_model_', '')
            print_progress_bar(idx-1, total_models, f"  Models")
            internal_model = prediction.load_model(model_path)
            if internal_model:
                internal_results = prediction.predict_sequences(internal_model, features_df.copy(), scaler)
                all_predictions[f"internal_{model_name}"] = internal_results
        print_progress_bar(total_models, total_models, f"  Models")
        print(f"  ✓ {total_models} models processed (RF, SVM, GB)")
    
    # --- Single Internal Model Logic ---
    else:
        print(f"  → Mode: Single Model ({internal_model_type.upper()})")
        print_progress_bar(0, 1, f"  Loading model")
        model_path = os.path.join(MODEL_DIR, f"amp_model_{internal_model_type}.pkl")
        internal_model = prediction.load_model(model_path)
        if internal_model:
            internal_results = prediction.predict_sequences(internal_model, features_df.copy(), scaler)
            all_predictions[f"internal_{internal_model_type}"] = internal_results
        print_progress_bar(1, 1, f"  Loading model")
        print(f"  ✓ Model {internal_model_type.upper()} loaded and executed")

    # --- External Model Logic ---
    if external_model_paths:
        total_ext = len(external_model_paths)
        for idx, model_path in enumerate(external_model_paths, 1):
            model_name = os.path.splitext(os.path.basename(model_path))[0]
            print_progress_bar(idx-1, total_ext, f"  External models")
            external_model = prediction.load_model(model_path)
            if external_model:
                external_results = prediction.predict_sequences(external_model, features_df.copy(), None)
                all_predictions[f"external_{model_name}"] = external_results
        print_progress_bar(total_ext, total_ext, f"  External models")
        print(f"  ✓ {total_ext} external model(s) processed")
    
    # Step 4: Generate Report
    current_step += 1
    if not all_predictions:
        print("No models were successfully loaded. Cannot generate prediction report.")
        print("=" * 80)
        return
        
    print(f"\nStep {current_step}/{total_steps}: Generating final comparison report...")
    print_progress_bar(0, 1, "Saving report")
    comparison_report_path = os.path.join(output_dir, "prediction_comparison_report.csv")
    reporting.save_comparison_report(features_df, all_predictions, use_ensemble, comparison_report_path)
    print_progress_bar(1, 1, "Saving report")
    print(f"✓ Report saved to {comparison_report_path}")
    
    # Calculate statistics
    print("\n" + "=" * 80)
    print("PREDICTION SUMMARY")
    print("=" * 80)
    
    # Load the saved report to get statistics
    report_df = pd.read_csv(comparison_report_path)
    total_sequences = len(report_df)
    
    # Determine which column to use for AMP classification
    if use_ensemble and 'ensemble_prediction' in report_df.columns:
        amp_count = report_df['ensemble_prediction'].sum()
        prediction_method = "ensemble voting"
    elif f'pred_internal_{internal_model_type}' in report_df.columns:
        amp_count = report_df[f'pred_internal_{internal_model_type}'].sum()
        prediction_method = f"{internal_model_type.upper()} model"
    else:
        # Fallback to first prediction column
        pred_cols = [col for col in report_df.columns if col.startswith('pred_')]
        if pred_cols:
            amp_count = report_df[pred_cols[0]].sum()
            prediction_method = "available model"
        else:
            amp_count = 0
            prediction_method = "unknown"
    
    non_amp_count = total_sequences - amp_count
    amp_percentage = (amp_count / total_sequences * 100) if total_sequences > 0 else 0
    
    print(f"Based on {total_sequences} submitted sequence(s):")
    print(f"  • {amp_count} ({amp_percentage:.1f}%) classified as potential AMPs")
    print(f"  • {non_amp_count} ({100-amp_percentage:.1f}%) classified as non-AMPs")
    print(f"  • Prediction method: {prediction_method}")
    print(f"\nDetailed results available in:")
    print(f"  → {comparison_report_path}")
    print("=" * 80)
    
    # Citation message
    print("\n" + "="*80)
    print("If this tool supports your research, please cite:")
    print("Luna-Aragão, M. A., da Silva, R. L., Pacífico, J., Santos-Silva, C. A. & Benko-Iseppon, A. M. (2025). AMPidentifier: A Python toolkit for predicting antimicrobial peptides using ensemble machine learning.")
    print("GitHub repository: https://github.com/madsondeluna/AMPIdentifier")
    print("="*80)
    print()