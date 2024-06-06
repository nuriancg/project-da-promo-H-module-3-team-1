#Importamos librerias
import matplotlib.pyplot as plt
from skimage import io
import os


#Introducimos nuestro logo
def logo_inicio():
    os.system("clear")
    logo=io.imread("logo.jpeg")/255.0
    print(logo.shape)
    print("\N{face with monocle} \N{face with monocle} \N{face with monocle} \N{face with monocle} \N{face with monocle}")
    print('')
    plt.imshow(logo, vmin=0,vmax=1)

#Definimos el menú
def menu():

    #limpiamos la pantalla

    print("     MENÚ:")
    print("    ------")
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

    seleccion=int(input(f'Elige una de las opciones (1,2,3,4 o 5 salir) -> '))
    
    return seleccion