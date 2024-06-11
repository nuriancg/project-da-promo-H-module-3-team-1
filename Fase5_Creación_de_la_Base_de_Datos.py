#Importamos librerias
from ast import literal_eval
import mysql.connector
from mysql.connector import Error


def crear_bbdd_y_tablas(host, user, password, schema_name):

    """
    Esta función crea una Base de Datos.

    Parameters:
    -----------------
    host (str): El nombre del host.
    user (str): El nombre del user.
    password (str): La contraseña para la conexión.
    schema_name (str): El nombre de la Base de Datos.

    Returns:
    ------------
    n/a
    """

    try:
        connection = mysql.connector.connect(host=host, user=user, password=password)
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {schema_name}")
            print('')
            print(f"* Base de datos '{schema_name}' creada correctamente o ya existente.")
            connection.commit()

            # Conectarmos a la base de datos creada
            connection.database = schema_name
            queries = ["""
            CREATE TABLE IF NOT EXISTS Employee (
                Employee_Number INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                Attrition BOOLEAN,
                Department VARCHAR(100),
                Job_Role VARCHAR(100),
                Job_Level TINYINT,
                Age_Group VARCHAR(6),
                CONSTRAINT chk_Job_Level CHECK (Job_Level BETWEEN 1 AND 5)
                );
                """,
                """
            CREATE TABLE IF NOT EXISTS Human_Resources (
                Employee_Number INT NOT NULL,
                Age INT,
                Gender CHAR(1),
                Marital_Status VARCHAR(100),
                Date_Birth INT,
                Education TINYINT,
                Education_Field VARCHAR(100),
                Num_Companies_Worked INT,
                Total_Working_Years INT,
                Training_Times_Last_Year INT,
                Years_At_Company INT,
                Years_With_Curr_Manager INT,
                Years_Since_Last_Promotion INT,
                Performance_Rating TINYINT,
                Job_Involvement TINYINT,
                Distance_From_Home INT,
                CONSTRAINT fk_HR_Employee_Number FOREIGN KEY (Employee_Number) REFERENCES Employee(Employee_Number),
                CONSTRAINT chk_Gender CHECK (Gender IN ('F', 'M')),
                CONSTRAINT chk_Marital_Status CHECK (Marital_Status IN ('Married', 'Divorced', 'Single', 'Unknown')),
                CONSTRAINT chk_Education CHECK (Education BETWEEN 1 AND 5),
                CONSTRAINT chk_Performance_Rating CHECK (Performance_Rating BETWEEN 1 AND 5),
                CONSTRAINT chk_Job_Involvement CHECK (Job_Involvement BETWEEN 1 AND 5)
                );
                """,
                """
            CREATE TABLE IF NOT EXISTS Finance (
                Employee_Number INT,
                Daily_Rate INT,
                Hourly_Rate INT,
                Monthly_Rate INT,
                Percent_Salary_Hike DECIMAL(5,2),
                Over_Time VARCHAR(50),
                CONSTRAINT fk_F_Employee_Number FOREIGN KEY (Employee_Number) REFERENCES Employee(Employee_Number),
                CONSTRAINT chk_Percent_Salary_Hike CHECK (Percent_Salary_Hike BETWEEN 0 AND 1),
                CONSTRAINT chk_Over_Time CHECK (Over_Time IN ('True', 'False', 'Unknown'))
                );
                """,
                """
            CREATE TABLE IF NOT EXISTS Job_Benefits (
                Employee_Number INT,
                Business_Travel VARCHAR(100),
                Remote_Work BOOLEAN, 
                Stock_Option_Level TINYINT,         
                CONSTRAINT fk_JB_Employee_Number FOREIGN KEY (Employee_Number) REFERENCES Employee(Employee_Number),
                CONSTRAINT chk_Stock_Option_Level CHECK (Stock_Option_Level BETWEEN 0 AND 4)
                );
                """,
                """
            CREATE TABLE IF NOT EXISTS Surveys (
                Employee_Number INT,
                Environment_Satisfaction INT,
                Job_Satisfaction TINYINT,
                Relationship_Satisfaction TINYINT,
                Satisfaction_Group VARCHAR(25),
                Work_Life_Balance TINYINT, 
                CONSTRAINT fk_S_Employee_Number FOREIGN KEY (Employee_Number) REFERENCES Employee(Employee_Number),
                CONSTRAINT chk_Relationship_Satisfaction CHECK (Relationship_Satisfaction BETWEEN 1 AND 5),
                CONSTRAINT chk_Job_Satisfaction CHECK (Job_Satisfaction BETWEEN 1 AND 5),
                CONSTRAINT chk_Work_Life_Balance CHECK (Work_Life_Balance BETWEEN 1 AND 5)
                );
            """]
                # Ejecuta cada consulta de creación de tablas individualmente porque si lo hacemos a la vez da error.
            num_tablas=0
            for query in queries:
                cursor.execute(query)
                connection.commit()
                num_tablas+=1
            print(f'* {num_tablas} tablas creadas correctamente')
    except Error as e:
            print('')
            print(f"!!! Error al crear tablas: {e}")
            connection.rollback()  # Retrocede cambios si hay un error
    finally:
            cursor.close() 
            
