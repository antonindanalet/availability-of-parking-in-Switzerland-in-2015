from utils_mtmc.get_mtmc_files import *
import pandas as pd
from pathlib import Path


def run_availability_of_parking():
    """ Compute statistics about parking availability with spatial differentiation """
    df_hh = get_data_household()
    print('Basis:', len(df_hh.index))
    results_for_all_hh = get_results_for_all_hh(df_hh)
    compute_availability_of_parking_space_by_nb_of_cars(df_hh, results_for_all_hh)
    """ Results by type of place of living (full categories) """
    nb_parking_home_0_by_hh_loc = df_hh.groupby('W_staedt_char_2012').apply(get_weighted_average_and_std,
                                                                            'nb_parking_spaces_for_cars_at_home_0')
    nb_parking_home_1_by_hh_loc = df_hh.groupby('W_staedt_char_2012').apply(get_weighted_average_and_std,
                                                                            'nb_parking_spaces_for_cars_at_home_1')
    nb_parking_home_2_by_hh_loc = df_hh.groupby('W_staedt_char_2012').apply(get_weighted_average_and_std,
                                                                            'nb_parking_spaces_for_cars_at_home_2')
    nb_parking_home_3_by_hh_loc = df_hh.groupby('W_staedt_char_2012').apply(get_weighted_average_and_std,
                                                                            'nb_parking_spaces_for_cars_at_home_3+')
    # Generate a CSV-file with the results
    differentiation_by_hh_loc = pd.concat([nb_parking_home_0_by_hh_loc,
                                           nb_parking_home_1_by_hh_loc,
                                           nb_parking_home_2_by_hh_loc,
                                           nb_parking_home_3_by_hh_loc], axis=1)
    differentiation_by_hh_loc.columns = ['Proportion without parking space',
                                         'Standard deviation without parking space',
                                         'Proportion with 1 parking space',
                                         'Standard deviation with 1 parking space',
                                         'Proportion with 2 parking spaces',
                                         'Standard deviation with 2 parking spaces',
                                         'Proportion with 3 and more parking spaces',
                                         'Standard deviation with 3 and more parking spaces']
    differentiation_by_hh_loc.rename(index={0: 'Rural municipalities without urban character',
                                            # in German: 0 = laendliche Gemeinde ohne staedtischen Charaketer
                                            1: 'Agglomeration core municipalities (core cities)',
                                            # in German: 1 = Agglomerationskerngemeinde (Kernstadt)
                                            2: 'Agglomeration core municipalities (primary cores)',
                                            # in German: 2 = Agglomerationskerngemeinde (Hauptkern)
                                            3: 'Agglomeration core municipalities (secondary cores)',
                                            # in German: 3 = Agglomerationskerngemeinde (Nebenkern)
                                            4: 'Agglomeration commuting zone municipalities',
                                            # in German: 4 = Agglomerationsgürtelgemeinde
                                            5: 'Municipalites oriented to multiple cores',
                                            # in German: 5 = Mehrfach orientierte Gemeinde
                                            6: 'Core municipalities outside agglomeration',
                                            # in German: 6 = Kerngemeinde ausserhalb Agglomerationen
                                            }, inplace=True)
    file_name = 'availability_of_parking_space_by_household_location.csv'
    pd.concat([results_for_all_hh, differentiation_by_hh_loc]).to_csv(Path('../data/output/' + file_name))
    print(file_name, 'saved in data/output')

    """ Results by aggregated categories (similarly as in the main report) """
    dict_aggregation = {0: 3,  # laendliche Gemeinde ohne staedtischen Charaketer
                        1: 1,  # Staedtischer Kernraum
                        2: 1,  # Staetischer Kernraum
                        3: 1,  # Staedtischer Kernraum
                        4: 2,  # Einflussgebiet staedtischer Kerne
                        5: 2,  # Einflussgebiet staedtischer Kerne
                        6: 1}  # Staedtischer Kernraum
    df_hh['W_staedt_char_2012_agg'] = df_hh['W_staedt_char_2012'].map(dict_aggregation)
    nb_parking_home_0_by_hh_loc = df_hh.groupby('W_staedt_char_2012_agg').apply(get_weighted_average_and_std,
                                                                                'nb_parking_spaces_for_cars_at_home_0')
    nb_parking_home_1_by_hh_loc = df_hh.groupby('W_staedt_char_2012_agg').apply(get_weighted_average_and_std,
                                                                                'nb_parking_spaces_for_cars_at_home_1')
    nb_parking_home_2_by_hh_loc = df_hh.groupby('W_staedt_char_2012_agg').apply(get_weighted_average_and_std,
                                                                                'nb_parking_spaces_for_cars_at_home_2')
    nb_parking_home_3_by_hh_loc = df_hh.groupby('W_staedt_char_2012_agg').apply(get_weighted_average_and_std,
                                                                                'nb_parking_spaces_for_cars_at_home_3+')
    # Generate a CSV-file with the results
    differentiation_by_hh_loc = pd.concat([nb_parking_home_0_by_hh_loc,
                                           nb_parking_home_1_by_hh_loc,
                                           nb_parking_home_2_by_hh_loc,
                                           nb_parking_home_3_by_hh_loc], axis=1)
    differentiation_by_hh_loc.columns = ['Proportion without parking space',
                                         'Standard deviation without parking space',
                                         'Proportion with 1 parking space',
                                         'Standard deviation with 1 parking space',
                                         'Proportion with 2 parking spaces',
                                         'Standard deviation with 2 parking spaces',
                                         'Proportion with 3 and more parking spaces',
                                         'Standard deviation with 3 and more parking spaces']
    differentiation_by_hh_loc.rename(index={1: 'Staedtischer Kernraum',
                                            # in German: Staedtischer Kernraum
                                            2: 'Einflussgebiet staedtischer Kerne',
                                            # in German: Einflussgebiet staedtischer Kerne
                                            3: 'Rural municipalities without urban character',
                                            # in German: laendliche Gemeinde ohne staedtischen Charaketer
                                            }, inplace=True)
    file_name = 'availability_of_parking_space_by_household_location_agg.csv'
    pd.concat([results_for_all_hh, differentiation_by_hh_loc]).to_csv(Path('../data/output/' + file_name))
    print(file_name, 'saved in data/output')


def get_data_household():
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
    return df_hh


def get_results_for_all_hh(df_hh):
    """ Reproduce results from the main report (G 2.3.1.1) """
    # Replace all values higher than 3 by 3 in variable nb_parking... --> becomes category "3+ spaces for cars at home"
    df_hh['nb_parking_spaces_for_cars_at_home_0'] = \
        df_hh['nb_parking_spaces_for_cars_at_home'].apply(lambda x: 1 if x == 0 else 0)
    df_hh['nb_parking_spaces_for_cars_at_home_1'] = \
        df_hh['nb_parking_spaces_for_cars_at_home'].apply(lambda x: 1 if x == 1 else 0)
    df_hh['nb_parking_spaces_for_cars_at_home_2'] = \
        df_hh['nb_parking_spaces_for_cars_at_home'].apply(lambda x: 1 if x == 2 else 0)
    df_hh['nb_parking_spaces_for_cars_at_home_3+'] = \
        df_hh['nb_parking_spaces_for_cars_at_home'].apply(lambda x: 1 if x >= 3 else 0)
    # Results for all households
    weighted_avg_nb_parking_home_0, weigthed_std_parking_home_0 = \
        get_weighted_average_and_std(df_hh, 'nb_parking_spaces_for_cars_at_home_0')
    weighted_avg_nb_parking_home_1, weigthed_std_parking_home_1 = \
        get_weighted_average_and_std(df_hh, 'nb_parking_spaces_for_cars_at_home_1')
    weighted_avg_nb_parking_home_2, weigthed_std_parking_home_2 = \
        get_weighted_average_and_std(df_hh, 'nb_parking_spaces_for_cars_at_home_2')
    weighted_avg_nb_parking_home_3, weigthed_std_parking_home_3 = \
        get_weighted_average_and_std(df_hh, 'nb_parking_spaces_for_cars_at_home_3+')
    # Group the results
    results_for_all_hh = pd.DataFrame({'Proportion without parking space': weighted_avg_nb_parking_home_0,
                                       'Standard deviation without parking space': weigthed_std_parking_home_0,
                                       'Proportion with 1 parking space': weighted_avg_nb_parking_home_1,
                                       'Standard deviation with 1 parking space': weigthed_std_parking_home_1,
                                       'Proportion with 2 parking spaces': weighted_avg_nb_parking_home_2,
                                       'Standard deviation with 2 parking spaces': weigthed_std_parking_home_2,
                                       'Proportion with 3 and more parking spaces': weighted_avg_nb_parking_home_3,
                                       'Standard deviation with 3 and more parking spaces': weigthed_std_parking_home_3,
                                       }, index=['All households'])
    return results_for_all_hh


def compute_availability_of_parking_space_by_nb_of_cars(df_hh, results_for_all_hh):
    """ Reproduce results from the main report (G 2.3.1.1) """
    # Replace all values higher than 3 by 3 in variable nb_cars... --> becomes category "3+ cars owned by the hh"
    df_hh['nb_cars_in_household'] = df_hh['nb_cars_in_household'].apply(lambda x: x if x <= 3 else 3)
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
    file_name = 'availability_of_parking_space_by_nb_of_cars.csv'
    pd.concat([results_for_all_hh, differentiation_by_nb_cars]).to_csv(Path('../data/output/' + file_name))
    print(file_name, 'saved in data/output')


def get_weighted_average_and_std(df_zp, name_variable):
    nb_of_obs = len(df_zp.index)
    weighted_avg = (df_zp[name_variable] * df_zp['weight_household']).sum() / df_zp['weight_household'].sum()
    variance = np.divide(weighted_avg * (1.0-weighted_avg), float(nb_of_obs))
    weighted_std = 1.645 * 1.14 * np.sqrt(variance)
    return pd.Series({'Proportion': weighted_avg, 'Standard deviation': weighted_std})


if __name__ == '__main__':
    run_availability_of_parking()
