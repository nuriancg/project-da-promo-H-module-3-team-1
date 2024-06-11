#Importamos librerias
import pandas as pd
import mysql.connector
from mysql.connector import Error
import warnings

import os

#Importamos otros ficheros
import Fase5_archivos_apoyo.Fase5_menu as menu
import Fase5_archivos_apoyo.Fase5_Carga_de_Datos as cdd
import Fase5_archivos_apoyo.Fase5_Creación_de_la_Base_de_Datos as cbbdd
import Fase5_archivos_apoyo.Fase5_Transformación_de_Datos as tdd

# Ajustes de visualizacion
pd.set_option('display.max_columns', None)
warnings.filterwarnings("ignore")


# Iniciamos variables necesarias para la conexión con MySQL
host = '127.0.0.1'
user = 'root'
password = 'AlumnaAdalab'


while True:
        menu.logo_inicio()
        seleccion = menu.menu()
  
        if seleccion == '1':
                os.system("clear")
                menu.logo_inicio()
                print('--------------------------------------------------------------------------')
                print('')
                #url_raw_data = 'https://raw.githubusercontent.com/nuriancg/project-da-promo-H-module-3-team-1/master/HR_RAW_DATA.csv'
                print('* Introduce la dirección del archivo que quieres abrir y presiona "ENTER":')
                print('')
                url_raw_data = input(' ')
                print('')

                try:
                        df = tdd.leer_fichero(url_raw_data)
                        print('')
                        input('Presiona "ENTER" para continuar')

                except:
                        print('!!! El formato del archivo no es correcto ¡¡¡')
                        print('')
                        print('Tiene que ser un archivo ".csv". Intentalo de nuevo.')
                        print('')
                        input('Presiona "ENTER" para continuar')
                        url_raw_data=()

        elif seleccion == '2':
                os.system("clear")
                menu.logo_inicio()
                print('--------------------------------------------------------------------------')
                print('')
                try:
                        df = tdd.transformacion_datos(df)
                        df = tdd.cambio_employee_num(df)
                        print('')
                        print(f' \N{check mark}',f' Se ha creado un Data Frame con {df.shape[0]} filas y {df.shape[1]} columnas. ')
                        print('')
                        offset=0
                        print('Columnas del Data Frame:')
                        for _ in range ((len(list(df.columns))//5)+1):
                                print(list(df.columns)[offset:(offset+5):])
                                offset+=5
                        #url_clean_data='https://raw.githubusercontent.com/nuriancg/project-da-promo-H-module-3-team-1/master/HR_CLEAN_DATA.csv'
                        print('')
                        print('* Introduce la dirección dónde quieres guardar el archivo y presiona "ENTER":')
                        print('')
                        url_clean_data= input(' ')
                        print('')
                        tdd.guardar_fichero(df,url_clean_data) 
                        print('')
                        input('Presiona "ENTER" para continuar')

                except:
                        print('!!! No hay datos guardados en la memória virtual !!!')
                        print('')
                        print(f'            \N{raised back of hand}   \N{raised back of hand}   \N{raised back of hand}   \N{raised back of hand}   \N{raised back of hand}')
                        print('')
                        print('Antes de transformar los datos debes de cargarlos seleccionando la OPCIÓN 1 del menú de inicio.')
                        print('')
                        input('Presiona "ENTER" para continuar')
        

        elif seleccion == '3':
                os.system("clear")
                menu.logo_inicio()
                print('--------------------------------------------------------------------------')
                print('')
                print('* Introduce el nombre de la Base de Datos que quieres crear y presiona "ENTER":')
                print('')
                schema_name= input(' ')
                cbbdd.crear_bbdd_y_tablas(host, user, password, schema_name)
                print('')
                input('Presiona "ENTER" para continuar')

        elif seleccion == '4':
                os.system("clear")
                menu.logo_inicio()
                print('--------------------------------------------------------------------------')
                print('')

                try:
                        print(f'Quieres introducir los datos del archivo guardado en {url_clean_data} ?')
                        print('')
                        yon= (input('Selecciona Y (Yes) o N (No) y presiona "ENTER": ')).upper()
                        print('')
                except:
                        yon = 'N'
                
                if yon == 'Y':
                        url_datos=url_clean_data
                elif yon == 'N':
                        print('')
                        print('* Introduce la dirección del archivo dónde tienes los datos:')
                        print('')
                        url_datos=input('')   
                        print('')   

                try:
                        connection = mysql.connector.connect(host=host, user=user, password=password, database=schema_name)
                        df = pd.read_csv(url_datos)   
                        for tabla in ['Employee', 'Human_Resources', 'Finance', 'Job_Benefits', 'Surveys']:
                                cdd.insertar_datos_tabla(df, connection, tabla)
                        print('')
                        input('Presiona "ENTER" para continuar')        


                except:
                        url_datos=()
                        print('!!! No hay una Base de datos creada o el fichero no tiene el formato correcto !!!')
                        print('')
                        print(f'                      \N{raised back of hand}   \N{raised back of hand}   \N{raised back of hand}   \N{raised back of hand}   \N{raised back of hand}')
                        print('')
                        print('- El archivo tiene que ser de formato ".csv".')
                        print('- Antes de cargar los datos debes de crear una Base de Datos seleccionando la OPCIÓN 3 del menú de inicio.')
                        print('')
                        input('Presiona "ENTER" para continuar')              

        elif seleccion == '5':
                print("")
                print('')
                print('   Gracias y hasta pronto')
                print('')
                print("         \N{slightly smiling face} \N{slightly smiling face} \N{slightly smiling face} \N{slightly smiling face} \N{slightly smiling face}")
                print('')
                input('Presiona "ENTER" para continuar')
                exit()

        else:
                print('')
                print('')
                print('!!! Esa opcion no es valida ¡¡¡')
                print('')
                print('       \N{neutral face}','\N{neutral face}','\N{neutral face}','\N{neutral face}','\N{neutral face}')
                print('')
                input('Presiona "ENTER" para continuar')
                continue
         

