# Availability of parking spaces in Switzerland in 2015
This code computes the availability of parking spaces at home and at work by urban typology of the home and/or work location. 

This code uses data from the Mobility and Transport Microcensus (<a href="https://www.are.admin.ch/mtmc">MTMC</a>) 2015. The results are available as CSV-files.

## Results
The results are available in three languages: English, French and German.

### Results in English
The results in English are available in the folder "<a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/tree/master/data/output/tables/EN">EN</a>".

#### Results about parking spaces at home
The results in English about parking spaces at home are available in the folder "<a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/tree/master/data/output/tables/EN/home">home</a>" and show the number of parking spaces:
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/EN/home/avail_parking_space_by_agglo_size.csv">by population of the agglomeration of the place of living (in 5 categories of number of inhabitants + outside of agglomerations)</a>
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/EN/home/avail_parking_space_by_agglo_size_agg.csv">by population of the agglomeration of the place of living (aggregated in 3 categories of number of inhabitants + outside of agglomerations)</a>
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/EN/home/avail_parking_space_by_household_location.csv">by level of urbanisation of the place of living (in 7 categories)</a>
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/EN/home/avail_parking_space_by_household_location_agg.csv">by level of urbanisation of the place of living (aggregated in 3 categories)</a>
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/EN/home/avail_parking_space_by_nb_of_cars.csv">by number of cars in the household</a> (these results are similar to the figure G 2.3.1.1 in the main report of the MTMC 2015, page 15, see report <a href="https://www.are.admin.ch/dam/are/de/dokumente/verkehr/dokumente/mikrozensus/verkehrsverhalten-der-bevolkerung-ergebnisse-des-mikrozensus-mobilitat-und-verkehr-2015.pdf.download.pdf/Mikrozensus_Verkehrsverhalten%20der%20Bev%C3%B6lkerung%202015_de.pdf">in German</a> and <a href="https://www.are.admin.ch/dam/are/fr/dokumente/verkehr/dokumente/mikrozensus/verkehrsverhalten-der-bevolkerung-ergebnisse-des-mikrozensus-mobilitat-und-verkehr-2015.pdf.download.pdf/Mikrozensus_Verkehrsverhalten%20der%20Bev%C3%B6lkerung%202015_fr.pdf">in French</a>)

Statistical basis for these results: 56'874 households with valid information

#### Results about parking spaces at work
The results in English about parking spaces at work are available in the folder "<a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/tree/master/data/output/tables/EN/work">work</a>" and show if there are parking spaces, and if yes, if parking spaces are free or paid:
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/EN/work/avail_parking_space_by_agglo_size_work_loc.csv">by population of the agglomeration where the work place is located (in 5 categories of number of inhabitants + outside of agglomerations)</a>
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/EN/work/avail_parking_space_by_agglo_size_work_loc_agg.csv">by population of the agglomeration where the work place is located (aggregated in 3 categories of number of inhabitants + outside of agglomerations)</a>
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/EN/work/avail_parking_space_by_work_location.csv">by level of urbanisation of the work place (in 7 categories)</a>
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/EN/work/avail_parking_space_by_work_location_agg.csv">by level of urbanisation of the work place (aggregated in 3 categories)</a>

Statistical basis for these results: 8855 active persons, 18 years old or older, who answered the supplementary module about soft mobility and job occuation

#### Results about parking spaces at work by home location
These results show the availability of parking spaces at work (and if they exist, if they are free or paid) depending on the home location (size of agglomeration and level of urbanisation of the place of living). They also show cross tables of where people live and work, knowing if they have a parking space at work (and if it exists, if it is free or paid). All these results are in folder "<a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/tree/master/data/output/tables/EN/work_vs_home">work_vs_home</a>", specifically availability of parking spaces <b>at work</b>:
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/EN/work_vs_home/avail_parking_space_at_work_by_agglo_size_home_loc.csv">by population of the agglomeration <b>of the place of living</b> (in 5 categories of number of inhabitants + outside of agglomerations)</a>
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/EN/work_vs_home/avail_parking_space_at_work_by_agglo_size_home_loc_agg.csv">by population of the agglomeration <b>of the place of living</b> (aggregated in 3 categories of number of inhabitants + outside of agglomerations)</a>
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/EN/work_vs_home/avail_parking_space_at_work_by_home_location.csv">by level of urbanisation <b>of the place of living</b> (in 7 categories)</a>
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/EN/work_vs_home/avail_parking_space_at_work_by_home_location_agg.csv">by level of urbanisation <b>of the place of living</b> (aggregated in 3 categories)</a>

and the proportion of people living and working in places with different levels of urbanisation (aggregated in 3 categories):
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/EN/work_vs_home/no_parking_space_at_work_by_home_work_location_agg.csv">among people without parking space at work</a>, 
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/EN/work_vs_home/free_parking_space_at_work_by_home_work_location_agg.csv">among people with free parking spaces at work</a> and 
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/EN/work_vs_home/paid_parking_space_at_work_by_home_work_location_agg.csv">among people with paid parking spaces at work</a>.

Statistical basis for these results: 8855 active persons, 18 years old or older, who answered the supplementary module about soft mobility and job occuation

### Résultats en français
Les résultats en français sont disponibles dans le dossier
"<a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/tree/master/data/output/tables/FR">FR</a>".

#### Disponibilité de places de stationnement au domicile
Les résultats en français concernant la disponibilité de places de stationnement au domicile sont disponibles dans le
 dossier
 "<a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/tree/master/data/output/tables/FR/domicile">domicile</a>"
 et présentent le nombre de places de parking ou de garage:
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/FR/domicile/dispo_place_stationnement_selon_pop_agglo.csv">selon la population de l'agglomération du lieu de domicile (en 5 catégories de nombre d'habitants + 1 catégorie "hors agglomérations")</a>
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/FR/domicile/dispo_place_stationnement_selon_pop_agglo_agg.csv">selon la population de l'agglomération du lieu de domicile (agrégé en 3 catégories de nombre d'habitants + 1 catégorie "hors agglomération")</a>
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/FR/domicile/dispo_place_stationnement_selon_typo_spatiale_menage.csv">selon le degré d'urbanisation du lieu de domicile (en 7 catégories)</a>
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/FR/domicile/dispo_place_stationnement_selon_typo_spatiale_menage_agg.csv">selon le degré d'urbanisation du lieu de domicile (agrégé en 3 catégories)</a>
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/FR/domicile/dispo_place_stationnement_selon_nb_voiture_dans_menage.csv">selon le nombre de voitures dans le ménage</a> (ces résultats sont identiques à ceux présentés dans le graphique
G 2.3.1.1 du <a href="https://www.are.admin.ch/dam/are/fr/dokumente/verkehr/dokumente/mikrozensus/verkehrsverhalten-der-bevolkerung-ergebnisse-des-mikrozensus-mobilitat-und-verkehr-2015.pdf.download.pdf/Mikrozensus_Verkehrsverhalten%20der%20Bev%C3%B6lkerung%202015_fr.pdf">
rapport principal du MRMT 2015</a>, page 15)

Base pour le calcul de ces résultats : 56'874 ménages avec indication valable

#### Disponibilité de place de stationnement au lieu de travail
Les résultats en français concernant la disponibilité de place de stationnement au lieu de travail sont disponibles
dans le dossier
"<a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/tree/master/data/output/tables/FR/travail">travail</a>"
et présentent si une place de stationnement est disponible, et si oui, si elle est gratuite ou payante:
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/FR/travail/dispo_place_stationnement_selon_pop_agglo_travail.csv">selon la population de l'agglomération du lieu de travail (en 5 catégories de nombre d'habitants + 1 catégorie "hors agglomérations")</a>
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/FR/travail/dispo_place_stationnement_selon_pop_agglo_travail_agg.csv">selon la population de l'agglomération du lieu de travail (agrégé en 3 catégories de nombre d'habitants + 1 catégorie "hors agglomération")</a>
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/FR/travail/dispo_place_stationnement_selon_typo_spatiale_travail.csv">selon le degré d'urbanisation du lieu de travail (en 7 catégories)</a>
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/FR/travail/dispo_place_stationnement_selon_typo_spatiale_travail_agg.csv">selon le degré d'urbanisation du lieu de travail (agrégé en 3 catégories)</a>

Base pour le calcul de ces résultats : 8855 personnes actives occupées de 18 ans ou plus interrogées dans le module supplémentaire "Mobilité douce et profession"

#### Disponibilité de places de stationnement au lieu de travail selon le lieu de domicile
Ces résultats présentent la disponibilité de places de stationnement au lieu de travail (et si elles existent, si elles sont payantes ou gratuites) en fonction du lieu de domicile (taille de l'agglomération et niveau d'urbanisation du lieu de domicile). Ils présentent aussi trois tableaux croisés du niveau d'urbanisation des lieux de domicile et de travail des personnes ayant une place de stationnement disponible au travail. Tous ces résultats se trouvent dans le dossier "<a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/tree/master/data/output/tables/FR/travail_vs_domicile">travail_vs_domicile</a>". On y trouve en particulier la disponibilité de place de stationnement <b>au lieu de travail</b>:
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/FR/travail_vs_domicile/dispo_place_stationnement_au_travail_selon_pop_agglo_domicile.csv">selon la population de l'agglomération du <b>lieu de domicile</b> (en 5 catégories de nombre d'habitants + 1 catégorie "hors agglomération")</a>
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/FR/travail_vs_domicile/dispo_place_stationnement_au_travail_selon_pop_agglo_domicile_agg.csv">selon la population de l'agglomération du <b>lieu de domicile</b> (agrégé en 3 catégories de nombre d'habitants + 1 catégorie "hors agglomération")</a>
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/FR/travail_vs_domicile/dispo_place_stationnement_au_travail_selon_typo_spatiale_domicile.csv">selon le degré d'urbanisation du <b>lieu de domicile</b> (en 7 catégories)</a>
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/FR/travail_vs_domicile/dispo_place_stationnement_au_travail_selon_typo_spatiale_domicile_agg.csv">selon le degré d'urbanisation du <b>lieu de domicile</b> (agrégé en 3 catégories)</a>

et la proportion de personnes vivant et travaillant dans des lieux de différentes degrés d'urbanisation (agrégé en 3 catégories) parmi : 
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/FR/travail_vs_domicile/pas_de_place_stationnement_au_travail_selon_typo_spatiale_domicile_travail_agg.csv">les personnes sans place de stationnement au lieu de travail</a>, 
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/FR/travail_vs_domicile/place_stationnement_gratuite_au_travail_selon_typo_spatiale_domicile_travail_agg.csv">les personnes avec une place de stationnement gratuite</a> et
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/FR/travail_vs_domicile/place_stationnement_payante_au_travail_selon_typo_spatiale_domicile_travail_agg.csv">les personnes avec une place de stationnement payante</a>.

Base pour le calcul de ces résultats : 8855 personnes actives occupées de 18 ans ou plus interrogées dans le module supplémentaire "Mobilité douce et profession"

### Ergebnisse auf Deutsch
Die Ergebnisse auf Deutsch finden sich im Ordner "<a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/tree/master/data/output/tables/DE">DE</a>".

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for reproducing the result and understanding how it has been generated.

### Prerequisites

To run the code itself, you need python 3, pandas and numpy.

For it to produce the results, you also need the raw data of the Transport and Mobility Microcensus 2015, not included on GitHub. These data are individual data and therefore not open. You can however get them by filling in this form in <a href="https://www.are.admin.ch/are/de/home/verkehr-und-infrastruktur/grundlagen-und-daten/mzmv/datenzugang.html">German</a>, <a href="https://www.are.admin.ch/are/fr/home/mobilite/bases-et-donnees/mrmt/accesauxdonnees.html">French</a> or <a href="https://www.are.admin.ch/are/it/home/mobilita/basi-e-dati/mcmt/accessoaidati.html">Italian</a>. The cost of the data is available in the document "<a href="https://www.are.admin.ch/are/de/home/medien-und-publikationen/publikationen/grundlagen/mikrozensus-mobilitat-und-verkehr-2015-mogliche-zusatzauswertung.html">Mikrozensus Mobilität und Verkehr 2015: Mögliche Zusatzauswertungen</a>"/"<a href="https://www.are.admin.ch/are/fr/home/media-et-publications/publications/bases/mikrozensus-mobilitat-und-verkehr-2015-mogliche-zusatzauswertung.html">Microrecensement mobilité et transports 2015: Analyses supplémentaires possibles</a>".

### Run the code

Please copy the files <em>houshalte.csv</em> and <em>zielpersonen.csv</em> from 2015 that you receive from the Swiss Federal Statistical Office (FSO) in the folders "<a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/tree/master/data/input">data/input</a>". Then run <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/src/run_availability_of_parking.py">run_availability_of_parking.py</a>. 

DO NOT commit or share in any way these two CSV-files! These are personal data.
