from utils_mtmc.get_mtmc_files import *
from utils_mtmc.get_weighted_average_and_std import *


def get_results_for_all_zp(df_zp):
    df_zp['nb_parking_spaces_for_cars_at_work_free'] = \
        df_zp['nb_parking_spaces_for_cars_at_work'].apply(lambda x: 1 if x == 1 else 0)
    df_zp['nb_parking_spaces_for_cars_at_work_paid'] = \
        df_zp['nb_parking_spaces_for_cars_at_work'].apply(lambda x: 1 if x == 2 else 0)
    df_zp['nb_parking_spaces_for_cars_at_work_0'] = \
        df_zp['nb_parking_spaces_for_cars_at_work'].apply(lambda x: 1 if x == 3 else 0)
    # Results for everyone
    weighted_avg_nb_parking_work_free, weigthed_std_parking_work_free = \
        get_weighted_average_and_std(df_zp, 'nb_parking_spaces_for_cars_at_work_free',
                                     name_weight = 'weight_person')
    weighted_avg_nb_parking_work_paid, weigthed_std_parking_work_paid = \
        get_weighted_average_and_std(df_zp, 'nb_parking_spaces_for_cars_at_work_paid',
                                     name_weight = 'weight_person')
    weighted_avg_nb_parking_work_0, weigthed_std_parking_work_0 = \
        get_weighted_average_and_std(df_zp, 'nb_parking_spaces_for_cars_at_work_0',
                                     name_weight = 'weight_person')
    # Group the results
    results_for_all_zp = pd.DataFrame({'Proportion with free parking at work': weighted_avg_nb_parking_work_free,
                                       'Standard deviation with free parking at work': weigthed_std_parking_work_free,
                                       'Proportion with paid parking at work': weighted_avg_nb_parking_work_paid,
                                       'Standard deviation with paid parking at work': weigthed_std_parking_work_paid,
                                       'Proportion without at work': weighted_avg_nb_parking_work_0,
                                       'Standard deviation without parking space at homes at work':
                                           weighted_avg_nb_parking_work_0
                                       }, index=['All households'])
    return results_for_all_zp


def get_data_person():
    """ Get the data about people that are needed and remove observations that are not valid """
    selected_columns = ['f41300',
                        'WP',
                        # 'f40900',
                        # 'f41100_01',
                        # 'f40800_01'
                        ]
    df_zp = get_zp(selected_columns=selected_columns)
    # Rename columns
    df_zp = df_zp.rename(columns={'f41300': 'nb_parking_spaces_for_cars_at_work',
                                  'WP': 'weight_person',
                                  # 'f40900': 'full_time',
                                  # 'f41100_01': 'position_in_company',
                                  # 'f40800_01': 'employement_status'
                                  })
    # Removing observations with answers "don't know" and "no answer"
    df_zp = df_zp[df_zp['nb_parking_spaces_for_cars_at_work'] != -98]  # no answer
    df_zp = df_zp[df_zp['nb_parking_spaces_for_cars_at_work'] != -97]  # don't know
    df_zp = df_zp[df_zp['nb_parking_spaces_for_cars_at_work'] != -99]  # younger than 18 or not part of this module or
                                                                       # not active (student and part time <50%)
    # df_zp = df_zp[df_zp['full_time'] != -97]  # don't know
    # df_zp = df_zp[df_zp['full_time'] != -98]  # no answer
    # df_zp = df_zp[df_zp['full_time'] != -99]  # not active
    # df_zp = df_zp[df_zp['position_in_company'] != -97]  # don't know
    # df_zp = df_zp[df_zp['position_in_company'] != -98]  # no answer
    # df_zp = df_zp[df_zp['employement_status'] != -99]  # no answer
    return df_zp