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

Statistical basis for these results: 8855 active persons, 18 years old or older, who answered the odule about soft mobility and job occuation

#### Results about parking spaces at work by home location
These results show the availability of parking spaces at work (and if they exist, if they are free or paid) depending on the home location (size of agglomeration and level of urbanisation of the place of living). They also show a cross table showing where people without a parking space at work live and work. All these results are in folder "<a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/tree/master/data/output/tables/EN/work_vs_home">work_vs_home</a>", specifically availability of parking spaces <b>at work</b>:
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/EN/work_vs_home/avail_parking_space_at_work_by_agglo_size_home_loc.csv">by population of the agglomeration <b>of the place of living</b> (in 5 categories of number of inhabitants + outside of agglomerations)</a>
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/EN/work_vs_home/avail_parking_space_at_work_by_agglo_size_home_loc_agg.csv">by population of the agglomeration <b>of the place of living</b> (aggregated in 3 categories of number of inhabitants + outside of agglomerations)</a>
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/EN/work_vs_home/avail_parking_space_at_work_by_home_location.csv">by level of urbanisation <b>of the place of living</b> (in 7 categories)</a>
- <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/EN/work_vs_home/avail_parking_space_at_work_by_home_location_agg.csv">by level of urbanisation <b>of the place of living</b> (aggregated in 3 categories)</a>

and <a href="https://github.com/antonindanalet/availability-of-parking-in-Switzerland-in-2015/blob/master/data/output/tables/EN/work_vs_home/no_parking_space_at_work_by_home_work_location_agg.csv">the proportion of people living and working in places with different levels of urbanisation (aggregated in 3 categories) among people without parking space at work</a>.

Statistical basis for these results: 8855 active persons, 18 years old or older, who answered the odule about soft mobility and job occuation
