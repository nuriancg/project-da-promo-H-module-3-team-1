#Importamos librerias
from mysql.connector import Error
from ast import literal_eval
import mysql.connector
import pandas as pd
import os

def insertar_datos_tabla(df,connection, nombre_tabla):

    """
    Esta función inserta datos en las tablas de la Base de Datos.

    Parameters:
    -----------------
    df (DataFrame): El DataFrame del que queremos sacar la información.
    connection: El connector mysql.connector.connect(host=, user=, password=, database=)
    nombre_tabla (str): El nombre de la tabla al que queremos insertar la información

    Returns:
    ------------
    n/a
    """
        
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
                print(f"* Datos insertados correctamente en la tabla {nombre_tabla}.")
            except Error as e:
                print(f"!!! Error al insertar datos en la tabla {nombre_tabla}: {e}")
                connection.rollback() # Deshace los datos insertados antes del error
            finally:
                cursor.close()
        else:
            print(f"!!! Faltan columnas en el DataFrame para insertar en la tabla {nombre_tabla}.")
    else:
        print("!!! Nombre de tabla no reconocido.")

    cursor.close()
