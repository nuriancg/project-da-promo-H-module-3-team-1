#Importamos librerias
import pandas as pd
import mysql.connector
from mysql.connector import Error

import os

#Importamos otros ficheros
import Fase5_menu as menu
import Fase5_Carga_de_Datos as cdd
import Fase5_Creación_de_la_Base_de_Datos as cbbdd
import Fase5_Extracción_de_Datos as edd
import Fase5_Transformación_de_Datos as tdd


menu.logo_inicio()
seleccion = menu.menu()

if seleccion == 3:

    url_raw_data=input(f'Introduce la dirección del archivo que quieres abrir:  ')

    url_raw_data='https://raw.githubusercontent.com/nuriancg/project-da-promo-H-module-3-team-1/master/HR_RAW_DATA.csv'
    tdd.leer_fichero(url_raw_data)