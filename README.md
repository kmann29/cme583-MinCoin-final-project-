# Exploring US Mining Safety Data
CME583 Final Group Project - Group MinCoin

MinCoin Project Description:
This project will conduct an exploratory data analysis (EDA) of U.S. mining injury datasets, focusing on the relationships between policy changes, and injury trends. Key regulatory milestones, such as the Federal Mine Safety and Health Act, and advancements in mining technology will be analyzed to assess their impact on injury rates. These findings aim to identify gaps in current practices and guide future technological and regulatory improvements to reduce injuries in the mining sector.
Collaborators:

# Overview of Files
1. MinCoin MSHA Data Sorting(Non-Metal,Metal).ipynb : This code looks at all of the MSHA fatality reports from 2010 to 2024 and analyzes trends in fatalaties.  
   - extracted_data.csv : This is the extracted dataframe as a result of the Fatalatiy Report PDFs from the MSHA database ran
2. Mining disasters-fatilities.csv
3. Mining fatilities bots.ipynb: Mine Fatalities data is downloaded from NIOSH, and using mine name, city, and state, coordinate is extracted from wikipedia. For the one that did not have coordinates, openstreemap API is used to extract coordinates using city and state. Various graphs are demonstrated to conduct geospacial analysis and show correlation of safety regulations and improvememnt of mining technology. 
4. Tesseract Download.html
5. geospatial_analysis.ipynb : Reads the accident dataset from MSHA and generates a choropleth map of accident count throughout the United States along with multiple graphs to show the relationship between accident frequency, production, operator experience, etc. 
6. state_and_city_fatalities_map_with_spaced_legend.html
7. updated_test_data_with_coordinates.csv
8. us_accident_density_map.html : Accident map generated from geospatial_analysis.ipynb saved as html. 
9. webscraping_analysis.ipynb

# Link to Medium Article
Exploring U.S Mining Safety Data: https://medium.com/@komalmann98/exploring-u-s-mining-safety-data-ffa8df361138 
   
