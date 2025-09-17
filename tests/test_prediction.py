# tests/test_prediction.py

import os
import shutil
import pandas as pd
import joblib
import pytest
from sklearn.linear_model import LogisticRegression

# Import the functions to be tested from your application code
from amp_identifier.prediction import load_model, predict_sequences

# Define a test class to structure the tests
class TestPrediction:
    """
    Test suite for the prediction module.
    """
    # --- Test Setup and Teardown ---
    
    @classmethod
    def setup_class(cls):
        """
        Set up a temporary environment for the tests.
        This runs once before all tests in this class.
        """
        # Create a temporary directory for test artifacts
        cls.test_dir = "tests/temp_test_assets"
        os.makedirs(cls.test_dir, exist_ok=True)
        
        # Create a simple, predictable dummy model
        # Train a model on a tiny, non-random dataset
        X_dummy = pd.DataFrame({'feature1': [1, 2, 10, 11], 'feature2': [0, 0, 5, 5]})
        y_dummy = [0, 0, 1, 1]
        dummy_model = LogisticRegression()
        dummy_model.fit(X_dummy, y_dummy)
        
        # Save the dummy model
        cls.dummy_model_path = os.path.join(cls.test_dir, "dummy_model.pkl")
        joblib.dump(dummy_model, cls.dummy_model_path)

        # Create a dummy features dataframe for prediction
        cls.dummy_features_df = pd.DataFrame({
            'ID': ['test_seq_1', 'test_seq_2'],
            'sequence': ['ACDE', 'NPQR'],
            'feature1': [1.5, 10.5], # One should be class 0, the other class 1
            'feature2': [0.1, 4.9]
        })

    @classmethod
    def teardown_class(cls):
        """
        Clean up the temporary environment after all tests are done.
        This runs once after all tests in this class.
        """
        shutil.rmtree(cls.test_dir)

    # --- Test Cases ---

    def test_load_model_success(self):
        """
        Test that a valid model file is loaded correctly.
        """
        model = load_model(self.dummy_model_path)
        assert model is not None
        assert hasattr(model, 'predict') # Check if it's a model-like object

    def test_load_model_file_not_found(self):
        """
        Test that loading a non-existent model returns None.
        """
        model = load_model("non_existent_path.pkl")
        assert model is None

    def test_predict_sequences_valid_input(self):
        """
        Test the main prediction function with valid inputs.
        """
        # Load the dummy model
        model = load_model(self.dummy_model_path)
        
        # Perform prediction
        results_df = predict_sequences(model, self.dummy_features_df)

        # Assertions to check the output
        assert results_df is not None
        assert isinstance(results_df, pd.DataFrame)
        assert len(results_df) == 2
        assert 'prediction' in results_df.columns
        assert 'probability_AMP' in results_df.columns
        
        # Check the actual predicted values based on the dummy model
        # seq_1 (feature1=1.5) should be predicted as 0
        # seq_2 (feature1=10.5) should be predicted as 1
        assert results_df['prediction'].iloc[0] == 0
        assert results_df['prediction'].iloc[1] == 1
        assert results_df['probability_AMP'].iloc[0] < 0.5
        assert results_df['probability_AMP'].iloc[1] > 0.5

    def test_predict_sequences_missing_feature(self):
        """
        Test prediction when the input dataframe is missing a feature column.
        """
        model = load_model(self.dummy_model_path)
        
        # Create a dataframe with a missing feature
        features_with_missing_col = self.dummy_features_df.drop(columns=['feature2'])
        
        # The function should handle this gracefully and return None
        results_df = predict_sequences(model, features_with_missing_col)
        
        assert results_df is None