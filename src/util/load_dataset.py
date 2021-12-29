import pandas as pd

def load_dataset(filepath, names):
    return pd.read_csv(filepath,
                 encoding='ISO-8859-1', 
                 names=names)