#Importamos librerias
import pandas as pd
import mysql.connector
from mysql.connector import Error

import os

#Importamos otros ficheros
import Fase5_menu as menu
import Fase5_Carga_de_Datos as cdd
import Fase5_Creación_de_la_Base_de_Datos as cbbdd
import Fase5_Transformación_de_Datos as tdd

host = '127.0.0.1'
user = 'root'
password = 'AlumnaAdalab'
schema_name = 'ABC_Corporation'
# data_url = 'https://raw.githubusercontent.com/nuriancg/project-da-promo-H-module-3-team-1/master/HR_CLEAN_DATA.csv'

seleccion = menu.menu()
while seleccion != 5:
    menu.logo_inicio()
    seleccion = menu.menu()
  
    if seleccion == 1:
            cbbdd.crear_bbdd_y_tablas(host, user, password, schema_name)
    elif seleccion == 2:
            url_raw_data = input('Introduce la dirección del archivo que quieres abrir: ')
            tdd.leer_fichero(url_raw_data)
    # elif seleccion == 3:
    #     tdd.
    elif seleccion == 4:
            connection = mysql.connector.connect(host=host, user=user, password=password, database=schema_name)
            df = pd.read_csv(url_raw_data) 
            for tabla in ['Employee', 'Human_Resources', 'Finance', 'Job_Benefits', 'Surveys']:
                cdd.insertar_datos_tabla(df, connection, tabla)

    


   


        

        
    
# %%
