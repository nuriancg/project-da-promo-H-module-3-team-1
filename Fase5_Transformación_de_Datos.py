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

    """
    Esta función abre un fichero .csv a partir de la dirección (url) especificad y genera un DataFrame.

    Parameters:
    -----------------
    url (str): String con la dirección del fichero .csv que queremos abrir.

    Returns:
    ------------
    df_original (DataFrame): El fichero en formato DataFrame
    """
    
    df_original = pd.read_csv(url, index_col=0)

    print('\N{floppy disk}','Tu fichero se ha almacenado corerctamente en la memória virtual.')
    return df_original


# Cambiamos los nombres de las columnas
def cambiar_nombre_col(data):

    """
    Esta función modifica los nombres de todas las columnas para que queden en formato Xxxx_Xxxx.

    Parameters:
    -----------------
    data (DataFrame): El DataFrame al que le queremos modificar los nombres de las columnas.

    Returns:
    ------------
    returns: data (DataFrame).
    """
        
    def normalizar_encabezados(encabezado):

        """
        Esta función modifica el formato del texto para que quede en formato Xxxx_Xxxx.

        Parameters:
        -----------------
        encabezado (str): El texto al que le queremos cambiar el formato.

        Returns:
        ------------
        encabezado: El texto con el formato cambiado.
        """

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


def transformacion_datos(data):


    """
    Esta función modifica el DataFrame (data) y lo prepara para poder crear una BBDD.

    Parameters:
    -----------------
    data (DataFrame): El DataFrame a modificar.

    Returns:
    ------------
    data: El DataFrame modificado.
    """


    # llamamos a la función que cambia los nombres de las columnas
    data = cambiar_nombre_col(data)

    #Creamos una lista con las columnas a eliminar
    lista_col_eliminar=['Employee_Count','Monthly_Income','Over_18','Years_In_Current_Role','Same_As_Monthly_Income','Salary', 'Standard_Hours','Role_Departament', 'Number_Children']
    
    def eliminar_columnas(data, lista_col):

        """
        Esta función elimina columnas (lista_col) de un DataFrame (data).

        Parameters:
        -----------------
        data (DataFrame): El DataFrame al que le queremos eliminar columnas.
        lista_col (lista): Lista de strings con el nombre de las columnas que queremos eliminar.

        Returns:
        ------------
        data: El DataFrame modificado.
        """

        for col in lista_col:
            data.drop(col, axis=1, inplace=True)

        return data

    # Llamamos a la función que elimina las columnas
    data = eliminar_columnas(data,lista_col_eliminar)

    #Creamos una lista con el nombre de las columnas nuevas que queremos creear
    lista_col_crear = ['Age_Group', 'Satisfaction_Group']
    
    def crear_columnas(data, *lista_col):

        """
        Esta función crea/añade columnas (lista_col) en un DataFrame (data).

        Parameters:
        -----------------
        data (DataFrame): El DataFrame al que le queremos añadir columnas.
        lista_col (lista): Lista de strings con el nombre de las columnas que queremos añadir.

        Returns:
        ------------
        data: El DataFrame modificado.
        """
       
        for col in lista_col:
            data.insert(1,'Age_Group', ' ')

        return data
    
    # Llamamos a la funcion que crea columnas nuevas
    data = crear_columnas(data, lista_col_crear)

    # Creamos una lista con el nombre de las columnas que queremos convertir a str
    lista_col_to_str=['Daily_Rate','Department','Education_Field','Employee_Number','Distance_From_Home','Environment_Satisfaction','Gender','Performance_Rating','Remote_Work','Total_Working_Years','Work_Life_Balance' ]
    
    def to_string(data, lista_col):

        """
        Esta función cambia el tipo de datos de una columna a string (str).

        Parameters:
        -----------------
        data (DataFrame): El DataFrame que queremos modificar.
        lista_col (lista): Lista de strings con el nombre de las columnas que queremos modificar.

        Returns:
        ------------
        data: El DataFrame modificado.
        """
        
        for col in lista_col:
            data[col] = data[col].astype(str)

        return data

    # Llamamos a la funcion que convierte los datos de una columna a string
    data = to_string(data,lista_col_to_str)

    # Creamos una lista con el nombre de las columnas que queremos cambior de ',0' por ''
    lista_col_to_no_coma=['Daily_Rate','Employee_Number','Performance_Rating','Total_Working_Years','Work_Life_Balance']

    def to_no_coma(data, lista_col):

        """
        Esta función elimina los ',0' de los valores de la columa especificada en un DataFrame (data). 
        El formato de los valores en la columna a modificar tienen que ser string (str).

        Parameters:
        -----------------
        data (DataFrame): El DataFrame que queremos modificar.
        lista_col (lista): Lista de strings con el nombre de las columnas que queremos modificar.

        Returns:
        ------------
        data: El DataFrame modificado.
        """
        
        for col in lista_col:
            data[col] = data[col].str.replace(',0','')
        return data

    # Llamamos a la función que elimina el ',0'
    data = to_no_coma(data,lista_col_to_no_coma)

    # Creamos una lista con el nombre de las columnas que queremos cambiar a booleanos
    lista_col_to_booleanos = ['Attrition', 'Over_Time','Remote_Work']

    def to_bool(data,lista_col):

        """
        Esta función modifica los datos de una columna de tipo booleano (bool) de un DataFrame (data).

        Parameters:
        -----------------
        data (DataFrame): El DataFrame que queremos modificar.
        lista_col (lista): Lista de strings con el nombre de las columnas que queremos modificar.

        Returns:
        ------------
        data: El DataFrame modificado.
        """

        dict_booleanos = {'1':True, 
                        'Yes':True, 
                        'True':True, 
                        '0':False, 
                        'No':False,
                        'False':False}


        for col in lista_col:
            data[col] = data[col].replace(dict_booleanos)

        return data
    
    # Llamamos a la funcion que cambia el dtype de las columnas a booleanos
    data = to_bool(data,lista_col_to_booleanos)

    # Creamos una lista con el nombre de las columnas a las que les queremos realizar otros cambios
    lista_col_otros = ['Age','Business_Travel','Daily_Rate', 'Department','Distance_From_Home','Environment_Satisfaction','Gender','Marital_Status','Percent_Salary_Hike']

    def limp_otros(data,lista_col):

        """
        Esta función realiza cambios varios a las columnas especificadas en un DataFrame (data).

        Parameters:
        -----------------
        data (DataFrame): El DataFrame que queremos modificar.
        lista_col (lista): Lista de strings con el nombre de las columnas que queremos modificar.

        Returns:
        ------------
        data: El DataFrame modificado.
        """

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
    
    # Llamamos a la funcion que realiza cambios varios a los valores de las columnas.
    data = limp_otros(data,lista_col_otros)

    # Creamos una lista con el nomnre de las columnas que queremos convertir a .title()
    lista_col_to_title = ['Business_Travel', 'Education_Field','Job_Role','Marital_Status']

    def to_title(data,lista_col):

        """
        Esta función modifica los valores de una columna que tenga formato string (str) y los modifica para que tengan las primeras letras en mayúscula.

        Parameters:
        -----------------
        data (DataFrame): El DataFrame que queremos modificar.
        lista_col (lista): Lista de strings con el nombre de las columnas que queremos modificar.

        Returns:
        ------------
        data: El DataFrame modificado.
        """
        
        for col in lista_col:
            data[col] = data[col].str.title()

        return data
    
    # Llamamos a la función que combierte las columnas a .title()
    data = to_title(data,lista_col_to_title)

    # Creamos una lista del nombre de las columnas en las que queremos cambiar los nulos str a 99999
    lista_col_int_nulos=['Daily_Rate','Employee_Number','Hourly_Rate','Performance_Rating','Total_Working_Years','Work_Life_Balance']

    def to_int_nulos(data,lista_col):

        """
        Esta función cambia los valores nulos de la columa especificada que este en formato string (str) en un DataFrame (data) y los reemplaza por '99999'.

        Parameters:
        -----------------
        data (DataFrame): El DataFrame que queremos modificar.
        lista_col (lista): Lista de strings con el nombre de las columnas que queremos modificar.

        Returns:
        ------------
        data: El DataFrame modificado.
        """

        for col in lista_col:
            data[col]=data[col].replace({'nan':99999,'NaN':99999, 'Not Available':99999})

        return data
    
    # Llamamos a la función que cabia los nulos por 99999
    data = to_int_nulos(data,lista_col_int_nulos)

    # CAmbio a formato deseado
    # Creamos una lista con el nombnre de las columnas que queremos cambiar a int
    lista_col_to_int=['Age','Daily_Rate','Distance_From_Home','Employee_Number','Environment_Satisfaction','Hourly_Rate','Job_Involvement','Monthly_Rate','Total_Working_Years','Performance_Rating','Work_Life_Balance']

    def to_int(data,lista_col):

        """
        Esta función cambia el tipo de datos de una columna a integer (int).

        Parameters:
        -----------------
        data (DataFrame): El DataFrame que queremos modificar.
        lista_col (lista): Lista de strings con el nombre de las columnas que queremos modificar.

        Returns:
        ------------
        data: El DataFrame modificado.
        """

        for col in lista_col:
            data[col] = data[col].astype(int)
        return data

    # Llamamos a la función que cambia las columnas a int
    data = to_int(data,lista_col_to_int)

    # Creamos una lista con los nombres de las columnas que queremos cambiar  a bool
    lista_col_to_bool=['Remote_Work']

    def to_bool(data,lista_col):

        """
        Esta función cambia el tipo de datos de una columna a booleano (bool).

        Parameters:
        -----------------
        data (DataFrame): El DataFrame que queremos modificar.
        lista_col (lista): Lista de strings con el nombre de las columnas que queremos modificar.

        Returns:
        ------------
        data: El DataFrame modificado.
        """

        for col in lista_col:
            data[col] = data[col].astype(bool)
        return data

    # Llamamos a la funcion que cambia los valores de la columna a bool
    data = to_bool(data,lista_col_to_bool)

    # Reemplazar nulos
    # Creamos una lista con los nombres de las columnas que queremos reemplazar los nulos int con .median()
    lista_col_median = ['Performance_Rating','Work_Life_Balance']

    def to_median(data,lista_col):

        """
        Esta función reemplaza los nulos de una columna que esta en formnato integer (int) por el valor de la mediana (median).

        Parameters:
        -----------------
        data (DataFrame): El DataFrame que queremos modificar.
        lista_col (lista): Lista de strings con el nombre de las columnas que queremos modificar.

        Returns:
        ------------
        data: El DataFrame modificado.
        """

        for col in lista_col:
            data[col]=data[col].replace({99999:np.nan})
            data[col] = data[col].fillna(data[col].median()).astype(int)

        return data

    # Llamamos a la funcion que reemplaza nulos int con .median()
    data = to_median(data,lista_col_median)

    # Creamos una lista con los nombres de las columnas que queremos reemplazar los nulos int con .mean()
    lista_col_mean = ['Total_Working_Years']

    def to_mean(data,lista_col):

        """
        Esta función reemplaza los nulos de una columna que esta en formnato integer (int) por el valor de la media (mean).

        Parameters:
        -----------------
        data (DataFrame): El DataFrame que queremos modificar.
        lista_col (lista): Lista de strings con el nombre de las columnas que queremos modificar.

        Returns:
        ------------
        data: El DataFrame modificado.
        """

        for col in lista_col:
            data[col]=data[col].replace({99999:np.nan})
            data[col] = data[col].fillna(data[col].mean()).astype(int)
        return data
    
    # Llamamos a la funcion que reeplaza nulos por .mean()
    data=to_mean(data,lista_col_mean)

    # Creamos una lista con el nombre de las columnas categoricas en las que queremos reemplazar los nulos por 'Unknown'
    lista_col_unknown =['Business_Travel','Department','Education_Field','Marital_Status','Over_Time']

    def reemplazar_nulos_por_unknown(data, lista_col):

        """
        Esta función reemplaza los nulos de una columna que esta en formnato object por el valor 'Unknown''.

        Parameters:
        -----------------
        data (DataFrame): El DataFrame que queremos modificar.
        lista_col (lista): Lista de strings con el nombre de las columnas que queremos modificar.

        Returns:
        ------------
        data: El DataFrame modificado.
        """

        for columna in lista_col:
            data[columna] = data[columna].replace({'nan':None,'Nan':None})
            data[columna].fillna('Unknown', inplace=True)
        return data
    
    # Llamamos a la funcion que reemplaza nulos por 'unknown'
    data = reemplazar_nulos_por_unknown(data, lista_col_unknown)

    # Rellenar nuevas columnas
    # columna 'Age_Group'
    def age_group(data, col):

        """
        Esta función introduce datos en la columa 'Age_Group'

        Parameters:
        -----------------
        data (DataFrame): El DataFrame que queremos modificar.
        col (str): String con el nombre de la columna que queremos modificar.

        Returns:
        ------------
        data: El DataFrame modificado.
        """

        rangos_edad = ['18-25', '26-35', '36-45', '46-55', '56-65']
        limites = [18, 26, 36, 46, 56, 66] # define los límites de cada grupo de edad, donde cada límite es exclusivo del grupo siguiente (excepto el último).


        data[col] = pd.cut(data['Age'], bins=limites, labels=rangos_edad, right=False)
        return data

    # Columna Satisfaction_Group
    def asignar_grupo(data, job_satisfaction):

        """
        Esta función introduce datos en la columa 'Job_Satisfaction'

        Parameters:
        -----------------
        data (DataFrame): El DataFrame que queremos modificar.
        job_satisfaction (str): String con el nombre de la columna que queremos modificar.

        Returns:
        ------------
        data: El DataFrame modificado.
        """

        for index, row in data.iterrows():
            if row[job_satisfaction] >= 3:
                data.loc[index,'Satisfaction_Group']= 'A'
            else:
                data.loc[index,'Satisfaction_Group']= 'B'
        return data

    # Llamamos a las funciones que introducin datos en las columnas nuevas
    data = age_group(data,'Age_Group')
    data = asignar_grupo(data, 'Job_Satisfaction')

    # Eliminar duplicados
    def eliminar_duplicados (data,subset):

        """
        Esta función elimina duplicados de un DataFrame (data) utilizando un subset formado por nombres de las columnas que queremos comparar.

        Parameters:
        -----------------
        data (DataFrame): El DataFrame que queremos modificar.
        subset (lista): Lista de strings con los nombres de la columnas que queremos comparar para ver si hay duplicados.

        Returns:
        ------------
        data: El DataFrame modificado.
        """

        data.drop_duplicates(subset=subset,keep='last',inplace=True)

        return data

    def eliminar_por_index (data, lista_index):

        """
        Esta función elimina duplicados de un DataFrame (data) utilizando una lista con los indices de las filas a eliminar (lista_index).

        Parameters:
        -----------------
        data (DataFrame): El DataFrame que queremos modificar.
        lista_index (lista): Lista de strings con los nombres de los índices de las filas que queremos eliminar.

        Returns:
        ------------
        data: El DataFrame modificado.
        """

        for employee in lista_index:
            data.drop(employee,axis=0,inplace=True)

        return data
    
    # Creamos un listado con el nombre de todas las columnas
    lista_col_names = set(data.columns.tolist())
    # Llamamos a la función que elimmina duplicados por subset
    data = eliminar_duplicados(data,lista_col_names)

    # Creamos un listado con el nombre de todas las columnas y le eliminamos 'Distance_From_Home'
    lista_columnas_2 = set(lista_col_names)
    lista_columnas_2.remove('Distance_From_Home')   
    # Llamamos a la función que elimina duplicados por subset
    data = eliminar_duplicados(data,lista_columnas_2)

    # Creamos un listado con el nombre de todas las columnas y eliminamos 'Remote Work'
    lista_columnas_3 = set(lista_col_names)
    lista_columnas_3.remove('Remote_Work')  
    # Llamamos a la función que elimina duplicados por subset
    data = eliminar_duplicados(data,lista_columnas_3)

    # Creamos un listado con el nombre de todas las columnas y eliminamos 'Distance_From_Home' y 'Remote Work'
    lista_columnas_4 = set(lista_col_names)
    lista_columnas_4.remove('Distance_From_Home')
    lista_columnas_4.remove('Remote_Work')
    # Llamamos a la función que elimina duplicados por subset
    data = eliminar_duplicados(data,lista_columnas_4)


    # Filrtamos el DF para obtener el DF dónde el 'Hourly_Rate'==99999 y el 'Employee_Number' != 999999
    data_duplicados_s5 = data[data['Employee_Number'].isin(data['Employee_Number'][data['Employee_Number'].duplicated() ])].sort_values('Employee_Number')
    data_duplicados_s5_filtrado = data_duplicados_s5[data_duplicados_s5['Hourly_Rate']==99999]
    data_duplicados_s5_filtrado = data_duplicados_s5_filtrado.loc[data_duplicados_s5_filtrado['Employee_Number']!=99999,:]
    # Guardamos en una lista los números de los índices de todas las filas del DF filtrado 'df_duplicados_s5_filtrado'
    lista_index_situacion_5= data_duplicados_s5_filtrado.index.tolist()
    # Llamamos a la función que elimina duplicados por indice
    data = eliminar_por_index(data, lista_index_situacion_5)

    # Filtramos el DF para obtener el DF dónde el 'Distance_From_Home' == 'Environment_Satisfaction' y el 'Employee_Number' != 999999
    data_duplicados_s6 = data[data['Employee_Number'].isin(data['Employee_Number'][data['Employee_Number'].duplicated() ])].sort_values('Employee_Number')
    data_duplicados_s6_filtrado = data_duplicados_s6[(data_duplicados_s6['Distance_From_Home']==data_duplicados_s6['Environment_Satisfaction'])]
    data_duplicados_s6_filtrado = data_duplicados_s6_filtrado.loc[data_duplicados_s6_filtrado['Employee_Number']!=99999,:]
    # Guardamos en una lista los números de los índices de todas las filas del DF filtrado 'df_duplicados_s6_filtrado'
    lista_index_situacion_6=data_duplicados_s6_filtrado.index.tolist()
    # Llamamos a la función que elimina duplicados por indice
    data = eliminar_por_index(data, lista_index_situacion_6)

    # Creamos un listado con el nombre de todas las columnas y eliminamos 'Distance_From_Home' y 'Environment_Satisfaction'
    lista_columnas_7 = set(lista_col_names)
    lista_columnas_7.remove('Distance_From_Home')
    lista_columnas_7.remove('Environment_Satisfaction')
    # Llamamos a la función que elimina duplicados por subset
    data=eliminar_duplicados(data, lista_columnas_7)

    # Creamos un listado con el nombre de todas las columnas y eliminamos 'Distance_From_Home', 'Environment_Satisfaction' y 'Remote_Work'
    lista_columnas_8 = set(lista_col_names)
    lista_columnas_8.remove('Distance_From_Home')
    lista_columnas_8.remove('Environment_Satisfaction')
    lista_columnas_8.remove('Remote_Work')
    # Llamamos a la función que elimina duplicados por subset
    data = eliminar_duplicados(data, lista_columnas_8)

    print(f' \N{check mark}',' Los datos se han transformado correctamente.')
    return data


# Cambio employee number
def cambio_employee_num (data):


    """
    Esta función reemplaza los valores '99999' en la columna 'Employee_Number' del DataFrame (data) por valores nuevos que se generan 
    a partir del valor más elevado de la columna 'Employee_Number'.

    Parameters:
    -----------------
    data (DataFrame): El DataFrame que queremos modificar.

    Returns:
    ------------
    data: El DataFrame modificado.
    """

    lista_employee_number = data['Employee_Number'].unique().tolist()
    lista_employee_number.sort()
    lista_employee_number.remove(99999)
        
    new_employee_number = (lista_employee_number[-1]) + 1

    indices = data.index[data['Employee_Number'] == 99999]

    #Iteramos con un for loop por la lista de índices y cambiamos el valor del 'Employee_Number' por el nuevo valor
    for i in indices:
        data.loc[i, 'Employee_Number'] = new_employee_number
        new_employee_number += 1

    # Set columna como index
    def set_col_index (data, col):

        """
        Esta función asigna una columna (col) como columna índice de un DataFrame (data).

        Parameters:
        -----------------
        data (DataFrame): El DataFrame que queremos modificar.
        subset (lista): Lista de strings con los nombres de la columnas que queremos comparar para ver si hay duplicados.

        Returns:
        ------------
        data: El DataFrame modificado.
        """

        data.set_index(col,drop=True,inplace=True)

        return data
    
    # Llamamos a la función que asigna una columna como columna índice
    data = set_col_index(data, 'Employee_Number')

    print(f' \N{check mark}',' Se han generado los "Employee Number" que faltaban correctamente.')
    return data


#Guardamos el DF en formato .csv
def guardar_fichero(data, url):

    """
    Esta función guarda un DataFrame (data) en la dirección (url) especificada en formato .csv.

    Parameters:
    -----------------
    data (DataFrame): El DataFrame que queremos guardar.
    url (str): String con la dirección dónde queremos guardar el DataFrame.

    Returns:
    ------------
    n/a
    """
    
    data.to_csv(url, index=True)
    print(f' \N{check mark}',f' Archivo guardado en {url}')














