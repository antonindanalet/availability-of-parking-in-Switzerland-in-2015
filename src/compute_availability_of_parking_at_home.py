from utils_mtmc.get_mtmc_files import *
from utils_mtmc.get_weighted_average_and_std import *


def compute_availability_of_parking_space_by_agglo_size(df_hh, results_for_all_hh):
    size_variable = 'W_AGGLO_GROESSE2012'
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
    dict_labels_de2fr = {'Alle Haushalte': '',
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
    file_name_en = 'availability_of_parking_space_by_agglo_size.csv'
    file_name_de = 'verfuegbarkeit_von_autoparkplaetzen_nach_agglo_groesse.csv'
    file_name_fr = 'dispo_de_place_stationnement_selon_pop_agglo.csv'
    compute_av_parking_for_one_size_variable(df_hh, results_for_all_hh, size_variable, dict_variable_labels,
                                             dict_labels_en2de, dict_labels_de2fr,
                                             file_name_en, file_name_de, file_name_fr)
    """ Results for larger groups of sizes for the agglomerations """
    dict_aggregation = {0: 0,
                        1: 1,
                        2: 1,
                        3: 2,
                        4: 2,
                        5: 3}
    size_variable_agg = 'W_AGGLO_GROESSE2012_agg'
    df_hh[size_variable_agg] = df_hh[size_variable].map(dict_aggregation)
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
    file_name_en_agg = 'availability_of_parking_space_by_agglo_size_agg.csv'
    file_name_de_agg = 'verfuegbarkeit_von_autoparkplaetzen_nach_agglo_groesse_agg.csv'
    file_name_fr_agg = 'dispo_de_place_stationnement_selon_pop_agglo_agg.csv'
    compute_av_parking_for_one_size_variable(df_hh, results_for_all_hh, size_variable_agg, dict_variable_labels_agg,
                                             dict_labels_en2de_agg, dict_labels_de2fr_agg,
                                             file_name_en_agg, file_name_de_agg, file_name_fr_agg)


def compute_av_parking_for_one_size_variable(df_hh, results_for_all_hh, size_variable, dict_variable_labels,
                                             dict_labels_en2de, dict_labels_de2fr,
                                             file_name_en, file_name_de,file_name_fr):
    """ Results by size of the agglomeration the household is located in """
    nb_parking_home_0_by_agglo_size = df_hh.groupby(size_variable).apply(get_weighted_average_and_std,
                                                                         'nb_parking_spaces_for_cars_at_home_0',
                                                                         name_weight='weight_household')
    nb_parking_home_1_by_agglo_size = df_hh.groupby(size_variable).apply(get_weighted_average_and_std,
                                                                         'nb_parking_spaces_for_cars_at_home_1',
                                                                         name_weight='weight_household')
    nb_parking_home_2_by_agglo_size = df_hh.groupby(size_variable).apply(get_weighted_average_and_std,
                                                                         'nb_parking_spaces_for_cars_at_home_2',
                                                                         name_weight='weight_household')
    nb_parking_home_3_by_agglo_size = df_hh.groupby(size_variable).apply(get_weighted_average_and_std,
                                                                         'nb_parking_spaces_for_cars_at_home_3+',
                                                                         name_weight='weight_household')
    # Generate a CSV-file with the results
    differentiation_by_agglo_size = pd.concat([nb_parking_home_0_by_agglo_size,
                                               nb_parking_home_1_by_agglo_size,
                                               nb_parking_home_2_by_agglo_size,
                                               nb_parking_home_3_by_agglo_size], axis=1)
    differentiation_by_agglo_size.columns = ['Proportion without parking space at home',
                                             'Standard deviation without parking space at home',
                                             'Proportion with 1 parking space at home',
                                             'Standard deviation with 1 parking space at home',
                                             'Proportion with 2 parking spaces at home',
                                             'Standard deviation with 2 parking spaces at home',
                                             'Proportion with 3 and more parking spaces at home',
                                             'Standard deviation with 3 and more parking spaces at home']
    differentiation_by_agglo_size.rename(index=dict_variable_labels, inplace=True)
    results_in_english = pd.concat([results_for_all_hh, differentiation_by_agglo_size])
    results_in_english.to_csv(Path('../data/output/tables/EN/home/' + file_name_en))
    print(file_name_en, 'saved in data/output/EN')
    # Save results in German
    results_in_german = results_in_english
    results_in_german.rename(index=dict_labels_en2de, inplace=True)
    results_in_german.to_csv(Path('../data/output/tables/DE/zuHause/' + file_name_de),
                             header=['Anteil ohne Parkplatz', 'Standardabweichung ohne Parkplatz',
                                     'Anteil mit 1 Parkplatz', 'Standardabweichung mit 1 Parkplatz',
                                     'Anteil mit 2 Parkplaetzen', 'Standardabweichung mit 2 Parkplaetzen',
                                     'Anteil mit 3 Parkplaetzen und mehr',
                                     'Standardabweichung mit 3 Parkplaetzen und mehr'])
    print(file_name_de, 'saved in data/output/DE')
    # Save results in French
    results_in_french = results_in_german
    results_in_french.rename(index=dict_labels_de2fr, inplace=True)
    results_in_french.to_csv(Path('../data/output/tables/FR/domicile/' + file_name_fr),
                             encoding='iso-8859-1',
                             header=['Proportion sans place de stationnement', 'Ecart type sans place de stationnement',
                                     'Proportion avec 1 place de stationnement',
                                     'Ecart type avec 1 place de stationnement',
                                     'Proportion avec 2 place de stationnement',
                                     'Ecart type avec 2 place de stationnement',
                                     'Proportion avec 3 place de stationnement ou plus',
                                     'Ecart type avec 3 place de stationnement ou plus'])
    print(file_name_fr, 'saved in data/output/FR')


def compute_availability_of_parking_space_by_type_hh(df_hh, results_for_all_hh):
    """ Results by type of place of living (full categories) """
    nb_parking_home_0_by_hh_loc = df_hh.groupby('W_staedt_char_2012').apply(get_weighted_average_and_std,
                                                                            'nb_parking_spaces_for_cars_at_home_0',
                                                                            name_weight = 'weight_household')
    nb_parking_home_1_by_hh_loc = df_hh.groupby('W_staedt_char_2012').apply(get_weighted_average_and_std,
                                                                            'nb_parking_spaces_for_cars_at_home_1',
                                                                            name_weight = 'weight_household')
    nb_parking_home_2_by_hh_loc = df_hh.groupby('W_staedt_char_2012').apply(get_weighted_average_and_std,
                                                                            'nb_parking_spaces_for_cars_at_home_2',
                                                                            name_weight = 'weight_household')
    nb_parking_home_3_by_hh_loc = df_hh.groupby('W_staedt_char_2012').apply(get_weighted_average_and_std,
                                                                            'nb_parking_spaces_for_cars_at_home_3+',
                                                                            name_weight = 'weight_household')
    # Generate a CSV-file with the results
    differentiation_by_hh_loc = pd.concat([nb_parking_home_0_by_hh_loc,
                                           nb_parking_home_1_by_hh_loc,
                                           nb_parking_home_2_by_hh_loc,
                                           nb_parking_home_3_by_hh_loc], axis=1)
    differentiation_by_hh_loc.columns = ['Proportion without parking space at home',
                                         'Standard deviation without parking space at home',
                                         'Proportion with 1 parking space at home',
                                         'Standard deviation with 1 parking space at home',
                                         'Proportion with 2 parking spaces at home',
                                         'Standard deviation with 2 parking spaces at home',
                                         'Proportion with 3 and more parking spaces at home',
                                         'Standard deviation with 3 and more parking spaces at home']
    differentiation_by_hh_loc.rename(index={0: 'Rural municipalities without urban character',
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
    file_name_en = 'availability_of_parking_space_by_household_location.csv'
    results_in_english = pd.concat([results_for_all_hh, differentiation_by_hh_loc])
    results_in_english.to_csv(Path('../data/output/tables/EN/home/' + file_name_en))
    print(file_name_en, 'saved in data/output/EN')
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
    file_name_de = 'verfuegbarkeit_von_autoparkplaetzen_nach_haushalt_raumtyp.csv'
    results_in_german.to_csv(Path('../data/output/tables/DE/zuHause/' + file_name_de),
                              header=['Anteil ohne Parkplatz', 'Standardabweichung ohne Parkplatz',
                                      'Anteil mit 1 Parkplatz', 'Standardabweichung mit 1 Parkplatz',
                                      'Anteil mit 2 Parkplaetzen', 'Standardabweichung mit 2 Parkplaetzen',
                                      'Anteil mit 3 Parkplaetzen und mehr',
                                      'Standardabweichung mit 3 Parkplaetzen und mehr'])
    print(file_name_de, 'saved in data/output/DE')
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
    file_name_fr = 'dispo_de_place_stationnement_selon_typo_spatiale_menage.csv'
    results_in_french.to_csv(Path('../data/output/tables/FR/domicile/' + file_name_fr),
                             encoding='iso-8859-1',
                             header=['Proportion sans place de stationnement', 'Ecart type sans place de stationnement',
                                     'Proportion avec 1 place de stationnement',
                                     'Ecart type avec 1 place de stationnement',
                                     'Proportion avec 2 place de stationnement',
                                     'Ecart type avec 2 place de stationnement',
                                     'Proportion avec 3 place de stationnement ou plus',
                                     'Ecart type avec 3 place de stationnement ou plus'])
    print(file_name_fr, 'saved in data/output/FR')

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
                                                                                'nb_parking_spaces_for_cars_at_home_0',
                                                                                name_weight = 'weight_household')
    nb_parking_home_1_by_hh_loc = df_hh.groupby('W_staedt_char_2012_agg').apply(get_weighted_average_and_std,
                                                                                'nb_parking_spaces_for_cars_at_home_1',
                                                                                name_weight = 'weight_household')
    nb_parking_home_2_by_hh_loc = df_hh.groupby('W_staedt_char_2012_agg').apply(get_weighted_average_and_std,
                                                                                'nb_parking_spaces_for_cars_at_home_2',
                                                                                name_weight = 'weight_household')
    nb_parking_home_3_by_hh_loc = df_hh.groupby('W_staedt_char_2012_agg').apply(get_weighted_average_and_std,
                                                                                'nb_parking_spaces_for_cars_at_home_3+',
                                                                                name_weight = 'weight_household')
    # Generate a CSV-file with the results
    differentiation_by_hh_loc = pd.concat([nb_parking_home_0_by_hh_loc,
                                           nb_parking_home_1_by_hh_loc,
                                           nb_parking_home_2_by_hh_loc,
                                           nb_parking_home_3_by_hh_loc], axis=1)
    differentiation_by_hh_loc.columns = ['Proportion without parking space at home',
                                         'Standard deviation without parking space at home',
                                         'Proportion with 1 parking space at home',
                                         'Standard deviation with 1 parking space at home',
                                         'Proportion with 2 parking spaces at home',
                                         'Standard deviation with 2 parking spaces at home',
                                         'Proportion with 3 and more parking spaces at home',
                                         'Standard deviation with 3 and more parking spaces at home']
    differentiation_by_hh_loc.rename(index={1: 'Urban core area',
                                            # in German: Staedtischer Kernraum
                                            2: 'Area influenced by urban cores',
                                            # in German: Einflussgebiet staedtischer Kerne
                                            3: 'Area beyond urban core influence',
                                            # in German: laendliche Gemeinde ohne staedtischen Charaketer
                                            }, inplace=True)
    file_name = 'availability_of_parking_space_by_household_location_agg.csv'
    results_in_english = pd.concat([results_for_all_hh, differentiation_by_hh_loc])
    results_in_english.to_csv(Path('../data/output/tables/EN/home/' + file_name))
    print(file_name, 'saved in data/output/EN')

    # results in German
    results_in_german = results_in_english
    results_in_german.rename(index={'All households': 'alle Haushalte',
                                    'Urban core area': 'Staedtischer Kernraum',
                                    'Area influenced by urban cores': 'Einflussgebiet staedtischer Kerne',
                                    'Area beyond urban core influence':
                                        'laendliche Gemeinde ohne staedtischen Charakter'
                                    }, inplace=True)
    file_name_de = 'verfuegbarkeit_von_autoparkplaetzen_nach_haushalt_raumtyp_agg.csv'
    results_in_german.to_csv(Path('../data/output/tables/DE/zuHause/' + file_name_de),
                             header=['Anteil ohne Parkplatz', 'Standardabweichung ohne Parkplatz',
                                     'Anteil mit 1 Parkplatz', 'Standardabweichung mit 1 Parkplatz',
                                     'Anteil mit 2 Parkplaetzen', 'Standardabweichung mit 2 Parkplaetzen',
                                     'Anteil mit 3 Parkplaetzen und mehr',
                                     'Standardabweichung mit 3 Parkplaetzen und mehr'])
    print(file_name_de, 'saved in data/output/DE')

    # Results in French
    results_in_french = results_in_german
    results_in_french.rename(index={'alle Haushalte': 'Tous les ménages',
                                    'Staedtischer Kernraum': 'Espace des centres urbains',
                                    'Einflussgebiet staedtischer Kerne': 'Espace sous influence des centres urbains',
                                    'laendliche Gemeinde ohne staedtischen Charakter':
                                        'Espace hors influence des centres urbains'
                                    }, inplace=True)
    file_name_fr = 'dispo_de_place_stationnement_selon_typo_spatiale_menage_agg.csv'
    results_in_french.to_csv(Path('../data/output/tables/FR/domicile/' + file_name_fr),
                             encoding='iso-8859-1',
                             header=['Proportion sans place de stationnement', 'Ecart type sans place de stationnement',
                                     'Proportion avec 1 place de stationnement',
                                     'Ecart type avec 1 place de stationnement',
                                     'Proportion avec 2 place de stationnement',
                                     'Ecart type avec 2 place de stationnement',
                                     'Proportion avec 3 place de stationnement ou plus',
                                     'Ecart type avec 3 place de stationnement ou plus'])
    print(file_name_fr, 'saved in data/output/FR')


def get_data_household():
    """ Get the data about households that are needed and remove observations that are not valid """
    selected_columns = ['f31100',
                        'WM',
                        'f30100',
                        'W_staedt_char_2012',
                        'W_AGGLO_GROESSE2012']
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
        get_weighted_average_and_std(df_hh, 'nb_parking_spaces_for_cars_at_home_0', name_weight='weight_household')
    weighted_avg_nb_parking_home_1, weigthed_std_parking_home_1 = \
        get_weighted_average_and_std(df_hh, 'nb_parking_spaces_for_cars_at_home_1', name_weight='weight_household')
    weighted_avg_nb_parking_home_2, weigthed_std_parking_home_2 = \
        get_weighted_average_and_std(df_hh, 'nb_parking_spaces_for_cars_at_home_2', name_weight='weight_household')
    weighted_avg_nb_parking_home_3, weigthed_std_parking_home_3 = \
        get_weighted_average_and_std(df_hh, 'nb_parking_spaces_for_cars_at_home_3+', name_weight='weight_household')
    # Group the results
    results_for_all_hh = pd.DataFrame({'Proportion without parking space at home': weighted_avg_nb_parking_home_0,
                                       'Standard deviation without parking space at home': weigthed_std_parking_home_0,
                                       'Proportion with 1 parking space at home': weighted_avg_nb_parking_home_1,
                                       'Standard deviation with 1 parking space at home': weigthed_std_parking_home_1,
                                       'Proportion with 2 parking spaces at home': weighted_avg_nb_parking_home_2,
                                       'Standard deviation with 2 parking spaces at home': weigthed_std_parking_home_2,
                                       'Proportion with 3 and more parking spaces at home': weighted_avg_nb_parking_home_3,
                                       'Standard deviation with 3 and more parking spaces at home': weigthed_std_parking_home_3,
                                       }, index=['All households'])
    return results_for_all_hh


def compute_availability_of_parking_space_by_nb_of_cars(df_hh, results_for_all_hh):
    """ Reproduce results from the main report (G 2.3.1.1) """
    # Replace all values higher than 3 by 3 in variable nb_cars... --> becomes category "3+ cars owned by the hh"
    df_hh['nb_cars_in_household'] = df_hh['nb_cars_in_household'].apply(lambda x: x if x <= 3 else 3)
    # Results depending on number of cars in the household
    nb_parking_home_0_by_nb_cars = df_hh.groupby('nb_cars_in_household').apply(get_weighted_average_and_std,
                                                                               'nb_parking_spaces_for_cars_at_home_0',
                                                                               name_weight='weight_household')
    nb_parking_home_1_by_nb_cars = df_hh.groupby('nb_cars_in_household').apply(get_weighted_average_and_std,
                                                                               'nb_parking_spaces_for_cars_at_home_1',
                                                                               name_weight='weight_household')
    nb_parking_home_2_by_nb_cars = df_hh.groupby('nb_cars_in_household').apply(get_weighted_average_and_std,
                                                                               'nb_parking_spaces_for_cars_at_home_2',
                                                                               name_weight='weight_household')
    nb_parking_home_3_by_nb_cars = df_hh.groupby('nb_cars_in_household').apply(get_weighted_average_and_std,
                                                                               'nb_parking_spaces_for_cars_at_home_3+',
                                                                               name_weight='weight_household')
    # Generate a CSV-file with the results
    differentiation_by_nb_cars = pd.concat([nb_parking_home_0_by_nb_cars,
                                            nb_parking_home_1_by_nb_cars,
                                            nb_parking_home_2_by_nb_cars,
                                            nb_parking_home_3_by_nb_cars], axis = 1)
    differentiation_by_nb_cars.columns = ['Proportion without parking space at home',
                                    'Standard deviation without parking space at home',
                                    'Proportion with 1 parking space at home',
                                    'Standard deviation with 1 parking space at home',
                                    'Proportion with 2 parking spaces at home',
                                    'Standard deviation with 2 parking spaces at home',
                                    'Proportion with 3 and more parking spaces at home',
                                    'Standard deviation with 3 and more parking spaces at home']
    differentiation_by_nb_cars.rename(index={0: 'No car in the household',
                                             1: '1 car in the household',
                                             2: '2 cars in the household',
                                             3: '3 and more cars in the household'}, inplace=True)
    file_name = 'availability_of_parking_space_by_nb_of_cars.csv'
    results_in_english = pd.concat([results_for_all_hh, differentiation_by_nb_cars])
    results_in_english.to_csv(Path('../data/output/tables/EN/home/' + file_name))
    print(file_name, 'saved in data/output/EN')

    # Results in German
    results_in_german = results_in_english
    results_in_german.rename(index={'All households': 'alle Haushalte',
                                    'No car in the household': 'Haushalte ohne Auto',
                                    '1 car in the household': 'Haushalte mit 1 Auto',
                                    '2 cars in the household': 'Haushalte mit 2 Autos',
                                    '3 and more cars in the household': 'Haushalte mit 3 Autos und mehr'
                                    }, inplace=True)
    file_name_de = 'verfuegbarkeit_von_autoparkplaetzen_nach_anzahl_autos_im_haushalt.csv'
    results_in_german.to_csv(Path('../data/output/tables/DE/zuHause/' + file_name_de),
                             header=['Anteil ohne Parkplatz', 'Standardabweichung ohne Parkplatz',
                                     'Anteil mit 1 Parkplatz', 'Standardabweichung mit 1 Parkplatz',
                                     'Anteil mit 2 Parkplaetzen', 'Standardabweichung mit 2 Parkplaetzen',
                                     'Anteil mit 3 Parkplaetzen und mehr',
                                     'Standardabweichung mit 3 Parkplaetzen und mehr'])
    print(file_name_de, 'saved in data/output/DE')

    # Results in French
    results_in_french = results_in_german
    results_in_french.rename(index={'alle Haushalte': 'Tous les ménages',
                                    'Haushalte ohne Auto': 'Ménages sans voiture',
                                    'Haushalte mit 1 Auto': 'Ménages avec 1 voiture',
                                    'Haushalte mit 2 Autos': 'Ménages avec 2 voitures',
                                    'Haushalte mit 3 Autos und mehr': 'Ménages avec 3 voitures et plus'
                                    }, inplace=True)
    file_name_fr = 'dispo_de_place_stationnement_selon_nb_voiture_dans_menage.csv'
    results_in_french.to_csv(Path('../data/output/tables/FR/domicile/' + file_name_fr),
                             encoding='iso-8859-1',
                             header=['Proportion sans place de stationnement', 'Ecart type sans place de stationnement',
                                     'Proportion avec 1 place de stationnement',
                                     'Ecart type avec 1 place de stationnement',
                                     'Proportion avec 2 place de stationnement',
                                     'Ecart type avec 2 place de stationnement',
                                     'Proportion avec 3 place de stationnement ou plus',
                                     'Ecart type avec 3 place de stationnement ou plus'])
    print(file_name_fr, 'saved in data/output/FR')