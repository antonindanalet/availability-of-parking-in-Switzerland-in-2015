import numpy as np
import pandas as pd


def get_weighted_average_and_std(df_zp, name_variable, name_weight):
    nb_of_obs = len(df_zp.index)
    weighted_avg = (df_zp[name_variable] * df_zp[name_weight]).sum() / df_zp[name_weight].sum()
    variance = np.divide(weighted_avg * (1.0-weighted_avg), float(nb_of_obs))
    weighted_std = 1.645 * 1.14 * np.sqrt(variance)
    return pd.Series({'Proportion': weighted_avg, 'Standard deviation': weighted_std})