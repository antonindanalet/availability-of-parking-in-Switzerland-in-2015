#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils_mtmc.get_mtmc_files import *
from utils_mtmc.get_weighted_average_and_std import *


def compute_availability_of_parking_space_by_agglo_size_work_loc(df_zp, results_for_all_zp):
    size_variable = 'A_AGGLO_GROESSE2012'
    dict_variable_labels = {0: 'Outside of agglomerations',
                            1: "Agglomerations with 500'000 inhabitants and more",
                            2: "Agglomerations with 250'000 to 499'999 inhabitants",
                            3: "Agglomerations with 100'000 to 249'999 inhabitants",
                            4: "Agglomerations with 50'000 to 99'999 inhabitants",
                            5: "Agglomerations with less than 50'000 inhabitants"}
    dict_labels_en2de = {'All households': 'Alle Haushalte',
                         'Outside of agglomerations': 'Keine Agglomerationszugehoerigkeit',
                         "Agglomerations with 500'000 inhabitants and more":
                             "Agglomerationen mit 500'000 Einwohner/innen und mehr",
                         "Agglomerations with 250'000 to 499'999 inhabitants":
                             "Agglomerationen mit 250'000 bis 499'999 Einwohner/innen",
                         "Agglomerations with 100'000 to 249'999 inhabitants":
                             "Agglomerationen mit 100'000 bis 249'999 Einwohner/innen",
                         "Agglomerations with 50'000 to 99'999 inhabitants":
                             "Agglomerationen mit 50'000 bis 99'999 Einwohner/innen",
                         "Agglomerations with less than 50'000 inhabitants":
                             "Agglomerationen mit weniger als 50'000 Einwohner/innen"}
    dict_labels_de2fr = {'Alle Haushalte': 'Tous les ménages',
                         'Keine Agglomerationszugehoerigkeit': 'Communes hors agglomérations',
                         "Agglomerationen mit 500'000 Einwohner/innen und mehr":
                             "Agglomérations de 500'000 habitants et plus",
                         "Agglomerationen mit 250'000 bis 499'999 Einwohner/innen":
                             "Agglomérations de 250'000 à 499'999 habitants",
                         "Agglomerationen mit 100'000 bis 249'999 Einwohner/innen":
                             "Agglomérations de 100'000 à 249'999 habitants",
                         "Agglomerationen mit 50'000 bis 99'999 Einwohner/innen":
                             "Agglomérations de 50'000 à 99'999 habitants",
                         "Agglomerationen mit weniger als 50'000 Einwohner/innen":
                             "Agglomérations de moins de 50'000 habitants"}
    file_name_en = 'avail_parking_space_by_agglo_size_work_loc.csv'
    file_name_de = 'verfueg_autoparkplaetzen_nach_agglo_groesse_arbeitstort.csv'
    file_name_fr = 'dispo_place_stationnement_selon_pop_agglo_travail.csv'
    compute_av_parking_for_one_size_variable(df_zp, results_for_all_zp, size_variable, dict_variable_labels,
                                             dict_labels_en2de, dict_labels_de2fr,
                                             file_name_en, file_name_de, file_name_fr)
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
                                1: "Agglomerations with 250'000 inhabitants and more",
                                2: "Agglomerations with 50'000 to 249'999 inhabitants",
                                3: "Agglomerations with less than 50'000 inhabitants"}
    dict_labels_en2de_agg = {'All households': 'Alle Haushalte',
                             'Outside of agglomerations': 'Keine Agglomerationszugehoerigkeit',
                             "Agglomerations with 250'000 inhabitants and more":
                                 "Agglomerationen mit 250'000 Einwohner/innen und mehr",
                             "Agglomerations with 50'000 to 249'999 inhabitants":
                                 "Agglomerationen mit 50'000 bis 249'999 Einwohner/innen",
                             "Agglomerations with less than 50'000 inhabitants":
                                 "Agglomerationen mit weniger als 50'000 Einwohner/innen"}
    dict_labels_de2fr_agg = {'Alle Haushalte': 'Tous les ménages',
                             'Keine Agglomerationszugehoerigkeit': 'Communes hors agglomérations',
                             "Agglomerationen mit 250'000 Einwohner/innen und mehr":
                                 "Agglomérations de 250'000 habitants et plus",
                             "Agglomerationen mit 50'000 bis 249'999 Einwohner/innen":
                                 "Agglomérations de 50'000 à 249'999 habitants",
                             "Agglomerationen mit weniger als 50'000 Einwohner/innen":
                                 "Agglomérations de moins de 50'000 habitants"}
    file_name_en_agg = 'avail_parking_space_by_agglo_size_work_loc_agg.csv'
    file_name_de_agg = 'verfueg_autoparkplaetzen_nach_agglo_groesse_arbeitsort_agg.csv'
    file_name_fr_agg = 'dispo_place_stationnement_selon_pop_agglo_travail_agg.csv'
    compute_av_parking_for_one_size_variable(df_zp, results_for_all_zp, size_variable_agg, dict_variable_labels_agg,
                                             dict_labels_en2de_agg, dict_labels_de2fr_agg,
                                             file_name_en_agg, file_name_de_agg, file_name_fr_agg)


def compute_av_parking_for_one_size_variable(df_zp, results_for_all_zp, size_variable, dict_variable_labels,
                                             dict_labels_en2de, dict_labels_de2fr,
                                             file_name_en, file_name_de,file_name_fr,
                                             folder_en='work', folder_fr='travail', folder_de='Arbeitsort'):
    """ Results by size of the agglomeration the household is located in """
    parking_work_free_by_agglo_size_work = df_zp.groupby(size_variable).apply(get_weighted_average_and_std,
                                                                              'parking_spaces_for_cars_at_work_free',
                                                                              name_weight='weight_person')
    parking_work_paid_by_agglo_size_work = df_zp.groupby(size_variable).apply(get_weighted_average_and_std,
                                                                              'parking_spaces_for_cars_at_work_paid',
                                                                              name_weight='weight_person')
    parking_work_0_by_agglo_size_work = df_zp.groupby(size_variable).apply(get_weighted_average_and_std,
                                                                           'parking_spaces_for_cars_at_work_0',
                                                                           name_weight='weight_person')
    # Generate a CSV-file with the results
    differentiation_by_agglo_size = pd.concat([parking_work_free_by_agglo_size_work,
                                               parking_work_paid_by_agglo_size_work,
                                               parking_work_0_by_agglo_size_work], axis=1)
    differentiation_by_agglo_size.columns = ['Proportion with free parking space at work',
                                             'Standard deviation with free parking space at work',
                                             'Proportion with paid parking space at work',
                                             'Standard deviation with paid parking space at work',
                                             'Proportion without parking space at work',
                                             'Standard deviation without parking space at work']
    differentiation_by_agglo_size.rename(index=dict_variable_labels, inplace=True)
    results_in_english = pd.concat([results_for_all_zp, differentiation_by_agglo_size])
    results_in_english.to_csv(Path('../data/output/tables/EN/' + folder_en + '/' + file_name_en))
    print(file_name_en, 'saved in data/output/EN/' + folder_en)
    # Save results in German
    results_in_german = results_in_english
    results_in_german.rename(index=dict_labels_en2de, inplace=True)
    results_in_german.to_csv(Path('../data/output/tables/DE/' + folder_de + '/' + file_name_de),
                             header=['Anteil mit Gratisparkplatz', 'Standardabweichung mit Gratisparkplatz',
                                     'Anteil mit Bezahlparkplatz', 'Standardabweichung mit Bezahlparkplatz',
                                     'Anteil ohne Parkplatz', 'Standardabweichung ohne Parkplatz'])
    print(file_name_de, 'saved in data/output/DE/' + folder_de)
    # Save results in French
    results_in_french = results_in_german
    results_in_french.rename(index=dict_labels_de2fr, inplace=True)
    results_in_french.to_csv(Path('../data/output/tables/FR/' + folder_fr + '/' + file_name_fr),
                             encoding='iso-8859-1',
                             header=['Proportion avec place de stationnement gratuite',
                                     'Ecart type avec place de stationnement gratuite',
                                     'Proportion avec place de stationnement payante',
                                     'Ecart type avec place de stationnement payante',
                                     'Proportion sans place de stationnement',
                                     'Ecart type sans place de stationnement'])
    print(file_name_fr, 'saved in data/output/FR/' + folder_fr)


def compute_availability_of_parking_space_by_type_work_loc(df_zp, results_for_all_zp):
    """ Results by type of place of living (full categories) """
    parking_work_free_by_work_loc = df_zp.groupby('A_staedt_char_2012').apply(get_weighted_average_and_std,
                                                                              'parking_spaces_for_cars_at_work_free',
                                                                              name_weight='weight_person')
    parking_work_paid_by_work_loc = df_zp.groupby('A_staedt_char_2012').apply(get_weighted_average_and_std,
                                                                              'parking_spaces_for_cars_at_work_paid',
                                                                              name_weight='weight_person')
    parking_work_0_by_work_loc = df_zp.groupby('A_staedt_char_2012').apply(get_weighted_average_and_std,
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
    differentiation_by_work_loc.rename(index={0: 'Rural municipalities without urban character',
                                              # in German: 0 = laendliche Gemeinde ohne staedtischen Charakter
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
    file_name_en = 'avail_parking_space_by_work_location.csv'
    results_in_english = pd.concat([results_for_all_zp, differentiation_by_work_loc])
    results_in_english.to_csv(Path('../data/output/tables/EN/work/' + file_name_en))
    print(file_name_en, 'saved in data/output/EN/work')
    # Save results in German
    results_in_german = results_in_english
    results_in_german.rename(index={'All households': 'Alle Haushalte',
                                    'Rural municipalities without urban character':
                                        'laendliche Gemeinde ohne staedtischen Charakter',
                                    'Agglomeration core municipalities (core cities)':
                                        'Agglomerationskerngemeinde (Kernstadt)',
                                    'Agglomeration core municipalities (primary cores)':
                                        'Agglomerationskerngemeinde (Hauptkern)',
                                    'Agglomeration core municipalities (secondary cores)':
                                        'Agglomerationskerngemeinde (Nebenkern)',
                                    'Agglomeration commuting zone municipalities': 'Agglomerationsguertelgemeinde',
                                    'Municipalites oriented to multiple cores': 'Mehrfach orientierte Gemeinde',
                                    'Core municipalities outside agglomeration':
                                        'Kerngemeinde ausserhalb Agglomerationen'
                                    }, inplace=True)
    file_name_de = 'verfueg_autoparkplaetzen_nach_arbeitsort_raumtyp.csv'
    results_in_german.to_csv(Path('../data/output/tables/DE/Arbeitsort/' + file_name_de),
                             header=['Anteil mit Gratisparkplatz', 'Standardabweichung mit Gratisparkplatz',
                                     'Anteil mit Bezahlparkplatz', 'Standardabweichung mit Bezahlparkplatz',
                                     'Anteil ohne Parkplatz', 'Standardabweichung ohne Parkplatz'])
    print(file_name_de, 'saved in data/output/DE/Arbeitsort')
    # Save results in French
    results_in_french = results_in_german
    results_in_french.rename(index={'Alle Haushalte': 'Tous les ménages',
                                    'laendliche Gemeinde ohne staedtischen Charakter':
                                        'Communes rurales sans caractère urbain',
                                    'Agglomerationskerngemeinde (Kernstadt)':
                                        "Communes-centres d'agglomération (villes-centres)",
                                    'Agglomerationskerngemeinde (Hauptkern)':
                                        "Communes-centres d'agglomération (centre principal)",
                                    'Agglomerationskerngemeinde (Nebenkern)':
                                        "Communes-centres d'agglomération (centre secondaire)",
                                    'Agglomerationsguertelgemeinde': "Communes de la couronne d'agglomération",
                                    'Mehrfach orientierte Gemeinde': 'Communes multi-orientées',
                                    'Kerngemeinde ausserhalb Agglomerationen':
                                        'Communes-centre hors agglomération'
                                    }, inplace=True)
    file_name_fr = 'dispo_place_stationnement_selon_typo_spatiale_travail.csv'
    results_in_french.to_csv(Path('../data/output/tables/FR/travail/' + file_name_fr),
                             encoding='iso-8859-1',
                             header=['Proportion avec place de stationnement gratuite',
                                     'Ecart type avec place de stationnement gratuite',
                                     'Proportion avec place de stationnement payante',
                                     'Ecart type avec place de stationnement payante',
                                     'Proportion sans place de stationnement',
                                     'Ecart type sans place de stationnement'])
    print(file_name_fr, 'saved in data/output/FR/travail')

    """ Results by aggregated categories (similarly as in the main report) """
    dict_aggregation = {0: 3,  # laendliche Gemeinde ohne staedtischen Charaketer
                        1: 1,  # Staedtischer Kernraum
                        2: 1,  # Staetischer Kernraum
                        3: 1,  # Staedtischer Kernraum
                        4: 2,  # Einflussgebiet staedtischer Kerne
                        5: 2,  # Einflussgebiet staedtischer Kerne
                        6: 1}  # Staedtischer Kernraum
    df_zp['A_staedt_char_2012_agg'] = df_zp['A_staedt_char_2012'].map(dict_aggregation)
    parking_work_free_by_work_loc_agg = df_zp.groupby('A_staedt_char_2012_agg').apply(get_weighted_average_and_std,
                                                                                'parking_spaces_for_cars_at_work_free',
                                                                                name_weight='weight_person')
    parking_work_paid_by_work_loc_agg = df_zp.groupby('A_staedt_char_2012_agg').apply(get_weighted_average_and_std,
                                                                                'parking_spaces_for_cars_at_work_paid',
                                                                                name_weight='weight_person')
    parking_work_0_by_work_loc_agg = df_zp.groupby('A_staedt_char_2012_agg').apply(get_weighted_average_and_std,
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
    differentiation_by_work_loc_agg.rename(index={1: 'Urban core area',
                                                  # in German: Staedtischer Kernraum
                                                  2: 'Area influenced by urban cores',
                                                  # in German: Einflussgebiet staedtischer Kerne
                                                  3: 'Area beyond urban core influence',
                                                  # in German: laendliche Gemeinde ohne staedtischen Charaketer
                                                  }, inplace=True)
    file_name = 'avail_parking_space_by_work_location_agg.csv'
    results_in_english = pd.concat([results_for_all_zp, differentiation_by_work_loc_agg])
    results_in_english.to_csv(Path('../data/output/tables/EN/work/' + file_name))
    print(file_name, 'saved in data/output/EN/work')

    # results in German
    results_in_german = results_in_english
    results_in_german.rename(index={'All households': 'alle Haushalte',
                                    'Urban core area': 'Staedtischer Kernraum',
                                    'Area influenced by urban cores': 'Einflussgebiet staedtischer Kerne',
                                    'Area beyond urban core influence':
                                        'laendliche Gemeinde ohne staedtischen Charakter'
                                    }, inplace=True)
    file_name_de = 'verfueg_autoparkplaetzen_nach_arbeitsort_raumtyp_agg.csv'
    results_in_german.to_csv(Path('../data/output/tables/DE/Arbeitsort/' + file_name_de),
                             header=['Anteil mit Gratisparkplatz', 'Standardabweichung mit Gratisparkplatz',
                                     'Anteil mit Bezahlparkplatz', 'Standardabweichung mit Bezahlparkplatz',
                                     'Anteil ohne Parkplatz', 'Standardabweichung ohne Parkplatz'])
    print(file_name_de, 'saved in data/output/DE/Arbeitsort')

    # Results in French
    results_in_french = results_in_german
    results_in_french.rename(index={'alle Haushalte': 'Tous les ménages',
                                    'Staedtischer Kernraum': 'Espace des centres urbains',
                                    'Einflussgebiet staedtischer Kerne': 'Espace sous influence des centres urbains',
                                    'laendliche Gemeinde ohne staedtischen Charakter':
                                        'Espace hors influence des centres urbains'
                                    }, inplace=True)
    file_name_fr = 'dispo_place_stationnement_selon_typo_spatiale_travail_agg.csv'
    results_in_french.to_csv(Path('../data/output/tables/FR/travail/' + file_name_fr),
                             encoding='iso-8859-1',
                             header=['Proportion avec place de stationnement gratuite',
                                     'Ecart type avec place de stationnement gratuite',
                                     'Proportion avec place de stationnement payante',
                                     'Ecart type avec place de stationnement payante',
                                     'Proportion sans place de stationnement',
                                     'Ecart type sans place de stationnement'])
    print(file_name_fr, 'saved in data/output/FR/travail')


def get_results_for_all_zp(df_zp):
    df_zp['parking_spaces_for_cars_at_work_free'] = \
        df_zp['parking_spaces_for_cars_at_work'].apply(lambda x: 1 if x == 1 else 0)
    df_zp['parking_spaces_for_cars_at_work_paid'] = \
        df_zp['parking_spaces_for_cars_at_work'].apply(lambda x: 1 if x == 2 else 0)
    df_zp['parking_spaces_for_cars_at_work_0'] = \
        df_zp['parking_spaces_for_cars_at_work'].apply(lambda x: 1 if x == 3 else 0)
    # Results for everyone
    weighted_avg_nb_parking_work_free, weighted_std_parking_work_free = \
        get_weighted_average_and_std(df_zp, 'parking_spaces_for_cars_at_work_free',
                                     name_weight = 'weight_person')
    weighted_avg_nb_parking_work_paid, weighted_std_parking_work_paid = \
        get_weighted_average_and_std(df_zp, 'parking_spaces_for_cars_at_work_paid',
                                     name_weight = 'weight_person')
    weighted_avg_nb_parking_work_0, weighted_std_parking_work_0 = \
        get_weighted_average_and_std(df_zp, 'parking_spaces_for_cars_at_work_0',
                                     name_weight = 'weight_person')
    # Group the results
    results_for_all_zp = pd.DataFrame({'Proportion with free parking space at work': weighted_avg_nb_parking_work_free,
                                       'Standard deviation with free parking space at work':
                                           weighted_std_parking_work_free,
                                       'Proportion with paid parking space at work': weighted_avg_nb_parking_work_paid,
                                       'Standard deviation with paid parking space at work':
                                           weighted_std_parking_work_paid,
                                       'Proportion without parking space at work': weighted_avg_nb_parking_work_0,
                                       'Standard deviation without parking space at work':
                                           weighted_std_parking_work_0
                                       }, index=['All households'])
    return results_for_all_zp


def get_data_person():
    """ Get the data about people that are needed and remove observations that are not valid """
    selected_columns = ['HHNR',
                        'f41300',
                        'WP',
                        'A_staedt_char_2012',
                        'A_AGGLO_GROESSE2012'
                        # 'f40900',
                        # 'f41100_01',
                        # 'f40800_01'
                        ]
    df_zp = get_zp(selected_columns=selected_columns)
    # Rename columns
    df_zp = df_zp.rename(columns={'f41300': 'parking_spaces_for_cars_at_work',
                                  'WP': 'weight_person',
                                  # 'f40900': 'full_time',
                                  # 'f41100_01': 'position_in_company',
                                  # 'f40800_01': 'employement_status'
                                  })
    # Removing observations with answers "don't know" and "no answer"
    df_zp = df_zp[df_zp['parking_spaces_for_cars_at_work'] != -98]  # no answer
    df_zp = df_zp[df_zp['parking_spaces_for_cars_at_work'] != -97]  # don't know
    df_zp = df_zp[df_zp['parking_spaces_for_cars_at_work'] != -99]  # younger than 18 or not part of this module or
                                                                       # not active (student and part time <50%)
    df_zp = df_zp[df_zp['A_staedt_char_2012'] != -97]  # no data, missing geodat about the typology of the agglo
    # df_zp = df_zp[df_zp['full_time'] != -97]  # don't know
    # df_zp = df_zp[df_zp['full_time'] != -98]  # no answer
    # df_zp = df_zp[df_zp['full_time'] != -99]  # not active
    # df_zp = df_zp[df_zp['position_in_company'] != -97]  # don't know
    # df_zp = df_zp[df_zp['position_in_company'] != -98]  # no answer
    # df_zp = df_zp[df_zp['employement_status'] != -99]  # no answer
    return df_zp