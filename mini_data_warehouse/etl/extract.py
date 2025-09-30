import pandas as pd

def extract_csv(file_path='data/sales.csv'):
    """Extract data from CSV"""
    return pd.read_csv(file_path)
