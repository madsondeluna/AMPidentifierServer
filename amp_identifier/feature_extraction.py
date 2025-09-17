# amp_identifier/feature_extraction.py

import pandas as pd
from modlamp.descriptors import GlobalDescriptor
from typing import List

def calculate_physicochemical_features(sequences: List[str], ids: List[str]) -> pd.DataFrame:
    """
    Calculates a set of physicochemical features for a list of sequences.

    Args:
        sequences (List[str]): A list of amino acid sequences.
        ids (List[str]): A list of corresponding sequence identifiers.

    Returns:
        pd.DataFrame: A DataFrame where each row corresponds to a sequence
                      and each column to a feature.
    """
    if not sequences:
        return pd.DataFrame()

    # Instantiate the descriptor
    desc = GlobalDescriptor(sequences)
    
    # Calculate a comprehensive set of features
    desc.calculate_all(amide=True)
    
    # Get the feature names and the results array from the descriptor
    feature_names = desc.featurenames 
    feature_array = desc.descriptor

    # Convert the numpy array to a pandas DataFrame with the correct column names
    features_df = pd.DataFrame(feature_array, columns=feature_names)

    # Now the .insert() method will work correctly
    features_df.insert(0, 'ID', ids)
    features_df.insert(1, 'sequence', sequences)
        
    return features_df