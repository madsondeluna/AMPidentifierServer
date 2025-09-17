# amp_identifier/reporting.py

import pandas as pd
from typing import Dict

def save_features_report(features_df: pd.DataFrame, file_path: str):
    # This function remains unchanged
    try:
        features_df.to_csv(file_path, index=False)
    except Exception as e:
        print(f"Error saving features report to {file_path}: {e}")

def save_comparison_report(base_df: pd.DataFrame, predictions: Dict[str, pd.DataFrame], is_ensemble: bool, file_path: str):
    """
    Merges predictions and calculates a majority vote if in ensemble mode.
    """
    final_report_df = base_df[['ID', 'sequence']].copy()
    prediction_columns = []

    for model_name, result_df in predictions.items():
        if result_df is not None:
            # Add prediction and probability columns for each model
            pred_col_name = f'pred_{model_name}'
            prob_col_name = f'prob_{model_name}'
            
            # Store internal prediction column names for voting
            if 'internal' in model_name:
                prediction_columns.append(pred_col_name)

            report_cols = result_df[['ID', 'prediction', 'probability_AMP']].copy()
            report_cols.rename(columns={
                'prediction': pred_col_name,
                'probability_AMP': prob_col_name
            }, inplace=True)
            
            final_report_df = pd.merge(final_report_df, report_cols, on='ID', how='left')
    
    # --- NEW: Calculate majority vote if in ensemble mode ---
    if is_ensemble and prediction_columns:
        # Sum the predictions (1 for AMP, 0 for non-AMP) across all internal models
        final_report_df['ensemble_vote_sum'] = final_report_df[prediction_columns].sum(axis=1)
        
        # The final prediction is 1 (AMP) if the sum of votes is > half the number of models
        num_models = len(prediction_columns)
        final_report_df['ensemble_prediction'] = (final_report_df['ensemble_vote_sum'] > num_models / 2).astype(int)
    
    try:
        final_report_df.to_csv(file_path, index=False)
    except Exception as e:
        print(f"Error saving comparison report to {file_path}: {e}")