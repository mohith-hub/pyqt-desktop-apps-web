import pandas as pd

def load_excel(file):
    return pd.read_excel(file)

def save_excel(df):
    return df.to_excel(index=False)
