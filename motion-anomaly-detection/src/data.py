import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Load raw motion data from a CSV file."""
    return pd.read_csv(path)


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Simple preprocessing for motion data."""
    df = df.dropna().reset_index(drop=True)
    return df
