# amp_identifier/data_io.py

from Bio import SeqIO
from typing import List, Tuple

def load_fasta_sequences(file_path: str) -> Tuple[List[str], List[str]]:
    """
    Loads sequences and their IDs from a FASTA file.

    Args:
        file_path (str): The path to the FASTA file.

    Returns:
        Tuple[List[str], List[str]]: A tuple containing a list of sequences 
                                     and a list of their corresponding IDs.
    """
    sequences = []
    ids = []
    try:
        for record in SeqIO.parse(file_path, "fasta"):
            sequences.append(str(record.seq))
            ids.append(record.id)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return [], []
    except Exception as e:
        print(f"An error occurred while reading the FASTA file: {e}")
        return [], []
    
    return sequences, ids