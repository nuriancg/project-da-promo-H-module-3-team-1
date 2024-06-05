# Importamos librerias
import pandas as pd
import numpy as np

import re

from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer

# Librerías de visualización
# -----------------------------------------------------------------------
import seaborn as sns
import matplotlib.pyplot as plt

# Ajustes de visualización
pd.set_option('display.max_columns',None)
#pd.set_option('display.max_rows',None)


## Definimos las funciones

# Leemos el .csv 
def leer_fichero(url):
    
    df_original = pd.read_csv(url, index_col=0)

    return df_original

# Cambiamos los nombres de las columnas
def cambiar_nombre_col(data):
     
    def normalizar_encabezados(encabezado):
        # Mapeo para palabras completamente en mayúsculas pq no encuentro patrón para dividir.
        casos_especiales = {
            'NUMCOMPANIESWORKED': 'Num_Companies_Worked',
            'TOTALWORKINGYEARS': 'Total_Working_Years',
            'YEARSWITHCURRMANAGER': 'Years_With_Curr_Manager',
            'NUMBERCHILDREN': 'Number_Children', # Añado otros casos especiales, Los pongo en mayúsculas para que los trate trate igual a los anteriores.
            'EMPLOYEECOUNT': 'Employee_Count',
            'EMPLOYEENUMBER': 'Employee_Number',
            'WORKLIFEBALANCE': 'Work_Life_Balance'
        }

        # Si el encabezado está en casos especiales devolver el formato dado.
        if encabezado.upper() in casos_especiales:
            return casos_especiales[encabezado.upper()]

        # Añadir guion bajo entre letras y números
        encabezado = re.sub(r'([a-zA-Z])(\d)', r'\1_\2', encabezado)

        # Para formatos que incluyen transiciones de minúscula a mayúscula
        if re.match(r'^[A-Za-z0-9]+$', encabezado):  # Si son letras seguidas de números sin guiones
            encabezado = re.sub(r'([a-z])([A-Z])', r'\1_\2', encabezado)
            encabezado = re.sub(r'([A-Z]+)([A-Z][a-z]+)', r'\1_\2', encabezado)

    # Capitalizar cada string separado por guiones
        palabras = encabezado.split('_')
        return '_'.join(word.capitalize() for word in palabras)

    data.columns = [normalizar_encabezados(columna) for columna in data.columns]
    return data

# Eliminar columnas
def eliminar_columnas(data, lista_col):
    for col in lista_col:
        data.drop(col, axis=1, inplace=True)

    return data

# Crear columnas nuevas
def crear_columnas(data, *lista_col):
    for col in lista_col:
        data.insert(1,'Age_Group', ' ')

    return data

# Convertir a str
def to_string(data, lista_col):
    
    for col in lista_col:
        data[col] = data[col].astype(str)

    return data

# Cambio de ',0' por ''
def to_no_coma(data, lista_col):
    for col in lista_col:
        data[col] = data[col].str.replace(',0','')
    return data

# Booleanos
def to_bool(data,lista_col):
    dict_booleanos = {'1':True, 
                    'Yes':True, 
                    'True':True, 
                    '0':False, 
                    'No':False,
                    'False':False}


    for col in lista_col:
        data[col] = data[col].replace(dict_booleanos)

    return data

# Otros cambios
def limp_otros(data,lista_col):

    for col in lista_col:

        if col == 'Age':
            reemplazos = {
                'forty-seven': 47,
                'fifty-eight': 58,
                'thirty-six': 36,
                'fifty-five': 55,
                'fifty-two': 52,
                'thirty-one': 31,
                'thirty': 30,
                'twenty-six': 26,
                'thirty-seven': 37,
                'thirty-two': 32,
                'twenty-four': 24
            }
            data[col] = data[col].replace(reemplazos)

        elif col == 'Business_Travel':
            data[col] = data[col].str.replace('-',' ').str.replace('_',' ')

        elif col == 'Daily_Rate':
            data[col] = data[col].str.replace('$', '')

        elif col == 'Department':
            data[col]=data[col].str.strip()
            
            for index, row in data.iterrows():
                job_role = row['Job_Role'].strip().lower()
                if job_role == 'sales executive':
                    data.loc[index, col] = 'Sales'
                if job_role == 'human resourses':
                    data.loc[index, col] = 'Human Resources'
                if job_role == 'research director'  or job_role == 'manufacturing director' or job_role == 'laboratory technician'or job_role == 'research scientist'or job_role == 'healthcare representative':
                    data.loc[index, col] = 'Research & Development'

        elif col == 'Distance_From_Home':
            data[col] = data[col].str.replace('-', '')

        elif col == 'Environment_Satisfaction':
            for index, row in data.iterrows():
                numero = int(row[col])
                if numero < 10 and numero not in [2, 3, 4]:
                    data.loc[index, col] = 1
                elif 10 <= numero <= 20:
                    data.loc[index, col] = 2
                elif 20 < numero <= 30:
                    data.loc[index, col] = 3
                elif 30 < numero <= 49:
                    data.loc[index, col] = 4

        elif col == 'Gender':
            data[col] = data[col].replace({'0': 'M', '1': 'F'})

        elif col == 'Marital_Status':
            data[col] = data[col].replace({'Marreid':'Married'})

        else:
            data[col] = data[col] / 100

    return data

# Str a .title()
def to_title(data,lista_col):
    for col in lista_col:
        data[col] = data[col].str.title()

    return data

# Cambio de nulos str a 99999
def to_int_nulos(data,lista_col):
    for col in lista_col:
        data[col]=data[col].replace({'nan':99999,'NaN':99999, 'Not Available':99999})

    return data

# CAmbio a formato deseado
# Cambio a int
def to_int(data,lista_col):
    for col in lista_col:
        data[col] = data[col].astype(int)
    return data

# Cambio a bool
def to_bool(data,lista_col):
    for col in lista_col:
        data[col] = data[col].astype(bool)
    return data

# Reemplazar nulos
# int con .median()
def to_median(data,lista_col):
    for col in lista_col:
        data[col]=data[col].replace({99999:np.nan})
        data[col] = data[col].fillna(data[col].median()).astype(int)

    return data

# int con .mean()
def to_mean(data,lista_col):
    for col in lista_col:
        data[col]=data[col].replace({99999:np.nan})
        data[col] = data[col].fillna(data[col].mean()).astype(int)
    return data

# Categorigos a 'Unknown'
def reemplazar_nulos_por_unknown(data, lista_col):
    for columna in lista_col:
        data[columna] = data[columna].replace({'nan':None,'Nan':None})
        data[columna].fillna('Unknown', inplace=True)
    return data

# Rellenar nuevas columnas
# Columna 'Age_Group'
def age_group(data, col):

    rangos_edad = ['18-25', '26-35', '36-45', '46-55', '56-65']
    limites = [18, 26, 36, 46, 56, 66] # define los límites de cada grupo de edad, donde cada límite es exclusivo del grupo siguiente (excepto el último).


    data[col] = pd.cut(data['Age'], bins=limites, labels=rangos_edad, right=False)
    return data

# Columna Satisfaction_Group
def asignar_grupo(data, job_satisfaction):
    for index, row in data.iterrows():
        if row[job_satisfaction] >= 3:
            data.loc[index,'Satisfaction_Group']= 'A'
        else:
            data.loc[index,'Satisfaction_Group']= 'B'
    return data

# Eliminar duplicados
def eliminar_duplicados (data,subset):

    data.drop_duplicates(subset=subset,keep='last',inplace=True)

    return data

def eliminar_por_index (data, lista_index):
    for employee in lista_index:
        data.drop(employee,axis=0,inplace=True)

    return data

# Cambio employee number
def cambio_employee_num (data):
    lista_employee_number = data['Employee_Number'].unique().tolist()
    lista_employee_number.sort()
    lista_employee_number.remove(99999)
    
    new_employee_number = (lista_employee_number[-1]) + 1

    indices = data.index[data['Employee_Number'] == 99999]

    #Iteramos con un for loop por la lista de índices y cambiamos el valor del 'Employee_Number' por el nuevo valor
    for i in indices:
        data.loc[i, 'Employee_Number'] = new_employee_number
        new_employee_number += 1

    return data

# Set columna como index
def set_col_index (data, col):
    data.set_index(col,drop=True,inplace=True)

    return data

#Guardamos el DF en formato .csv
def guardar_fichero(data, url):
    
    data.to_csv(url, index=True)
    print(f'Archivo guardado en {url}')














