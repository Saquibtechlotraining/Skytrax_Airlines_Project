import requests                 # request module is use to for making requests to fetch pages or data from websites.
from bs4 import BeautifulSoup   # A python library use for parsing HTML & XML documents, making it easier to extract specific information from webpages.
import pandas as pd             # Use to Data Cleaning and save the data in Excel or CSV format.
import datetime                 # datetime module use to save the current date.
import sqlalchemy               # These 2 libraries sqlalchemy and pyodbc are use to connect programming language with SQL (SSMS).
import pyodbc                   # pyodbc is use to make a database connection.
from info import password
from sqlalchemy import text

# Read airline file
f = open(r'airline_number.txt', 'r')
number = int(f.read())                  # Whenever we read the data the datatype is always in string, Here:, '0', '1',.... So convert
                                        # into intger(ie, 0,1,....), So we can add number+1, ......
f.close()


# Database Connection:-
server = 'saquibskytraxserver.database.windows.net, 1433'      # Here, 1433 are the port no. use to connect python with SQL (SSMS)
database = 'saquib_database_skytrax'
username = 'skytrax_saquibadmin'
password = password
driver = '{ODBC Driver 17 for SQL Server}'

# Create pyodbc connection string:-
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Connect to the Database using pyodbc connection string:-
connection = pyodbc.connect(connection_string)

# Create a sqlalchemy engine
engine = sqlalchemy.create_engine(f'mssql+pyodbc:///?odbc_connect={connection_string}')


recorded_date = str(datetime.date.today())

def collect_airline_names():

    list_of_airlines = []
    url = 'https://www.airlinequality.com/review-pages/latest-airline-reviews/'

    html = requests.get(url).content                                   # making requests

    soup = BeautifulSoup(html, 'lxml')                                 # converting HTML content to BeautifulSoup

    box = soup.find('ul', class_='item')                               # In this ul tag and class_='item' contains all the airlines name

    airline_names = box.find_all('li')                                 # Fetch the value from every li tag which is store in ul tag and class_='item'

    for airline_name in airline_names:
        list_of_airlines.append(airline_name.get_text())

    return list_of_airlines

# ***********************************************************************************************************************

def collect_airline_reviews(airline_name):

    list_of_reviews = []
    page = 1

    while True:

        print(f'Collection Data From Page {page}')

        url = f"https://www.airlinequality.com/airline-reviews/{airline_name.lower().replace(' ','-')}/page{page}/"


        html = requests.get(url).content

        soup = BeautifulSoup(html, 'lxml')

        boxes = soup.find_all('article', itemprop='review')

        if (bool(boxes)==False):
            break


        for box in boxes:
            dictionary_of_reviews = {}

            title = box.find('h2', class_='text_header').get_text()
            name = box.find('span', itemprop='name').get_text()
            review_date = box.find('time', itemprop='datePublished').get_text()
            review = box.find('div', class_='text_content').get_text()
            over_all_rating = box.find('span', itemprop='ratingValue')

            if (over_all_rating == None):
                over_all_rating = 0
            else:
                over_all_rating = over_all_rating.get_text()

            table = box.find('table', class_='review-ratings')
            table_rows = table.find_all('tr')

            d = {}

            for table_row in table_rows:
                table_data = table_row.find_all('td')
                key = table_data[0].get_text()
                value = table_data[1]
                if (value.find('span')):
                    value = len(value.find_all('span', class_='star fill'))
                else:
                    value = value.get_text()

                d[key] = value


            # column creation
            dictionary_of_reviews['recorded_date'] = recorded_date
            dictionary_of_reviews['airline'] = airline_name
            dictionary_of_reviews['name'] = name
            dictionary_of_reviews['review_date'] = review_date
            dictionary_of_reviews['review'] = review
            dictionary_of_reviews['over_all_rating'] = over_all_rating
            dictionary_of_reviews['detail'] = d

            list_of_reviews.append(dictionary_of_reviews)

        page = page + 1

    return list_of_reviews

# collecting list of airlines
airlines = collect_airline_names()       # all airlines names store in the airlines variable

print(f'Collecting Data from {airlines[number]}')
reviews = collect_airline_reviews(airlines[number])

mydata = pd.json_normalize(reviews)

# Basic Data Cleaning

# mydata.columns - Contain all the columns name Eg:- recorded date, detail.Wifi & Connectivity etc.

mydata.columns = mydata.columns.str.lower()
mydata.columns = mydata.columns.str.replace(' ','_')
mydata.columns = mydata.columns.str.replace('&','and')
mydata.columns = mydata.columns.str.replace('detail.','')
mydata['recorded_date'] = pd.to_datetime(mydata['recorded_date'])                   # Converting from string to Datetime

with engine.connect() as connection:                                                     # connect() is a function
    mydata.to_sql('airline', con=connection, if_exists='append', index=False,schema='dbo')


# if_exists='append' ->  Because if whenever we run again the data will be append.
# index=False        ->  We dont want index 0,1,2,3....
# con=connection     ->  Make a pyodbc connection
# schema='dbo'       ->  Giving schema 'dbo' in SSMS

f = open('airline_number.txt', 'w')
f.write(f'{number+1}')
f.close()




