#%%
from ETL_soporte import crear_bbdd, crear_tablas, insertar_datos_tabla
from mysql.connector import Error
import mysql.connector
import pandas as pd

def main():
    host = '127.0.0.1'
    user = 'root'
    password = 'AlumnaAdalab'
    schema_name = 'ABC_Corporation'
    data_url = 'https://raw.githubusercontent.com/nuriancg/project-da-promo-H-module-3-team-1/master/HR_CLEAN_DATA.csv'

    
    crear_bbdd(host, user, password, schema_name)

    
    connection = mysql.connector.connect(host=host, user=user, password=password, database=schema_name)
    
   
    crear_tablas(connection)

  
    df = pd.read_csv(data_url)
    for tabla in ['Employee', 'Human_Resources', 'Finance', 'Job_Benefits', 'Surveys']:
        insertar_datos_tabla(df, connection, tabla)

    
    connection.close()

if __name__ == "__main__":
    main()
# %%
# SEGUNDA OPCION INTERACTIVA ???


