import sqlalchemy    # These 2 libraries sqlalchemy and pyodbc are use to connect programming language with SQL (SSMS).
import pyodbc        # pyodbc is use to make a database connection.
from info import password
from sqlalchemy import text


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

# Simple sql query to create a table:-

create_table_query = """ 
CREATE TABLE airline (
    id INT PRIMARY KEY IDENTITY(1,1), 
    recorded_date DATE NULL, 
    review_date TEXT NULL, 
    airline VARCHAR(255) NULL,
    title TEXT NULL,
    review TEXT NULL,
    over_all_rating TEXT NULL, 
    name VARCHAR(255) NULL, 
    date VARCHAR(255) NULL, 
    text TEXT NULL, 
    type_of_traveller VARCHAR(255) NULL, 
    seat_type VARCHAR(255) NULL, 
    route VARCHAR(255) NULL, 
    date_flown VARCHAR(255) NULL, 
    seat_comfort VARCHAR(255) NULL, 
    cabin_staff_service VARCHAR(255) NULL, 
    food_and_beverages VARCHAR(255) NULL, 
    ground_service VARCHAR(255) NULL, 
    value_for_money VARCHAR(255) NULL, 
    recommended VARCHAR(255) NULL, 
    aircraft VARCHAR(255) NULL, 
    inflight_entertainment VARCHAR(255) NULL, 
    wifi_and_connectivity VARCHAR(255) NULL, 
    airline_id VARCHAR(255) NULL, 
);
"""

# Execute SQL Query To Create the Table

with connection.cursor() as cursor:             # Here, connection() is use to establish a connection between the Python an SQL (SSMS)
    cursor.execute(create_table_query)          # cursor() is the function of  connection , which is responsible # to execute SQL query
    connection.commit()                         # commit() is the function of connection, which is use to commit()s (ie, changes will be saved)






