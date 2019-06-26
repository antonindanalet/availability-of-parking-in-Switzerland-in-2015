#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from pathlib import Path
from utils_mtmc.get_weighted_average_and_std import *
from compute_availability_of_parking_at_work import compute_av_parking_for_one_size_variable


def compute_availability_of_parking_space_at_work_by_agglo_size_home_loc(df_zp, results_for_all_zp):
    size_variable = 'W_AGGLO_GROESSE2012'
    dict_variable_labels = {0: 'Typology of home location: Outside of agglomerations',
                            1: "Typology of home location: Agglomerations with 500'000 inhabitants and more",
                            2: "Typology of home location: Agglomerations with 250'000 to 499'999 inhabitants",
                            3: "Typology of home location: Agglomerations with 100'000 to 249'999 inhabitants",
                            4: "Typology of home location: Agglomerations with 50'000 to 99'999 inhabitants",
                            5: "Typology of home location: Agglomerations with less than 50'000 inhabitants"}
    dict_labels_en2de = {'All households': 'Alle Haushalte',
                         'Typology of home location: Outside of agglomerations':
                             'Urbanisierungsgrad des Wohnorts: Keine Agglomerationszugehoerigkeit',
                         "Typology of home location: Agglomerations with 500'000 inhabitants and more":
                             "Urbanisierungsgrad des Wohnorts: Agglomerationen mit 500'000 Einwohner/innen und mehr",
                         "Typology of home location: Agglomerations with 250'000 to 499'999 inhabitants":
                             "Urbanisierungsgrad des Wohnorts: Agglomerationen mit 250'000 bis 499'999 Einwohner/innen",
                         "Typology of home location: Agglomerations with 100'000 to 249'999 inhabitants":
                             "Urbanisierungsgrad des Wohnorts: Agglomerationen mit 100'000 bis 249'999 Einwohner/innen",
                         "Typology of home location: Agglomerations with 50'000 to 99'999 inhabitants":
                             "Urbanisierungsgrad des Wohnorts: Agglomerationen mit 50'000 bis 99'999 Einwohner/innen",
                         "Typology of home location: Agglomerations with less than 50'000 inhabitants":
                             "Urbanisierungsgrad des Wohnorts: Agglomerationen mit weniger als 50'000 Einwohner/innen"}
    dict_labels_de2fr = {'Alle Haushalte': 'Tous les ménages',
                         'Urbanisierungsgrad des Wohnorts: Keine Agglomerationszugehoerigkeit':
                             "Degré d'urbanisation au domicile: Communes hors agglomérations",
                         "Urbanisierungsgrad des Wohnorts: Agglomerationen mit 500'000 Einwohner/innen und mehr":
                             "Degré d'urbanisation au domicile: Agglomérations de 500'000 habitants et plus",
                         "Urbanisierungsgrad des Wohnorts: Agglomerationen mit 250'000 bis 499'999 Einwohner/innen":
                             "Degré d'urbanisation au domicile: Agglomérations de 250'000 à 499'999 habitants",
                         "Urbanisierungsgrad des Wohnorts: Agglomerationen mit 100'000 bis 249'999 Einwohner/innen":
                             "Degré d'urbanisation au domicile: Agglomérations de 100'000 à 249'999 habitants",
                         "Urbanisierungsgrad des Wohnorts: Agglomerationen mit 50'000 bis 99'999 Einwohner/innen":
                             "Degré d'urbanisation au domicile: Agglomérations de 50'000 à 99'999 habitants",
                         "Urbanisierungsgrad des Wohnorts: Agglomerationen mit weniger als 50'000 Einwohner/innen":
                             "Degré d'urbanisation au domicile: Agglomérations de moins de 50'000 habitants"}
    file_name_en = 'availability_of_parking_space_at_work_by_agglo_size_home_loc.csv'
    file_name_de = 'verfueg_autoparkplaetzen_am_arbeitsort_nach_agglo_groesse_wohnort.csv'
    file_name_fr = 'dispo_place_stationnement_au_travail_selon_pop_agglo_domicile.csv'
    compute_av_parking_for_one_size_variable(df_zp, results_for_all_zp, size_variable, dict_variable_labels,
                                             dict_labels_en2de, dict_labels_de2fr,
                                             file_name_en, file_name_de, file_name_fr,
                                             folder_en='work_vs_home', folder_fr='travail_vs_domicile',
                                             folder_de='Arbeitsort_vs_zuHause')
    """ Results for larger groups of sizes for the agglomerations """
    dict_aggregation = {0: 0,
                        1: 1,
                        2: 1,
                        3: 2,
                        4: 2,
                        5: 3}
    size_variable_agg = 'A_AGGLO_GROESSE2012_agg'
    df_zp[size_variable_agg] = df_zp[size_variable].map(dict_aggregation)
    dict_variable_labels_agg = {0: 'Outside of agglomerations',
                                1: "Typology of home location: Agglomerations with 250'000 inhabitants and more",
                                2: "Typology of home location: Agglomerations with 50'000 to 249'999 inhabitants",
                                3: "Typology of home location: Agglomerations with less than 50'000 inhabitants"}
    dict_labels_en2de_agg = {'All households': 'Alle Haushalte',
                             'Typology of home location: Outside of agglomerations':
                                 'Urbanisierungsgrad des Wohnorts: Keine Agglomerationszugehoerigkeit',
                             "Typology of home location: Agglomerations with 250'000 inhabitants and more":
                                 "Urbanisierungsgrad des Wohnorts: Agglomerationen mit 250'000 Einwohner/innen und mehr",
                             "Typology of home location: Agglomerations with 50'000 to 249'999 inhabitants":
                                 "Urbanisierungsgrad des Wohnorts: Agglomerationen mit 50'000 bis 249'999 Einwohner/innen",
                             "Typology of home location: Agglomerations with less than 50'000 inhabitants":
                                 "Urbanisierungsgrad des Wohnorts: Agglomerationen mit weniger als 50'000 Einwohner/innen",
                             'Outside of agglomerations': 'Keine Agglomerationszugehoerigkeit'}
    dict_labels_de2fr_agg = {'Alle Haushalte': 'Tous les ménages',
                             'Urbanisierungsgrad des Wohnorts: Keine Agglomerationszugehoerigkeit':
                                 "Degré d'urbanisation au domicile: Communes hors agglomérations",
                             "Urbanisierungsgrad des Wohnorts: Agglomerationen mit 250'000 Einwohner/innen und mehr":
                                 "Degré d'urbanisation au domicile: Agglomérations de 250'000 habitants et plus",
                             "Urbanisierungsgrad des Wohnorts: Agglomerationen mit 50'000 bis 249'999 Einwohner/innen":
                                 "Degré d'urbanisation au domicile: Agglomérations de 50'000 à 249'999 habitants",
                             "Urbanisierungsgrad des Wohnorts: Agglomerationen mit weniger als 50'000 Einwohner/innen":
                                 "Degré d'urbanisation au domicile: Agglomérations de moins de 50'000 habitants",
                             'Keine Agglomerationszugehoerigkeit': 'Communes hors agglomérations'}
    file_name_en_agg = 'availability_of_parking_space_at_work_by_agglo_size_home_loc_agg.csv'
    file_name_de_agg = 'verfueg_autoparkplaetzen_am_arbeitsort_nach_agglo_groesse_wohnort_agg.csv'
    file_name_fr_agg = 'dispo_place_stationnement_au_travail_selon_pop_agglo_domicile_agg.csv'
    compute_av_parking_for_one_size_variable(df_zp, results_for_all_zp, size_variable_agg, dict_variable_labels_agg,
                                             dict_labels_en2de_agg, dict_labels_de2fr_agg,
                                             file_name_en_agg, file_name_de_agg, file_name_fr_agg,
                                             folder_en='work_vs_home', folder_fr='travail_vs_domicile',
                                             folder_de='Arbeitsort_vs_zuHause')


def compute_availability_of_parking_space_at_work_by_home_location(df_zp, results_for_all_zp):
    """ Availability of parking space at work by home location """
    parking_work_free_by_work_loc = df_zp.groupby('W_staedt_char_2012').apply(get_weighted_average_and_std,
                                                                              'parking_spaces_for_cars_at_work_free',
                                                                              name_weight='weight_person')
    parking_work_paid_by_work_loc = df_zp.groupby('W_staedt_char_2012').apply(get_weighted_average_and_std,
                                                                              'parking_spaces_for_cars_at_work_paid',
                                                                              name_weight='weight_person')
    parking_work_0_by_work_loc = df_zp.groupby('W_staedt_char_2012').apply(get_weighted_average_and_std,
                                                                           'parking_spaces_for_cars_at_work_0',
                                                                           name_weight='weight_person')
    # Generate a CSV-file with the results
    differentiation_by_work_loc = pd.concat([parking_work_free_by_work_loc,
                                             parking_work_paid_by_work_loc,
                                             parking_work_0_by_work_loc], axis=1)
    differentiation_by_work_loc.columns = ['Proportion with free parking space at work',
                                           'Standard deviation with free parking space at work',
                                           'Proportion with paid parking space at work',
                                           'Standard deviation with paid parking space at work',
                                           'Proportion without parking space at work',
                                           'Standard deviation without parking space at work']
    differentiation_by_work_loc.rename(index={0: 'Typology of home location: Rural municipalities without urban character',
                                              # in German: 0 = laendliche Gemeinde ohne staedtischen Charakter
                                              1: 'Typology of home location: Agglomeration core municipalities (core cities)',
                                              # in German: 1 = Agglomerationskerngemeinde (Kernstadt)
                                              2: 'Typology of home location: Agglomeration core municipalities (primary cores)',
                                              # in German: 2 = Agglomerationskerngemeinde (Hauptkern)
                                              3: 'Typology of home location: Agglomeration core municipalities (secondary cores)',
                                              # in German: 3 = Agglomerationskerngemeinde (Nebenkern)
                                              4: 'Typology of home location: Agglomeration commuting zone municipalities',
                                              # in German: 4 = Agglomerationsgürtelgemeinde
                                              5: 'Typology of home location: Municipalites oriented to multiple cores',
                                              # in German: 5 = Mehrfach orientierte Gemeinde
                                              6: 'Typology of home location: Core municipalities outside agglomeration',
                                              # in German: 6 = Kerngemeinde ausserhalb Agglomerationen
                                              }, inplace=True)
    file_name_en = 'availability_of_parking_space_at_work_by_home_location.csv'
    results_in_english = pd.concat([results_for_all_zp, differentiation_by_work_loc])
    results_in_english.to_csv(Path('../data/output/tables/EN/work_vs_home/' + file_name_en))
    print(file_name_en, 'saved in data/output/EN/work_vs_home')
    # Save results in German
    results_in_german = results_in_english
    results_in_german.rename(index={'All households': 'Alle Haushalte',
                                    'Typology of home location: Rural municipalities without urban character':
                                        'Urbanisierungsgrad des Wohnorts: '
                                        'laendliche Gemeinde ohne staedtischen Charakter',
                                    'Typology of home location: Agglomeration core municipalities (core cities)':
                                        'Urbanisierungsgrad des Wohnorts: Agglomerationskerngemeinde (Kernstadt)',
                                    'Typology of home location: Agglomeration core municipalities (primary cores)':
                                        'Urbanisierungsgrad des Wohnorts: Agglomerationskerngemeinde (Hauptkern)',
                                    'Typology of home location: Agglomeration core municipalities (secondary cores)':
                                        'Urbanisierungsgrad des Wohnorts: Agglomerationskerngemeinde (Nebenkern)',
                                    'Typology of home location: Agglomeration commuting zone municipalities':
                                        'Urbanisierungsgrad des Wohnorts: Agglomerationsguertelgemeinde',
                                    'Typology of home location: Municipalites oriented to multiple cores':
                                        'Urbanisierungsgrad des Wohnorts: Mehrfach orientierte Gemeinde',
                                    'Typology of home location: Core municipalities outside agglomeration':
                                        'Urbanisierungsgrad des Wohnorts: Kerngemeinde ausserhalb Agglomerationen'
                                    }, inplace=True)
    file_name_de = 'verfueg_autoparkplaetzen_am_arbeitsort_nach_wohnort_raumtyp.csv'
    results_in_german.to_csv(Path('../data/output/tables/DE/Arbeitsort_vs_zuHause/' + file_name_de),
                             header=['Anteil mit Gratisparkplatz', 'Standardabweichung mit Gratisparkplatz',
                                     'Anteil mit Bezahlparkplatz', 'Standardabweichung mit Bezahlparkplatz',
                                     'Anteil ohne Parkplatz', 'Standardabweichung ohne Parkplatz'])
    print(file_name_de, 'saved in data/output/DE/Arbeitsort_vs_zuHause')
    # Save results in French
    results_in_french = results_in_german
    results_in_french.rename(index={'Alle Haushalte': 'Tous les ménages',
                                    'Urbanisierungsgrad des Wohnorts: laendliche Gemeinde ohne staedtischen Charakter':
                                        "Degré d'urbanisation au domicile: Communes rurales sans caractère urbain",
                                    'Urbanisierungsgrad des Wohnorts: Agglomerationskerngemeinde (Kernstadt)':
                                        "Degré d'urbanisation au domicile: "
                                        "Communes-centres d'agglomération (villes-centres)",
                                    'Urbanisierungsgrad des Wohnorts: Agglomerationskerngemeinde (Hauptkern)':
                                        "Degré d'urbanisation au domicile: "
                                        "Communes-centres d'agglomération (centre principal)",
                                    'Urbanisierungsgrad des Wohnorts: Agglomerationskerngemeinde (Nebenkern)':
                                        "Degré d'urbanisation au domicile: "
                                        "Communes-centres d'agglomération (centre secondaire)",
                                    'Urbanisierungsgrad des Wohnorts: Agglomerationsguertelgemeinde':
                                        "Degré d'urbanisation au domicile: Communes de la couronne d'agglomération",
                                    'Urbanisierungsgrad des Wohnorts: Mehrfach orientierte Gemeinde':
                                        "Degré d'urbanisation au domicile: Communes multi-orientées",
                                    'Urbanisierungsgrad des Wohnorts: Kerngemeinde ausserhalb Agglomerationen':
                                        "Degré d'urbanisation au domicile: Communes-centre hors agglomération"
                                    }, inplace=True)
    file_name_fr = 'dispo_place_stationnement_au_travail_selon_typo_spatiale_domicile.csv'
    results_in_french.to_csv(Path('../data/output/tables/FR/travail_vs_domicile/' + file_name_fr),
                             encoding='iso-8859-1',
                             header=['Proportion avec place de stationnement gratuite',
                                     'Ecart type avec place de stationnement gratuite',
                                     'Proportion avec place de stationnement payante',
                                     'Ecart type avec place de stationnement payante',
                                     'Proportion sans place de stationnement',
                                     'Ecart type sans place de stationnement'])
    print(file_name_fr, 'saved in data/output/FR/travail_vs_domicile')

    """ Results by aggregated categories (similarly as in the main report) """
    dict_aggregation = {0: 3,  # laendliche Gemeinde ohne staedtischen Charaketer
                        1: 1,  # Staedtischer Kernraum
                        2: 1,  # Staetischer Kernraum
                        3: 1,  # Staedtischer Kernraum
                        4: 2,  # Einflussgebiet staedtischer Kerne
                        5: 2,  # Einflussgebiet staedtischer Kerne
                        6: 1}  # Staedtischer Kernraum
    df_zp['W_staedt_char_2012_agg'] = df_zp['W_staedt_char_2012'].map(dict_aggregation)
    parking_work_free_by_work_loc_agg = df_zp.groupby('W_staedt_char_2012_agg').apply(get_weighted_average_and_std,
                                                                                      'parking_spaces_for_cars_at_work_free',
                                                                                      name_weight='weight_person')
    parking_work_paid_by_work_loc_agg = df_zp.groupby('W_staedt_char_2012_agg').apply(get_weighted_average_and_std,
                                                                                      'parking_spaces_for_cars_at_work_paid',
                                                                                      name_weight='weight_person')
    parking_work_0_by_work_loc_agg = df_zp.groupby('W_staedt_char_2012_agg').apply(get_weighted_average_and_std,
                                                                                   'parking_spaces_for_cars_at_work_0',
                                                                                   name_weight='weight_person')
    # Generate a CSV-file with the results
    differentiation_by_work_loc_agg = pd.concat([parking_work_free_by_work_loc_agg,
                                                 parking_work_paid_by_work_loc_agg,
                                                 parking_work_0_by_work_loc_agg], axis=1)
    differentiation_by_work_loc_agg.columns = ['Proportion with free parking space at work',
                                               'Standard deviation with free parking space at work',
                                               'Proportion with paid parking space at work',
                                               'Standard deviation with paid parking space at work',
                                               'Proportion without parking space at work',
                                               'Standard deviation without parking space at work']
    differentiation_by_work_loc_agg.rename(index={1: 'Typology of home location: Urban core area',
                                                  # in German: Staedtischer Kernraum
                                                  2: 'Typology of home location: Area influenced by urban cores',
                                                  # in German: Einflussgebiet staedtischer Kerne
                                                  3: 'Typology of home location: Area beyond urban core influence',
                                                  # in German: laendliche Gemeinde ohne staedtischen Charaketer
                                                  }, inplace=True)
    file_name = 'availability_of_parking_space_at_work_by_home_location_agg.csv'
    results_in_english = pd.concat([results_for_all_zp, differentiation_by_work_loc_agg])
    results_in_english.to_csv(Path('../data/output/tables/EN/work_vs_home/' + file_name))
    print(file_name, 'saved in data/output/EN/work_vs_home')

    # results in German
    results_in_german = results_in_english
    results_in_german.rename(index={'All households': 'alle Haushalte',
                                    'Typology of home location: Urban core area':
                                        'Urbanisierungsgrad des Wohnorts: Staedtischer Kernraum',
                                    'Typology of home location: Area influenced by urban cores':
                                        'Urbanisierungsgrad des Wohnorts: Einflussgebiet staedtischer Kerne',
                                    'Typology of home location: Area beyond urban core influence':
                                        'Urbanisierungsgrad des Wohnorts: laendliche Gemeinde ohne staedtischen Charakter'
                                    }, inplace=True)
    file_name_de = 'verfueg_autoparkplaetzen_am_arbeitsort_nach_wohnort_raumtyp_agg.csv'
    results_in_german.to_csv(Path('../data/output/tables/DE/Arbeitsort_vs_zuHause/' + file_name_de),
                             header=['Anteil mit Gratisparkplatz', 'Standardabweichung mit Gratisparkplatz',
                                     'Anteil mit Bezahlparkplatz', 'Standardabweichung mit Bezahlparkplatz',
                                     'Anteil ohne Parkplatz', 'Standardabweichung ohne Parkplatz'])
    print(file_name_de, 'saved in data/output/DE/Arbeitsort_vs_zuHause')

    # Results in French
    results_in_french = results_in_german
    results_in_french.rename(index={'alle Haushalte': 'Tous les ménages',
                                    'Urbanisierungsgrad des Wohnorts: Staedtischer Kernraum':
                                        "Degré d'urbanisation au domicile: Espace des centres urbains",
                                    'Urbanisierungsgrad des Wohnorts: Einflussgebiet staedtischer Kerne':
                                        "Degré d'urbanisation au domicile: Espace sous influence des centres urbains",
                                    'Urbanisierungsgrad des Wohnorts: laendliche Gemeinde ohne staedtischen Charakter':
                                        "Degré d'urbanisation au domicile: Espace hors influence des centres urbains"
                                    }, inplace=True)
    file_name_fr = 'dispo_place_stationnement_au_travail_selon_typo_spatiale_domicile_agg.csv'
    results_in_french.to_csv(Path('../data/output/tables/FR/travail_vs_domicile/' + file_name_fr),
                             encoding='iso-8859-1',
                             header=['Proportion avec place de stationnement gratuite',
                                     'Ecart type avec place de stationnement gratuite',
                                     'Proportion avec place de stationnement payante',
                                     'Ecart type avec place de stationnement payante',
                                     'Proportion sans place de stationnement',
                                     'Ecart type sans place de stationnement'])
    print(file_name_fr, 'saved in data/output/FR/travail_vs_domicile')


def compute_no_availability_of_parking_space_by_type_home_work_loc(df_zp):
    df_zp['parking_spaces_for_cars_at_work_0_weighted'] = df_zp['parking_spaces_for_cars_at_work_0'] * \
                                                          df_zp['weight_person']
    results_no_parking_at_work_loc_hw_agg = (pd.crosstab(df_zp.A_staedt_char_2012_agg, df_zp.W_staedt_char_2012_agg,
                                                         values=df_zp.parking_spaces_for_cars_at_work_0_weighted,
                                                         aggfunc=sum, normalize=True, margins=True,
                                                         margins_name="Total"))
    results_no_parking_at_work_loc_hw_agg.columns = ['Typology of home location: Urban core area',
                                                     'Typology of home location: Area influenced by urban cores',
                                                     'Typology of home location: Area beyond urban core influence',
                                                     'Total']
    results_no_parking_at_work_loc_hw_agg.index = ['Typology of work location: Urban core area',
                                                   'Typology of work location: Area influenced by urban cores',
                                                   'Typology of work location: Area beyond urban core influence',
                                                   'Total']
    file_name = 'no_parking_space_at_work_by_home_work_location_agg.csv'
    results_no_parking_at_work_loc_hw_agg.to_csv(Path('../data/output/tables/EN/work_vs_home/' + file_name))
    print(file_name, 'saved in data/output/EN/work_vs_home')