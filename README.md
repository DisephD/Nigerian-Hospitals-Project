# Nigerian-Hospitals-Project

## Overview
This project provides a detailed analysis of the distribution of hospitals across Nigeria. It includes visualisation of hospital locations, calculation of geographical distances, and insights into healthcare access across the different states and regions of the country. The project aims to assist in identifying areas with healthcare needs and promote data-driven decision-making for healthcare infrastructural development.

## Table of Contents
1. Project Description
2. My Motivation
3. Features
4. Technologies Used
5. Data Source
6. Structure
7. Images
8. Contact

## Project Description
In this project, I performed a geo-spatial analysis of healthcare facilities across Nigeria. The main objective was to visualize the distribution of hospitals, compare the number of hospitals to population density, and explore potential gaps in healthcare access.
You can explore the Tableau Dashboard for this project [here](https://https://public.tableau.com/app/profile/diseph.igoni/viz/Geo-spatialAnalysisNigerianHospitals_/DashboardHome?publish=yes)

## My Motivation
### Why I built it:
Healthcare is a critical sector, especially in developing nations like Nigeria. I was motivated to build this project to better understand the distribution of healthcare infrastructure across the country and identify areas where more healthcare services might be needed. The project helps identify regions with limited access to hospitals and provides insights that can assist policymakers in planning future healthcare infrastructure in Nigeria.

### What I learnt:
Working on this project taught me valuable lessons in handling geo-spatial data, as well as large data. 
I improved my skills in using Python libraries like Geopandas, and gained a deeper understanding of the healthcare challenges in Nigeria.

## Features
* #### Geo-spatial visualizations:
    Interactive maps that display hospitals across Nigeria, categorized by state and type.
* #### Hospital Clustering: 
    Insights into the concentration of hospitals and areas that are underserved.
* #### Metrics:
    Information like average hospitals, distance ratios, trends in hospital naming.

## Technologies Used
* Pandas: For data access, manipulation and handling.
* Geopandas: For geo-spatial data manipulation.
* Folium: For interactive map visualization.
* Tableau: For creating the dashboard and respective visualizations.
* Jupyter Notebook: For code execution.

## Data Source
The data for this project is sourced from:
The [Humanitarian Data Exchange](https://https://data.humdata.org/dataset/nigeria-hospitals-and-clinics-with-registration-status-and-location) platform, which was provided by the Nigeria Federal Ministry of Health.

## Structure
1. The [assets](/assets) folder contains the dashboard images for this Readme file.
2. The [data](/data) folder contains the source and modified data files used in this project.
2. The file [dashboard](/dashboard.txt) contains the link to the final tableau report.
3. The folder [scripts](/scripts) houses two python files and one folder. 
* The first file [data_cleaning](/scripts/data_cleaning.py) contains all the steps used to process and clean the data.
* The second file contains additional visualizations used to explore the data which were not included in the final report. 
* The nested folder [distance_calc_trials](/scripts/distance_calc_trials) contains the various methods used to arrive at a most optimised calculation of geographical distances.
4. The file [map.html](/map.html) contains a folium map which renders to the tableau dashboard.

## Images
![dashboard_image](/assets/image-1.png)
![dashboard_image](/assets/image-2.png)
![dashboard_image](/assets/image-3.png)

## Contact
For any inquiries, feedback, or issues, please reach out to me via disephdumigoni@gmail.com, with the subject "Nigerian Hospitals Project".
