import pandas as pd

def getData(filepath: str) -> any:
    df = pd.read_csv(filepath)
    return df