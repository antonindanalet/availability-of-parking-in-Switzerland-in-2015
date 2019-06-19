#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from pathlib import Path
from compute_availability_of_parking_at_home import *
from compute_availability_of_parking_at_work import *


def run_availability_of_parking():
    """ Compute statistics about parking availability with spatial differentiation """
    df_hh = get_data_household()
    print('--- Number of parking spaces at home ---')
    print('Basis:', len(df_hh.index), 'households with valid information')
    results_for_all_hh = get_results_for_all_hh(df_hh)
    compute_availability_of_parking_space_by_nb_of_cars(df_hh, results_for_all_hh)
    compute_availability_of_parking_space_by_type_hh(df_hh, results_for_all_hh)
    compute_availability_of_parking_space_by_agglo_size(df_hh, results_for_all_hh)
    print('--- Number of parking spaces at work ---')
    df_zp = get_data_person()  # zp = 'Zielperson' in German -> 'target person' in English
    print('Basis:', len(df_zp.index),
          'active persons 18 years old or older who answer this module about soft mobility and job occupation')
    results_for_all_zp = get_results_for_all_zp(df_zp)


if __name__ == '__main__':
    run_availability_of_parking()
