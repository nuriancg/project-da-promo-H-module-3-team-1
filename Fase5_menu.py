#Importamos librerias
import matplotlib.pyplot as plt
from skimage import io
import os

# Importamos librerias para crear logo
from pyfiglet import figlet_format
from termcolor import colored
from colorama import init

#Creamos una función que crea nuestro logo
def logo_inicio():

    """
    Esta función crea un logo que se va a visualizar en la terminal.

    Parameters:
    -----------------
    n/a

    Returns:
    ------------
    n/a
    """
        
    os.system("clear")

    # Renderiza "DATA" en 'color'
    data_texto = figlet_format('DATA', font='starwars', justify='center')
    data_colorido = colored(data_texto, 'magenta')
   
    # Renderiza "GADGETS" en blanco
    gadgets_texto = figlet_format('GADGETS', font='starwars', justify='center')
    gadgets_colorido = colored(gadgets_texto, 'magenta')
    print("     \N{face with monocle}        \N{face with monocle}        \N{face with monocle}        \N{face with monocle}         \N{face with monocle}         \N{face with monocle}         \N{face with monocle}")
    print('')
    print(data_colorido)
    print(gadgets_colorido)
    print("     \N{face with monocle}        \N{face with monocle}        \N{face with monocle}        \N{face with monocle}         \N{face with monocle}         \N{face with monocle}         \N{face with monocle}")
    print('')

#Definimos el menú
def menu():

    """
    Esta función muestra el menú.

    Parameters:
    -----------------
    n/a

    Returns:
    ------------
    seleccion (str): El input en formato str
    """

    #limpiamos la pantalla

    print("   MENÚ:")
    print("  -------")
    print("")
    print("  1. Extracción de Datos")
    print("  2. Transformación de Datos")
    print("  3. Creación de la Base de Datos")
    print('  4. Carga de Datos')
    print("")
    print("  5. Salir")
    print("")
    print("")
    print("================================================")

    seleccion=input(f'Elige una de las opciones (1,2,3,4 o 5 salir) -> ')
    
    return seleccion