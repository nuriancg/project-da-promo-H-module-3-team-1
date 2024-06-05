#!/usr/bin/env python
# coding: utf-8

# ## Creacion BBDD y Tabla Principal:

# In[29]:


import pandas as pd
import mysql.connector
from mysql.connector import Error


# In[30]:


def crear_schema(host, user, password, schema_name):
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
        


# In[31]:


def crear_base_datos(connection):
    cursor = connection.cursor()
    try:
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
        for query in queries:
            cursor.execute(query)
            connection.commit()
            print('Tablas creadas correctamente')# Asegura la ejecución y commit de cada comando individualmente
    except Error as e:
        print(f"Error al crear tablas: {e}")
        connection.rollback()  # Retrocede cambios si hay un error
    finally:
        cursor.close() 


# In[32]:


def insertar_datos_tabla(df,connection, nombre_tabla):
    tabla_columnas = {
        'Employee': ['Employee_Number', 'Attrition', 'Department', 'Job_Role', 'Job_Level', 'Age_Group'],
        'Human_Resources': [
            'Employee_Number', 'Age', 'Gender', 'Marital_Status', 'Date_Birth',
            'Education', 'Education_Field', 'Num_Companies_Worked', 'Total_Working_Years',
            'Training_Times_Last_Year', 'Years_At_Company', 'Years_With_Curr_Manager',
            'Years_Since_Last_Promotion', 'Performance_Rating', 'Job_Involvement', 'Distance_From_Home'],
        'Finance': ['Employee_Number', 'Daily_Rate', 'Hourly_Rate', 'Monthly_Rate', 'Percent_Salary_Hike', 'Over_Time'],
        'Job_Benefits': ['Employee_Number', 'Business_Travel', 'Remote_Work', 'Stock_Option_Level'],
        'Surveys': [
            'Employee_Number', 'Environment_Satisfaction', 'Job_Satisfaction',
            'Relationship_Satisfaction', 'Satisfaction_Group', 'Work_Life_Balance']
    }
    if nombre_tabla in tabla_columnas:
        if set(tabla_columnas[nombre_tabla]).issubset(df.columns): # issubset() es un mét
    
            # Hacemos inserción de datos
            cursor = connection.cursor()
            sub_df = df[tabla_columnas[nombre_tabla]]  # Usamos solo las columnas relevantes a la tabla que queremos.
            cols = ', '.join([f"`{col}`" for col in sub_df.columns])  # 'col' y 'placeholders' es sintaxis SQL para insertar valores en una tabla.
            placeholders = ', '.join(['%s'] * len(sub_df.columns))
            sql = f"INSERT INTO {nombre_tabla} ({cols}) VALUES ({placeholders})" 
            data = [tuple(row) for row in sub_df.to_numpy()] # Preparamos los datos para la inserción iterando sobre las filas que necesitamos.
            try:
                cursor.executemany(sql, data)
                connection.commit()
                print(f"Datos insertados correctamente en la tabla {nombre_tabla}.")
            except Error as e:
                print(f"Error al insertar datos en la tabla {nombre_tabla}: {e}")
                connection.rollback() # Deshace los datos insertados antes del error
            finally:
                cursor.close()
        else:
            print(f"Faltan columnas en el DataFrame para insertar en la tabla {nombre_tabla}.")
    else:
        print("Nombre de tabla no reconocido.")

    cursor.close()
# In[37]:



# host = '127.0.0.1'
# user = 'root'
# password = 'AlumnaAdalab'
# schema_name = 'ABC_Corporation'
# df = pd.read_csv('https://raw.githubusercontent.com/nuriancg/project-da-promo-H-module-3-team-1/master/HR_CLEAN_DATA.csv')

 # Ejecutamos funciones para comprobar_
# crear_schema(host, user, password, schema_name)
# connection = mysql.connector.connect(host=host, user=user, password=password, database=schema_name)

# crear_base_datos(connection)

# insertar_datos_tabla(df, connection,'Surveys') # 'Employee','Human_Resources','Finance', 'Job_Benefits','Surveys'

# connection.close()

