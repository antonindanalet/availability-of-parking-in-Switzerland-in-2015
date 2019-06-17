from utils_mtmc.get_mtmc_files import *
import pandas as pd
from pathlib import Path


def run_availability_of_parking():
    """ Compute statistics about parking availability with spatial differentiation """
    """ Get the data and remove observations that are not valid """
    selected_columns = ['f31100',
                        'WM',
                        'f30100',
                        'W_staedt_char_2012']
    df_hh = get_hh(selected_columns=selected_columns)
    # Rename columns
    df_hh = df_hh.rename(columns={'f31100': 'nb_parking_spaces_for_cars_at_home',
                                  'WM': 'weight_household',
                                  'f30100': 'nb_cars_in_household'})
    # Removing observations with answers "don't know" and "no answer"
    df_hh = df_hh[df_hh['nb_parking_spaces_for_cars_at_home'] != -98]
    df_hh = df_hh[df_hh['nb_parking_spaces_for_cars_at_home'] != -97]
    df_hh = df_hh[df_hh['nb_cars_in_household'] != -97]
    df_hh = df_hh[df_hh['nb_cars_in_household'] != -98]
    print('Basis:', len(df_hh.index))
    """ Reproduce results from the main report """
    # Replace all values higher than 3 by 3 in variable nb_parking... --> becomes category "3+ spaces for cars at home"
    df_hh['nb_parking_spaces_for_cars_at_home_0'] = \
        df_hh['nb_parking_spaces_for_cars_at_home'].apply(lambda x: 1 if x == 0 else 0)
    df_hh['nb_parking_spaces_for_cars_at_home_1'] = \
        df_hh['nb_parking_spaces_for_cars_at_home'].apply(lambda x: 1 if x == 1 else 0)
    df_hh['nb_parking_spaces_for_cars_at_home_2'] = \
        df_hh['nb_parking_spaces_for_cars_at_home'].apply(lambda x: 1 if x == 2 else 0)
    df_hh['nb_parking_spaces_for_cars_at_home_3+'] = \
        df_hh['nb_parking_spaces_for_cars_at_home'].apply(lambda x: 1 if x >= 3 else 0)
    # Replace all values higher than 3 by 3 in variable nb_cars... --> becomes category "3+ cars owned by the hh"
    df_hh['nb_cars_in_household'] = df_hh['nb_cars_in_household'].apply(lambda x: x if x <= 3 else 3)
    # Results for all households
    weighted_avg_nb_parking_home_0, weigthed_std_parking_home_0 = \
        get_weighted_average_and_std(df_hh, 'nb_parking_spaces_for_cars_at_home_0')
    weighted_avg_nb_parking_home_1, weigthed_std_parking_home_1 = \
        get_weighted_average_and_std(df_hh, 'nb_parking_spaces_for_cars_at_home_1')
    weighted_avg_nb_parking_home_2, weigthed_std_parking_home_2 = \
        get_weighted_average_and_std(df_hh, 'nb_parking_spaces_for_cars_at_home_2')
    weighted_avg_nb_parking_home_3plus, weigthed_std_parking_home_3plus = \
        get_weighted_average_and_std(df_hh, 'nb_parking_spaces_for_cars_at_home_3+')
    # Results depending on number of cars in the household
    nb_parking_home_0_by_nb_cars = df_hh.groupby('nb_cars_in_household').apply(get_weighted_average_and_std,
                                                                               'nb_parking_spaces_for_cars_at_home_0')
    nb_parking_home_1_by_nb_cars = df_hh.groupby('nb_cars_in_household').apply(get_weighted_average_and_std,
                                                                               'nb_parking_spaces_for_cars_at_home_1')
    nb_parking_home_2_by_nb_cars = df_hh.groupby('nb_cars_in_household').apply(get_weighted_average_and_std,
                                                                               'nb_parking_spaces_for_cars_at_home_2')
    nb_parking_home_3_by_nb_cars = df_hh.groupby('nb_cars_in_household').apply(get_weighted_average_and_std,
                                                                               'nb_parking_spaces_for_cars_at_home_3+')
    # Generate a CSV-file with the results
    general_results = pd.DataFrame({'Proportion without parking space': weighted_avg_nb_parking_home_0,
                                    'Standard deviation without parking space': weigthed_std_parking_home_0,
                                    'Proportion with 1 parking space': weighted_avg_nb_parking_home_1,
                                    'Standard deviation with 1 parking space': weigthed_std_parking_home_1,
                                    'Proportion with 2 parking spaces': weighted_avg_nb_parking_home_2,
                                    'Standard deviation with 2 parking spaces': weigthed_std_parking_home_2,
                                    'Proportion with 3 and more parking spaces': weighted_avg_nb_parking_home_3plus,
                                    'Standard deviation with 3 and more parking spaces': weigthed_std_parking_home_3plus,
                                    }, index=['All households'])
    differentiation_by_nb_cars = pd.concat([nb_parking_home_0_by_nb_cars,
                                            nb_parking_home_1_by_nb_cars,
                                            nb_parking_home_2_by_nb_cars,
                                            nb_parking_home_3_by_nb_cars], axis = 1)
    differentiation_by_nb_cars.columns = ['Proportion without parking space',
                                    'Standard deviation without parking space',
                                    'Proportion with 1 parking space',
                                    'Standard deviation with 1 parking space',
                                    'Proportion with 2 parking spaces',
                                    'Standard deviation with 2 parking spaces',
                                    'Proportion with 3 and more parking spaces',
                                    'Standard deviation with 3 and more parking spaces']
    differentiation_by_nb_cars.rename(index={0: 'No car in the household',
                                             1: '1 car in the household',
                                             2: '2 cars in the household',
                                             3: '3 and more cars in the household'}, inplace=True)
    file_name = 'Availability_of_parking_space_by_nb_of_cars.csv'
    pd.concat([general_results, differentiation_by_nb_cars]).to_csv(Path('../data/output/' + file_name))
    print(file_name, 'saved in data/output')
    """ Results by type of place of living: urban, rural, etc. """
    # print(df_hh.groupby('W_staedt_char_2012').apply(get_weighted_average_and_std,
    #                                                 'nb_parking_spaces_for_cars_at_home_0'))
    # print(df_hh.groupby('W_staedt_char_2012').apply(get_weighted_average_and_std,
    #                                                 'nb_parking_spaces_for_cars_at_home_1'))
    # print(df_hh.groupby('W_staedt_char_2012').apply(get_weighted_average_and_std,
    #                                                 'nb_parking_spaces_for_cars_at_home_2'))
    # print(df_hh.groupby('W_staedt_char_2012').apply(get_weighted_average_and_std,
    #                                                 'nb_parking_spaces_for_cars_at_home_3+'))


def get_weighted_average_and_std(df_zp, name_variable):
    nb_of_obs = len(df_zp['weight_household'].unique())
    weighted_avg = (df_zp[name_variable] * df_zp['weight_household']).sum() / df_zp['weight_household'].sum()
    variance = np.divide((df_zp['weight_household'] * ((df_zp[name_variable] - weighted_avg) ** 2)).sum(),
                         df_zp['weight_household'].sum() - 1)
    weighted_std = np.divide(1.645 * 1.14 * np.sqrt(variance), np.sqrt(nb_of_obs))
    return pd.Series({'Proportion': weighted_avg, 'Standard deviation': weighted_std})


if __name__ == '__main__':
    run_availability_of_parking()
