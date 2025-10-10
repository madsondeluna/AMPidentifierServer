# amp_identifier/core.py

import os
import glob
import time
import pandas as pd
from . import data_io, feature_extraction, prediction, reporting

# Define the location of internal models
MODEL_DIR = "model_training/saved_model"
SCALER_PATH = os.path.join(MODEL_DIR, "feature_scaler.pkl")


class AnimatedProgressBar:
    """Animated progress bar with time estimation and elegant visual."""
    
    def __init__(self, total, description="Processing", bar_length=45):
        self.total = total
        self.current = 0
        self.description = description
        self.bar_length = bar_length
        self.start_time = time.time()
        self.animation_frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        self.frame_index = 0
        
    def update(self, step=1):
        """Update progress bar."""
        self.current += step
        self.frame_index = (self.frame_index + 1) % len(self.animation_frames)
        self._render()
    
    def _render(self):
        """Render the progress bar."""
        percentage = (self.current / self.total * 100) if self.total > 0 else 0
        filled = int(self.bar_length * self.current / self.total) if self.total > 0 else 0
        
        # Create gradient bar with different characters for visual appeal
        bar_chars = []
        for i in range(self.bar_length):
            if i < filled - 1:
                bar_chars.append('━')
            elif i == filled - 1 and self.current < self.total:
                bar_chars.append('╸')
            else:
                bar_chars.append('─')
        
        bar = ''.join(bar_chars)
        
        # Calculate time estimates
        elapsed_time = time.time() - self.start_time
        if self.current > 0 and self.current < self.total:
            avg_time_per_step = elapsed_time / self.current
            remaining_steps = self.total - self.current
            eta_seconds = avg_time_per_step * remaining_steps
            eta_str = self._format_time(eta_seconds)
            time_info = f"ETA: {eta_str}"
        elif self.current >= self.total:
            total_time = self._format_time(elapsed_time)
            time_info = f"Done in {total_time}"
        else:
            time_info = "Calculating..."
        
        # Animation spinner
        spinner = self.animation_frames[self.frame_index] if self.current < self.total else '✓'
        
        # Render with colors and formatting
        status = f"\r{spinner} {self.description}: [{bar}] {percentage:.1f}% ({self.current}/{self.total}) | {time_info}"
        print(status, end='', flush=True)
    
    def _format_time(self, seconds):
        """Format seconds into human-readable time."""
        if seconds < 1:
            return f"{seconds*1000:.0f}ms"
        elif seconds < 60:
            return f"{seconds:.1f}s"
        elif seconds < 3600:
            mins = int(seconds / 60)
            secs = int(seconds % 60)
            return f"{mins}m {secs}s"
        else:
            hours = int(seconds / 3600)
            mins = int((seconds % 3600) / 60)
            return f"{hours}h {mins}m"
    
    def set_description(self, description):
        """Update the description."""
        self.description = description
        self._render()
    
    def finish(self):
        """Complete the progress bar."""
        self.current = self.total
        self._render()
        print()  # Add newline when finished

def run_prediction_pipeline(input_file: str, output_dir: str, internal_model_type: str, use_ensemble: bool, external_model_paths: list):
    """Orchestrates the full prediction pipeline with model selection and ensemble options."""
    total_steps = 4
    current_step = 0
    
    print("=" * 80)
    print("AMP IDENTIFICATION PIPELINE")
    print("=" * 80)

    # Step 1: Load sequences
    current_step += 1
    print(f"\n╔{'═' * 78}╗")
    print(f"║ Step {current_step}/{total_steps}: Loading sequences from {os.path.basename(input_file):<47} ║")
    print(f"╚{'═' * 78}╝")
    
    progress = AnimatedProgressBar(1, "Loading FASTA", bar_length=50)
    sequences, seq_ids = data_io.load_fasta_sequences(input_file)
    progress.update()
    progress.finish()
    
    if not sequences:
        print("No sequences loaded. Exiting pipeline.")
        return
    print(f"✓ Found {len(sequences)} sequence(s) ready for analysis.\n")

    # Step 2: Calculate features
    current_step += 1
    print(f"╔{'═' * 78}╗")
    print(f"║ Step {current_step}/{total_steps}: Calculating physicochemical features{' ' * 30} ║")
    print(f"╚{'═' * 78}╝")
    
    progress = AnimatedProgressBar(len(sequences), "Extracting features", bar_length=50)
    features_df = feature_extraction.calculate_physicochemical_features(sequences, seq_ids)
    features_df.fillna(0, inplace=True)
    progress.current = len(sequences)
    progress.finish()
    
    features_report_path = os.path.join(output_dir, "physicochemical_features.csv")
    reporting.save_features_report(features_df, features_report_path)
    print(f"✓ Features saved to: {features_report_path}\n")

    # Step 3: Run predictions
    current_step += 1
    print(f"╔{'═' * 78}╗")
    print(f"║ Step {current_step}/{total_steps}: Running predictions{' ' * 44} ║")
    print(f"╚{'═' * 78}╝")
    
    # Load the scaler for feature normalization
    print("  → Loading feature scaler...")
    scaler = prediction.load_scaler(SCALER_PATH)
    if scaler is None:
        print("  ⚠ Warning: Could not load scaler. Predictions may be inaccurate.")
    
    all_predictions = {}
    
    # --- Ensemble Voting Logic ---
    if use_ensemble:
        print("  → Mode: Ensemble Voting (RF + SVM + GB)")
        internal_model_paths = glob.glob(os.path.join(MODEL_DIR, "amp_model_*.pkl"))
        if not internal_model_paths:
            print("  ⚠ Warning: No internal models found for ensemble mode.")
        
        total_models = len(internal_model_paths)
        progress = AnimatedProgressBar(total_models, "Loading models", bar_length=50)
        
        for idx, model_path in enumerate(internal_model_paths, 1):
            model_name = os.path.splitext(os.path.basename(model_path))[0].replace('amp_model_', '').upper()
            progress.set_description(f"Processing {model_name}")
            
            internal_model = prediction.load_model(model_path)
            if internal_model:
                internal_results = prediction.predict_sequences(internal_model, features_df.copy(), scaler)
                all_predictions[f"internal_{model_name.lower()}"] = internal_results
            
            progress.update()
        
        progress.finish()
        print(f"✓ {total_models} models processed successfully\n")
    
    # --- Single Internal Model Logic ---
    else:
        print(f"  → Mode: Single Model ({internal_model_type.upper()})")
        progress = AnimatedProgressBar(1, f"Loading {internal_model_type.upper()}", bar_length=50)
        
        model_path = os.path.join(MODEL_DIR, f"amp_model_{internal_model_type}.pkl")
        internal_model = prediction.load_model(model_path)
        if internal_model:
            internal_results = prediction.predict_sequences(internal_model, features_df.copy(), scaler)
            all_predictions[f"internal_{internal_model_type}"] = internal_results
        
        progress.update()
        progress.finish()
        print(f"✓ Model {internal_model_type.upper()} executed successfully\n")

    # --- External Model Logic ---
    if external_model_paths:
        total_ext = len(external_model_paths)
        progress = AnimatedProgressBar(total_ext, "External models", bar_length=50)
        
        for idx, model_path in enumerate(external_model_paths, 1):
            model_name = os.path.splitext(os.path.basename(model_path))[0]
            progress.set_description(f"Loading {model_name}")
            
            external_model = prediction.load_model(model_path)
            if external_model:
                external_results = prediction.predict_sequences(external_model, features_df.copy(), None)
                all_predictions[f"external_{model_name}"] = external_results
            
            progress.update()
        
        progress.finish()
        print(f"✓ {total_ext} external model(s) processed\n")
    
    # Step 4: Generate Report
    current_step += 1
    if not all_predictions:
        print("No models were successfully loaded. Cannot generate prediction report.")
        print("=" * 80)
        return
    
    print(f"╔{'═' * 78}╗")
    print(f"║ Step {current_step}/{total_steps}: Generating final comparison report{' ' * 33} ║")
    print(f"╚{'═' * 78}╝")
    
    progress = AnimatedProgressBar(1, "Saving results", bar_length=50)
    comparison_report_path = os.path.join(output_dir, "prediction_comparison_report.csv")
    reporting.save_comparison_report(features_df, all_predictions, use_ensemble, comparison_report_path)
    progress.update()
    progress.finish()
    print(f"✓ Report saved to: {comparison_report_path}\n")
    
    # Calculate statistics with elegant display
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 25 + "PREDICTION SUMMARY" + " " * 35 + "║")
    print("╠" + "═" * 78 + "╣")
    
    # Load the saved report to get statistics
    report_df = pd.read_csv(comparison_report_path)
    total_sequences = len(report_df)
    
    # Determine which column to use for AMP classification
    if use_ensemble and 'ensemble_prediction' in report_df.columns:
        amp_count = int(report_df['ensemble_prediction'].sum())
        prediction_method = "Ensemble Voting (RF + SVM + GB)"
    elif f'pred_internal_{internal_model_type}' in report_df.columns:
        amp_count = int(report_df[f'pred_internal_{internal_model_type}'].sum())
        prediction_method = f"{internal_model_type.upper()} Model"
    else:
        # Fallback to first prediction column
        pred_cols = [col for col in report_df.columns if col.startswith('pred_')]
        if pred_cols:
            amp_count = int(report_df[pred_cols[0]].sum())
            prediction_method = "Available Model"
        else:
            amp_count = 0
            prediction_method = "Unknown"
    
    non_amp_count = total_sequences - amp_count
    amp_percentage = (amp_count / total_sequences * 100) if total_sequences > 0 else 0
    non_amp_percentage = 100 - amp_percentage
    
    # Create visual bar chart
    amp_bar_len = int(amp_percentage / 2) if amp_percentage > 0 else 0
    non_amp_bar_len = 50 - amp_bar_len
    
    print(f"║ Total sequences analyzed: {total_sequences:<52} ║")
    print(f"║ Prediction method: {prediction_method:<59} ║")
    print("╠" + "─" * 78 + "╣")
    print(f"║ Potential AMPs detected:     {amp_count:>4} ({amp_percentage:>5.1f}%)  [{'█' * amp_bar_len}{'░' * non_amp_bar_len}]  ║")
    print(f"║ Potential Non-AMPs:          {non_amp_count:>4} ({non_amp_percentage:>5.1f}%)  [{'░' * amp_bar_len}{'█' * non_amp_bar_len}]  ║")
    print("╠" + "═" * 78 + "╣")
    print(f"║ 📄 Results file: {comparison_report_path:<59} ║")
    print("╚" + "═" * 78 + "╝")

    print("\n--- Pipeline Finished Successfully ---")

    # Citation message
    print("\n" + "="*80)
    print("If this tool supports your research, please cite:")
    print("Luna-Aragão, M. A., da Silva, R. L., Pacífico, J., Santos-Silva, C. A. & Benko-Iseppon, A. M. (2025).")
    print("AMPidentifier: A Python toolkit for predicting antimicrobial peptides using ensemble machine learning.")
    print("GitHub repository: https://github.com/madsondeluna/AMPIdentifier")
    print("="*80)
    print()