


import pandas as pd
import mysql.connector
from mysql.connector import Error

def create_schema(host, user, password, schema_name):
    try:
        connection = mysql.connector.connect(host=host, user=user, password=password)
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {schema_name}")
            print(f"Database '{schema_name}' creada o ya existe.")
            cursor.close()
        connection.close()
    except Error as e:
        print(f"Error mientras conectamos  MySQL: {e}")

def create_database(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Personal_Record (
            Employee_Number INT PRIMARY KEY,
            Age INT,
            Age_Group VARCHAR(100),
            Attrition BOOLEAN,
            Business_Travel VARCHAR(100),
            Daily_Rate INT,
            Department VARCHAR(100),
            Distance_From_Home INT,
            Education TINYINT,
            Education_Field VARCHAR(100),
            Environment_Satisfaction INT,
            Gender CHAR(1),
            Hourly_Rate INT,
            Job_Involvement TINYINT,
            Job_Level TINYINT,
            Job_Role VARCHAR(100),
            Job_Satisfaction TINYINT,
            Marital_Status VARCHAR(100),
            Monthly_Income INT,
            Monthly_Rate INT,
            Num_Companies_Worked INT,
            Over_Time VARCHAR(50),
            Percent_Salary_Hike DECIMAL(5,2),
            Performance_Rating TINYINT,
            Relationship_Satisfaction TINYINT,
            Satisfaction_Group VARCHAR(25), 
            Stock_Option_Level TINYINT,
            Total_Working_Years INT,
            Training_Times_Last_Year INT,
            Work_Life_Balance TINYINT,
            Years_At_Company INT,
            Years_Since_Last_Promotion INT,
            Years_With_Curr_Manager INT,
            Date_Birth INT,
            Remote_Work BOOLEAN,
            CONSTRAINT chk_Gender CHECK (Gender IN ('F', 'M')),
            CONSTRAINT chk_Over_Time CHECK (Over_Time IN ('True', 'False', 'Unknown')),
            CONSTRAINT chk_Percent_Salary_Hike CHECK (Percent_Salary_Hike BETWEEN 0 AND 1),
            CONSTRAINT chk_Education CHECK (Education BETWEEN 1 AND 5),
            CONSTRAINT chk_Job_Involvement CHECK (Job_Involvement BETWEEN 1 AND 5),
            CONSTRAINT chk_Job_Level CHECK (Job_Level BETWEEN 1 AND 5),
            CONSTRAINT chk_Job_Satisfaction CHECK (Job_Satisfaction BETWEEN 1 AND 5),
            CONSTRAINT chk_Marital_Status CHECK (Marital_Status IN ('Married', 'Divorced', 'Single', 'Unknown')),
            CONSTRAINT chk_Performance_Rating CHECK (Performance_Rating BETWEEN 1 AND 5),
            CONSTRAINT chk_Relationship_Satisfaction CHECK (Relationship_Satisfaction BETWEEN 1 AND 5),
            CONSTRAINT chk_Stock_Option_Level CHECK (Stock_Option_Level BETWEEN 0 AND 4),
            CONSTRAINT chk_Work_Life_Balance CHECK (Work_Life_Balance BETWEEN 1 AND 5)
        );
        """)
        connection.commit()
        print("Se ha creado la tabla.")
    except Error as e:
        print(f"Error al crear tabla: {e}")
    finally:
        cursor.close()

def load_data(df, connection):
    cursor = connection.cursor()
    cols = ', '.join([f"`{col}`" for col in df.columns])
    placeholders = ', '.join(['%s'] * len(df.columns))
    sql = f"INSERT INTO Personal_Record ({cols}) VALUES ({placeholders})"
    try:
        for index, row in df.iterrows():
            cursor.execute(sql, tuple(row))
        connection.commit()
        print("registros insertados correctamente.")
    except Error as e:
        print(f"Error al insertar datos: {e}")
        connection.rollback()
    finally:
        cursor.close()

# Ejecucion principal
host = '127.0.0.1'
user = 'root'
password = 'AlumnaAdalab'
schema_name = 'ABC_Corporation'

# Creamos schema 
create_schema(host, user, password, schema_name)
connection = mysql.connector.connect(host=host, user=user, password=password, database=schema_name)

# aseguramos que el schema existe
create_database(connection)

# Insertamos datos a la tabla
df = pd.read_csv('https://raw.githubusercontent.com/nuriancg/project-da-promo-H-module-3-team-1/master/HR_CLEAN_DATA.csv')
load_data(df, connection)

# Cerramos conexion
connection.close()