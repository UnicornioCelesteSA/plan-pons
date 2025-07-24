import pandas as pd

def load_cirugias(path):
    return pd.read_excel(path)

def load_desmontaje(path):
    return pd.read_excel(path)
