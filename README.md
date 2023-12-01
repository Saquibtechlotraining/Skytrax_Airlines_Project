# Skytrax Airlines Project

Dashboard Link : https://www.novypro.com/project/aviation-fleet-dashboard-airlines--aircrafts-overview

#### Note:- For this project, I scraped data from the 14th of September, 2023.

Sample Data [Click Here](https://github.com/Saquibtechlotraining/Skytrax_Airlines_Project/blob/main/Skytrax_Project/sample.xlsx)

Raw Data [Click Here](https://github.com/Saquibtechlotraining/Skytrax_Airlines_Project/blob/main/Skytrax_All_Airlines_Reviews_data.csv)

Clean Data [Click Here](https://github.com/Saquibtechlotraining/Skytrax_Airlines_Project/blob/main/Skytrax_Project/Clean_Data/clean_skytrax_data.csv)

### • Loading Data also in SQL Server Management Studio(SSMS) 
Table creation Code [Click Here](https://github.com/Saquibtechlotraining/Skytrax_Airlines_Project/blob/main/Skytrax_Project/table.py)

## TABLE OF CONTENT
### 1) Project Overview 
    1.1 Background 
    1.2 Objective 
    1.3 Key Components

### 2) Data Collection and Storage 
    2.1 Web Scraping from Skytrax Reviews 
  [Click Here](https://github.com/Saquibtechlotraining/Skytrax_Airlines_Project/blob/main/Skytrax_Project/scraping.py)
  
    2.2 Azure SQL Database Integration 

    Azure SQL Database Integration Properties
  [Click Here](https://github.com/Saquibtechlotraining/Skytrax_Airlines_Project/blob/main/My%20Azure%20resource_group_admin_%26password.txt)

### 3) Data Processing and Analysis 
    3.1 Data Extraction with Pyspark (Databricks)
  [Click Here](https://github.com/Saquibtechlotraining/Skytrax_Airlines_Project/tree/main/Screenshot_Load_data_in_Pyspark)

    Preprocessing with Pandas Part-1 
  [Click Here](https://github.com/Saquibtechlotraining/Skytrax_Airlines_Project/blob/main/Skytrax_Project/SkytraxProject_Part-1.ipynb)

    After Part-1 Save data
  [Click Here](https://github.com/Saquibtechlotraining/Skytrax_Airlines_Project/blob/main/Skytrax_Project/Skytrax_Airlines_Reviews.csv)

    Part-2 
  [Click Here](https://github.com/Saquibtechlotraining/Skytrax_Airlines_Project/blob/main/Skytrax_Project/SkytraxProject_Part-2.ipynb)
 
    3.2 Exploratory Data Analysis (EDA)
    3.3 Advanced Analytics

### 4) Results and Insights 
    4.1 Extracted Insights 
    4.2 Visualization of Findings 
    4.3 Business Implications

### 5) Conclusion 
    5.1 Project Impact 
    5.2 Lessons Learned 
    5.3 Future Enhancements

## Content
### 1) Project Overview
    1.1 Background
    1.2 Objective
    1.3 Key Components

#### 1.1 Background
In today's rapidly evolving airline industry, customer feedback plays a pivotal role in shaping business strategies. This project centers around harnessing the power of data by collecting and analyzing airline reviews from Skytrax, a leading source of passenger opinions and reviews for airlines worldwide.

#### 1.2 Objective
The primary objective of our project is to extract meaningful insights from daily airline reviews, enabling airlines to make data-driven decisions to enhance customer satisfaction, optimize services, and stay competitive in the market.

#### 1.3 Key Components
The Skytrax Airline Reviews Analysis Pipeline comprises four crucial stages: data collection, data storage, data processing, and insights generation. Each stage is meticulously designed to ensure the accuracy, integrity, and reliability of the extracted information.

### 2) Data Collection and Storage
    2.1 Web Scraping from Skytrax Reviews
    2.2 Azure SQL Database Integration

#### 2.1 Web Scraping from Skytrax Reviews
At the core of this project is the data collection process, where advanced web scraping techniques are employed to gather a representative sample of airline reviews from the Skytrax website. Cutting-edge technologies navigate through web pages, extract relevant information, and transform it into structured data.

#### 2.2 Azure SQL Database Integration
For seamless and efficient data management, we leverage Azure SQL Database, a robust cloud-based relational database service. Collected reviews are securely stored, ensuring data availability, scalability and robustness. This integration facilities easy data retrieval and forms the foundation for subsequent analysis.

### 3) Data Processing and Analysis
    3.1 Data Extraction with Pyspark (Databricks) and Preprocessing with Pandas
    3.2 Exploratory Data Analysis (EDA)
    3.3 Advanced Analytics

#### 3.1 Data Extraction with Pyspark (Databricks) and Preprocessing with Pandas
 In this section, we navigate the technical intricacies of data preprocessing, initially utilizing Pyspark for the extraction phase. Pyspark, a powerful tool for large-scale data analysis, efficiently processes and extracts the raw data. Following the extraction, the data is stored in CSV file format in the local system. The subsequent preprocessing stage is then seamlessly executed using Pandas. Leveraging Pandas's capabilities for data manipulation and 
analysis, we clean and transform the CSV-formatted data into a structured format, laying a robust-foundation for further analysis.

#### 3.2 Exploratory Data Analysis (EDA)
With the preprocessed data in hand, we embark on an exploratory journey to uncover hidden patterns, trends and anomalies. Employing Exploratory 
Data Analysis (EDA) techniques, we visualize and summarize the data. The process provides an initial glimpse into passenger's sentiments, preferences,
and experiences, enhancing our understanding of the dataset.

#### 3.3 Advanced Analytics
Building upon the refined dataset, advanced analytical techniques take centre stage. Machine Learning algorithms, sentiment analysis, and text mining are among the methodologies employed to extract deeper insights. The advances analyses empower airlines to identify key areas for improvement and strategically capitalize on their strengths, contributing to a comprehensive understanding of the reviews.

### 4) Results and Insights
    4.1 Extracted Insights
    4.2 Visualization of Findings
    4.3 Business Implications

#### 4.1 Extracted Insights
The culmination of our efforts is the extraction of invaluable insights from the vast pool of reviews. These insights shed light on critical aspects such as service quality, customer satisfaction, and emerging trends. We present these findings in a structured and actionable manner, equipping airlines with data-backed knowledge to make informed decisions.

#### 4.2 Visualization of Findings
Visual representation of data plays a pivotal role in conveying complex information concisely. In this section, we showcase a variety of visually appealing graphs, charts, maps, tables that encapsulate the essence of our analyses. These visualizations make it easy to grasp the implications of the data at a glance.

#### 4.3 Business Implications
The true value of our project emerges as we translate insights into tangible business strategies. We explore the real-world implications of our findings, demonstrating how airlines can optimize operations, refine customer interactions, and devise innovative marketing campaigns based on the data-driven insights.

### 5) Conclusion 
    5.1 Project Impact
    5.2 Lessons Learned
    5.3 Future Enhancements

#### 5.1 Project Impact
In the final section of our documentation, we reflect upon the impact of the Skytrax Airline Reviews Analysis Pipeline. We highlight the ways in which our project contributes to the evolution of the airline industry, fostering a culture of data-driven decision-making and continuous improvement.

#### 5.2 Lessons Learned
No project is without its challenges and learning experiences. In this subsection, we candidly discuss the hurdles we encountered during the project's lifecycle and the strategies we employed to overcome them. These insights serve as a valuable resource for future endeavors.

#### 5.3 Future Enhancements
As technology and data science methodologies evolve, so too will our project. We outline potential avenues for future enhancements, including the integration of additional data sources, implementation of more advanced analytics, and exploration of predictive modeling.

### Dashboard View
![Screenshot 2023-12-01 214152](https://github.com/Saquibtechlotraining/image-added-readme/assets/91885135/3811f98b-13e3-4fc9-a7b0-62e7cb90bdf7)

![Screenshot 2023-12-01 214214](https://github.com/Saquibtechlotraining/image-added-readme/assets/91885135/31086bd6-6804-4190-9704-e3a957581d97)

![Screenshot 2023-12-01 214225](https://github.com/Saquibtechlotraining/image-added-readme/assets/91885135/b52e5888-4158-42cf-9249-fec473cd53be)

![Screenshot 2023-12-01 214235](https://github.com/Saquibtechlotraining/image-added-readme/assets/91885135/e3601c57-b51a-466f-b15e-46105e38ed1c)



 ## Model View
![image](https://github.com/Saquibtechlotraining/image-added-readme/assets/91885135/4babd2c6-9d31-49bb-ad86-711562e7bf18)



