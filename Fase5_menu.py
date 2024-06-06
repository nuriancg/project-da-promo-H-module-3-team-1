#Importamos librerias

import os


#Introducimos nuestro logo
def logo_inicio():
    os.system("clear")
    print('''LOGO''')

#Definimos el menú
def menu():

    #limpiamos la pantalla

    print("Menú")
    print("")
    print("  1. Creación_de_la_Base_de_Datos")
    print("  2. Extracción de Datos")
    # print("  3. Transformación_de_Datos")
    print('  4. Inserción de Datos')
    print("  5. Salir")
    print("")
    print("")

    print("================================================")

    seleccion=int(input(f"Elige una de las opciones (1,2,3,4 o 5 salir):  "))

    return seleccion