# Exploring US Mining Safety Data
CME583 Final Group Project - Group MinCoin

MinCoin Project Description:
This project will conduct an exploratory data analysis (EDA) of U.S. mining injury datasets, from Mining Safety and Health Administration (MSHA) and National Institute for Occupational Safety and Health (NIOSH). Two different sources of of datasets were analyzed due to the NIOSH data consists of fatality data from 1839-2010 and MSHA consists of fatality and accident data from 2010-2024. Accessing and analyzing the multiple sources ensure that historic data can be compared to present day data. These datasets will be reviewed and analyzed to determine the impact of various factors such as policy changes and technology advancements. Key regulatory milestones, such as the Federal Mine Safety and Health Act, and advancements in mining technology will be analyzed to assess their impact on injury rates. These findings aim to identify gaps in current practices and guide future technological and regulatory improvements to reduce injuries in the mining sector. 


# Overview of Files
1. MinCoin MSHA Data Sorting(Non-Metal,Metal).ipynb : This code looks at all of the MSHA fatality reports from 2010 to 2024 and analyzes trends in fatalaties.  
   - extracted_data.csv : This is the extracted dataframe as a result of the Fatalatiy Report PDFs from the MSHA database ran
2. Mining disasters-fatilities.csv
3. Mining fatilities bots.ipynb: Mine Fatalities data is downloaded from NIOSH, and using mine name, city, and state, coordinate is extracted from wikipedia. For the one that did not have coordinates, openstreemap API is used to extract coordinates using city and state. Various graphs are demonstrated to conduct geospacial analysis and show correlation of safety regulations and improvememnt of mining technology. 
4. Tesseract Download.html
5. geospatial_analysis.ipynb : Reads the accident dataset from MSHA and generates a choropleth map of accident count throughout the United States along with multiple graphs to show the relationship between accident frequency, production, operator experience, etc. 
6. state_and_city_fatalities_map_with_spaced_legend.html: Fatality map generated from Mining fatilities bots.ipynb.
7. updated_test_data_with_coordinates.csv: dataframe that includes coordinates that are web scraped. 
8. us_accident_density_map.html : Accident map generated from geospatial_analysis.ipynb saved as html. 
9. webscraping_analysis.ipynb

# Link to Medium Article
Exploring U.S Mining Safety Data: https://medium.com/@komalmann98/exploring-u-s-mining-safety-data-ffa8df361138

# Workflow for MSHA Data Analysis
![image](https://github.com/user-attachments/assets/8a955653-b3a1-43cc-bab2-2359d47246ec)

# Workflow for GeoSpatial Data Analysis
![image](https://github.com/user-attachments/assets/b1a921c2-5a7e-40ee-89c1-e930c4a65152)

# Work Attribution
| Team Member | Role | Contribution|
|----------|----------|----------|
Komal Mann | Data Retriever| Developed code to access MSHA data using Selenium and PyTesseract integration, found correlations within the data for metal and Non-Metal Mining. Reviewed U.S. mining legislative actions and the impact of those actions on mining fatalities over time. |
Jessie Jung|Communications Specialist|Created a geospatial map of the data, found correlations within the data, cross referenced compiled data with existing data.|
Hyeun Jun Chang| Quality Assurance Reviewer| Did the NIOSH data processing, cleaned datasets, and analyzed trends in advancements in blasting and mining technology. Investigated correlations between technological advancements and mining fatalities. 
Aarnav Deenapanray|Team Leader| Developed code to access MSHA data using Selenium and PyTesseract integration, Found correlations within the data for Coal Mining. |



   
