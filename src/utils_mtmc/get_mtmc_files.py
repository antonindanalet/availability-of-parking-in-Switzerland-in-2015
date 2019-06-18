import pandas as pd
import numpy as np
from pathlib import Path
import os


folder_path = Path('../data/input/')


def get_hh(selected_columns=None):
    with open(folder_path / 'haushalte.csv', 'r') as haushalte_file:
        df_hh = pd.read_csv(haushalte_file,
                            dtype={'HHNR': int},
                            usecols=selected_columns)
    return df_hh


def get_zp(selected_columns=None):
        path_2_zielpersonen = os.path.join('..', 'data', 'input', )
        if os.path.isfile(folder_path / 'zielpersonen.csv'):
            with open(folder_path / 'zielpersonen.csv', 'r', encoding='latin1') as zielpersonen_file:
                if selected_columns is None:
                    df_zp = pd.read_csv(zielpersonen_file)
                else:
                    df_zp = pd.read_csv(zielpersonen_file,
                                        dtype={'HHNR': int},
                                        usecols=selected_columns)
                return df_zp
        else:
            raise Exception('File "zielpersonen.csv" not in the folder "data/input". Please copy it there.')
