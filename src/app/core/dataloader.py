import pandas as pd


def load_csv(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    # TODO : Ajouter preprocessing
    return df
