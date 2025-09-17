# main.py

import argparse
import os
from amp_identifier.core import run_prediction_pipeline

def main():
    """
    Main function to parse command-line arguments and run the prediction pipeline.
    """
    parser = argparse.ArgumentParser(
        description="AMP Identifier: A tool for Antimicrobial Peptide prediction and analysis.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument(
        "-i", "--input",
        required=True,
        type=str,
        help="Path to the input file containing sequences (FASTA format)."
    )
    parser.add_argument(
        "-o", "--output_dir",
        required=True,
        type=str,
        help="Directory where the result files will be saved."
    )
    # --- UPDATED: Argument to choose a specific internal model ---
    parser.add_argument(
        "-m", "--model",
        type=str,
        default='rf',
        choices=['rf', 'svm', 'gb'],
        help="Type of internal model to use for prediction. (default: rf)."
    )
    # --- NEW: Argument to trigger ensemble voting ---
    parser.add_argument(
        "--ensemble",
        action='store_true',  # This makes it a flag, e.g., --ensemble
        help="Use all internal models and predict by majority vote."
    )
    parser.add_argument(
        "-e", "--external_models",
        nargs='*',
        type=str,
        default=[],
        help="List of paths to external .pkl models for comparison."
    )

    args = parser.parse_args()

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
        print(f"Created output directory: {args.output_dir}")

    run_prediction_pipeline(
        input_file=args.input,
        output_dir=args.output_dir,
        internal_model_type=args.model,
        use_ensemble=args.ensemble,
        external_model_paths=args.external_models
    )

if __name__ == "__main__":
    main()