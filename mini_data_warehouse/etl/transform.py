def clean_data(df):
    """Clean and standardize data"""
    df = df.dropna()
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    return df
