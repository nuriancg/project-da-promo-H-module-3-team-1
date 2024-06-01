import mysql.connector
from mysql.connector import errorcode
import pandas as pd


# Función de conexión a MySQL
def connect_to_mysql():
    connection = mysql.connector.connect(
        host='localhost',  
        user='root', 
        password='AlumnaAdalab',
        
    )
    return connection

archivo = 'HR_CLEAN_DATA_2.csv'
#Funcion extraccion de datos:
def extract_data(archivo):
    return pd.read_csv(archivo)

# Función para crear la base de datos
def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Personal_Record (
        Age INT,
        Age_Group VARCHAR(100),
        Attrition BOOLEAN,
        Business_Travel VARCHAR(100),
        Daily_Rate INT,
        Department VARCHAR(100),
        Distance_From_Home INT,
        Education TINYINT,
        Education_Field VARCHAR(100),
        Employee_Number INT PRIMARY KEY,
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
        CONSTRAINT chk_Stock_Option_Level CHECK (Stock_Option_Level BETWEEN 1 AND 4),
        CONSTRAINT chk_Work_Life_Balance CHECK (Work_Life_Balance BETWEEN 1 AND 5)
    );
    """)  
    connection.commit()
    
    # Función de carga de datos
def load_data(archivo, connection):
    cursor = connection.cursor()
    # Building the SQL insert statement dynamically based on df columns
    cols = ', '.join([f"`{col}`" for col in archivo.columns])
    placeholders = ', '.join(['%s'] * len(archivo.columns))
    sql = f"INSERT INTO Personal_Record ({cols}) VALUES ({placeholders})"
    
    for index, row in archivo.iterrows():
        cursor.execute("USE nombre_de_tu_base_de_datos",sql, tuple(row))
    connection.commit()
    cursor.close()

    # Función principal para ejecutar la ETL
def run_etl(archivo):
    connection = connect_to_mysql()
    data = extract_data(archivo)
    create_database(connection)
    load_data(data, connection)
    connection.close()

if __name__ == "__main__":
    file_path = 'HR_CLEAN_DATA_2.csv'
    run_etl(file_path)
    
    