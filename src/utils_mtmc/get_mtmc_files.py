import pandas as pd
import numpy as np
from pathlib import Path


folder_path = Path('../data/input/')


def get_hh(selected_columns=None):
    with open(folder_path / 'haushalte.csv', 'r') as haushalte_file:
        df_hh = pd.read_csv(haushalte_file,
                            dtype={'HHNR': int},
                            usecols=selected_columns)
    return df_hh