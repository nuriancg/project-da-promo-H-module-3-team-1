#Importamos librerias
import pandas as pd
import mysql.connector
from mysql.connector import Error
import warnings

import os

#Importamos otros ficheros
import Fase5_menu as menu
import Fase5_Carga_de_Datos as cdd
import Fase5_Creación_de_la_Base_de_Datos as cbbdd
import Fase5_Transformación_de_Datos as tdd

# Ajustes de visualizacion
pd.set_option('display.max_columns', None)
warnings.filterwarnings("ignore")



host = '127.0.0.1'
user = 'root'
password = 'AlumnaAdalab'
schema_name = 'ABC_Corporation'
# data_url = 'https://raw.githubusercontent.com/nuriancg/project-da-promo-H-module-3-team-1/master/HR_CLEAN_DATA.csv'


while True:
        menu.logo_inicio()
        seleccion = menu.menu()
  
        if seleccion == 1:
                os.system("clear")
                #url_raw_data = 'https://raw.githubusercontent.com/nuriancg/project-da-promo-H-module-3-team-1/master/HR_RAW_DATA.csv'
                url_raw_data = input('Introduce la dirección del archivo que quieres abrir: ')
                print('')
                df = tdd.leer_fichero(url_raw_data)
                print('')
                input('Presiona "ENTER" para continuar')

        elif seleccion == 2:
                os.system("clear")
                df = tdd.transformacion_datos(df)
                df = tdd.cambio_employee_num(df)
                print(f' \N{check mark}',f' Se ha creado un Data Frame con {df.shape[0]} filas y {df.shape[1]} columnas. ')
                print('')
                print(f'Columnas: \n{list(df.columns)}')
                #url_clean_data='https://raw.githubusercontent.com/nuriancg/project-da-promo-H-module-3-team-1/master/HR_CLEAN_DATA.csv'
                print('')
                url_clean_data= input('Introduce la dirección dónde quieres guardar el archivo: ')
                print('')
                tdd.guardar_fichero(df,url_clean_data) 
                print('')
                input('Presiona "ENTER" para continuar')
        

        elif seleccion == 3:
                os.system("clear")
                cbbdd.crear_bbdd_y_tablas(host, user, password, schema_name)
                input('Presiona "ENTER" para continuar')

        elif seleccion == 4:
                os.system("clear")
                connection = mysql.connector.connect(host=host, user=user, password=password, database=schema_name)
                df = pd.read_csv(url_clean_data) 
                for tabla in ['Employee', 'Human_Resources', 'Finance', 'Job_Benefits', 'Surveys']:
                        cdd.insertar_datos_tabla(df, connection, tabla)
                input('Presiona "ENTER" para continuar')        

        elif seleccion == 5:
                print("")
                print('Gracias y hasta pronto')
                print("    \N{slightly smiling face} \N{slightly smiling face} \N{slightly smiling face} \N{slightly smiling face} \N{slightly smiling face}")
                print('')
                input('Presiona "ENTER" para continuar')
                exit()

        else:
                print('')
                print('!!! Esa opcion no es valida ¡¡¡')
                print('       \N{neutral face}','\N{neutral face}','\N{neutral face}','\N{neutral face}','\N{neutral face}')
                print('')
                input('Presiona "ENTER" para continuar')
                continue
         

