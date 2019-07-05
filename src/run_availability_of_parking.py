from compute_availability_of_parking_at_home import *
from compute_availability_of_parking_at_work import *
from compute_availability_of_parking_at_work_vs_home import *


def run_availability_of_parking():
    """ Compute statistics about parking availability with spatial differentiation """
    df_hh = get_data_household()
    print('--- Number of parking spaces at home ---')
    print('Basis:', len(df_hh.index), 'households with valid information')
    results_for_all_hh = get_results_for_all_hh(df_hh)
    compute_availability_of_parking_space_by_nb_of_cars(df_hh, results_for_all_hh)
    compute_availability_of_parking_space_by_type_hh(df_hh, results_for_all_hh)
    compute_availability_of_parking_space_by_agglo_size(df_hh, results_for_all_hh)
    print('--- Availability of parking spaces at work ---')
    df_zp = get_data_person()  # zp = 'Zielperson' in German -> 'target person' in English
    print('Basis:', len(df_zp.index),
          'active persons 18 years old or older who answer the module about soft mobility and job occupation')
    results_for_all_zp = get_results_for_all_zp(df_zp)
    compute_availability_of_parking_space_by_type_work_loc(df_zp, results_for_all_zp)
    compute_availability_of_parking_space_by_agglo_size_work_loc(df_zp, results_for_all_zp)
    ''' Results about parking space at work with respect to home location '''
    print('--- Availability of parking spaces at work with respect to home location ---')
    df_zp = pd.merge(df_zp, df_hh[['HHNR',
                                   'W_staedt_char_2012_agg',
                                   'W_AGGLO_GROESSE2012_agg',
                                   'nb_parking_spaces_for_cars_at_home_0',
                                   'W_AGGLO_GROESSE2012',
                                   'W_staedt_char_2012']], on='HHNR', how='left')
    print('Basis:', len(df_zp.index),
          'active persons 18 years old or older who answer the module about soft mobility and job occupation')
    compute_availability_of_parking_space_by_type_home_work_loc(df_zp)
    compute_availability_of_parking_space_at_work_by_home_location(df_zp, results_for_all_zp)
    compute_availability_of_parking_space_at_work_by_agglo_size_home_loc(df_zp, results_for_all_zp)


if __name__ == '__main__':
    run_availability_of_parking()
