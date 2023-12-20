# Skytrax Airlines Project

Dashboard Link : https://www.novypro.com/project/aviation-fleet-dashboard-airlines--aircrafts-overview-power-bi

Note:- For this project, I scraped data from the website [Skytrax](https://www.airlinequality.com/review-pages/latest-airline-reviews/) of 14th of September, 2023.

① Sample Data of one airline [Click Here](https://github.com/Saquibtechlotraining/Skytrax_Airlines_Project/blob/main/Skytrax_Project/sample.xlsx)

② Table creation Code [Click Here](https://github.com/Saquibtechlotraining/Skytrax_Airlines_Project/blob/main/Skytrax_Project/table.py)

## Project Overview 
    Background 
    Objective 

#### ➡ Background -
In today's rapidly evolving airline industry, customer feedback plays a pivotal role in shaping business strategies. This project centers around harnessing the power of data by collecting and analyzing 
airline reviews from Skytrax, a leading source of passenger opinions and reviews for airlines worldwide.

#### ➡ Objective -
The primary objective of our project is to extract meaningful insights from daily airline reviews, enabling airlines to make data-driven decisions to enhance customer satisfaction, optimize services, and stay competitive in the market.

## Skytrax Airlines Project Piplines:-
➡ Each stage is meticulously designed to ensure the accuracy, integrity, and reliability of the extracted information.
### Pipeline 1: Data Collection Pipeline
#### ① Task: Collecting airlines data from Skytrax.
#### ② Components:
##### • WebScrapping (Python)
    • Utilize advanced web scraping techniques to extract relevant information from the Skytrax website.
    • Employ cutting-edge technologies to navigate through web pages and transform raw data into a structured format.
Extracted Data/ Raw Data : [Click Here](https://github.com/Saquibtechlotraining/Skytrax_Airlines_Project/blob/main/Skytrax_All_Airlines_Reviews_data.csv)
    
##### • Data Storage (Azure SQL Database):
    • Integrate with Azure SQL Database for secure and efficient storage.
    • Ensure data availability, scalability, and robustness for easy retrieval.
Database Connection Information [Click Here](https://github.com/Saquibtechlotraining/Skytrax_Airlines_Project/blob/main/My%20Azure%20resource_group_admin_%26password.txt)

### Pipeline 2: Data Processing Pipeline
#### ① Task: Process and analyze the collected data to prepare it for insights generation.
#### ② Components:
##### • Data Extraction with Pyspark (Databricks):
    • Utilize Pyspark for large-scale data analysis and efficient extraction.
    • Store the extracted data in CSV format in the local system.
[Click Here](https://github.com/Saquibtechlotraining/Skytrax_Airlines_Project/tree/main/Screenshot_Load_data_in_Pyspark)

##### • Preprocessing with Pandas:
    • Leverage Pandas for data manipulation and analysis.
    • Clean and transform the CSV-formatted data into a structured format for further analysis.

## Pipeline 3: Exploratory Data Analysis (EDA) and Advanced Analytics Pipeline
#### ① Task: Explore data patterns, perform sentiment analysis, and apply advanced analytics techniques.
#### ② Components:
##### • Exploratory Data Analysis (Python):
    • Visualize and summarize the preprocessed data using EDA techniques.
    • Gain insights into passenger sentiments, preferences, and experiences.
 Preprocessing with Pandas Part-1 [Click Here](https://github.com/Saquibtechlotraining/Skytrax_Airlines_Project/blob/main/Skytrax_Project/SkytraxProject_Part-1.ipynb)
 
 After Part-1 Save data [Click Here](https://github.com/Saquibtechlotraining/Skytrax_Airlines_Project/blob/main/Skytrax_Project/Skytrax_Airlines_Reviews.csv)
 
 Preprocessing with Pandas Part-2 [Click Here](https://github.com/Saquibtechlotraining/Skytrax_Airlines_Project/blob/main/Skytrax_Project/SkytraxProject_Part-2.ipynb)

 Clean Data : [Clean Data](https://github.com/Saquibtechlotraining/Skytrax_Airlines_Project/blob/main/Skytrax_Project/Clean_Data/clean_skytrax_data.csv)

## Pipeline 4: Visualization
#### ① Task: Visualization of Clean Data 
#### ② Components:
##### • For Visualization use Power Bi :
     • After obtaining the final clean data, utilize Power BI for creating interactive and visually appealing dashboards and reports.
     Power BI allows for seamless visualization of insights, making it easy to 
     communicate and interpret complex information.

###### • Business Implications:
① Translate insights into tangible business strategies.
② Explore real-world implications and demonstrate how airlines can optimize operations, refine customer interactions, and devise innovative marketing campaigns based on data-driven insights.
    
###### • Project Impact Assessment:
Reflect on how the project contributes to the evolution of the airline industry and fosters a culture of data-driven decision-making.
    
###### • Lessons Learned:
Discuss challenges encountered during the project lifecycle and strategies employed to overcome them.
    
###### • Future Enhancements:
Outline potential avenues for future enhancements, including the integration of additional data sources, implementation of more advanced analytics, and exploration of predictive modeling.


### Dashboard View
![Screenshot 2023-12-01 222814](https://github.com/Saquibtechlotraining/image-added-readme/assets/91885135/9b3b3b86-a638-4e28-bb4f-4f989a01da5c)

![Screenshot 2023-12-01 222843](https://github.com/Saquibtechlotraining/image-added-readme/assets/91885135/59d9b151-0a68-4d9d-ac63-6e7cce4c5f93)

![Screenshot 2023-12-01 222923](https://github.com/Saquibtechlotraining/image-added-readme/assets/91885135/1e48c78a-6657-4bb6-b001-9dff8aa66492)


 ## Model View
![image](https://github.com/Saquibtechlotraining/image-added-readme/assets/91885135/4babd2c6-9d31-49bb-ad86-711562e7bf18)

## Tools Used:
• Scraping - Webscraping

• Programming Language - Python 

• Database - Azure SQL

• Data Extraction - Pyspark

• Data Preprocessing - Pandas

• Data Visualization - Power Bi


