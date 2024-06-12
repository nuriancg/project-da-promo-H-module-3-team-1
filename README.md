**(_English information at the end of this page_)**


#  Optimización de Talento de ABC Corporation
      
_La Iniciativa de Optimización de Talento de ABC Corporation tiene como objetivo abordar diferentes aspectos relacionados con los recursos humanos de su empresa. Para ello, han contratado los servicios de nuestra empresa, Data Gadgets._

_**Data Gadgets** es una empresa formada por un grupo de analistas de datos que utilizamos metodología ágil para cumplir eficientemente con los objetivos propuestos en tiempo récord._

## Equipo Data Gatgets: 📈🔍

|Names|GitHub_link_user_name|
|-----|------------------|
|_Patricia González_|https://github.com/Patri-EGG|
|_Paola Sánchez_|https://github.com/paolasanchezsolorzano|
|_Fernanda Marti_|https://github.com/fernandaMarti|
|_Nuria Cano_| https://github.com/nuriancg|
|_Raquel Castellanos_|https://github.com/RachelCaste|


## Descripción del Cliente 👨‍💻

_ABC Corporation, fundada en 1980 en California, es una firma de consultoría tecnológica especializada en proporcionar soluciones de inteligencia artificial (IA) y aprendizaje automático a empresas de diversas industrias._

## Objetivo: 🎯
_Identificar factores clave que influyen en la satisfacción de sus empleados y, en última instancia, en la retención de los mismos. Presentar los resultados del análisis exploratorio de datos, diseñar un experimento A/B para probar hipótesis críticas y analizar los resultados para proporcionar a ABC Corporation información valiosa y veraz._

## Documentación Inicial 📌
_En esta sección, encontrarás la descripción de cada una de las columnas del documento original._

<details>
<summary> Diccionario:</summary>

| Nombre de la columna        | Descripción                                                                                  |
| ------------------- | --------------------------------------------------------------------------------------------- |
| Age                 | The employee’s age.                                                                           |
| Attrition           | Indicates whether the employee has left the company (“No” means they haven’t left, and “Yes” means they have). |
| BusinessTravel      | Describes the frequency of work-related travel for the employee (e.g., “Travel_Rarely” for infrequent travel). |
| DailyRate           | The employee’s daily rate.                                                                    |
| Department          | The department in which the employee works (e.g., “Research & Development,” “Sales,” etc.). |
| DistanceFromHome    | The distance from the employee’s home to their workplace.                                     |
| Education           | The employee’s education level (usually on a scale from 1 to 5).                               |
| EducationField      | The field of education or specialization for the employee.                                     |
| EmployeeCount       | A counter (usually set to 1) used for counting employees.                                      |
| EmployeeNumber      | A unique identification number for the employee.                                              |
| EnvironmentSatisfaction | Employee satisfaction level related to their work environment, ranging from 1 to 4 (with 4 being the highest satisfaction). |
| Gender              | The employee’s gender (where 0 corresponds to “male” and 1 to “female”).                        |
| HourlyRate          | The employee’s hourly rate.                                                                   |
| JobInvolvement      | The level of employee involvement in their work.                                               |
| JobLevel            | The employee’s hierarchical level within the company.                                          |
| JobRole             | The employee’s job role or position.                                                           |
| JobSatisfaction     | Employee satisfaction level with their job.                                                    |
| MaritalStatus       | The employee’s marital status (e.g., “Single,” “Married,” etc.).                                |
| MonthlyIncome       | The employee’s monthly income.                                                                 |
| MonthlyRate         | The employee’s monthly rate.                                                                   |
| NumCompaniesWorked  | The number of companies where the employee has worked.                                          |
| Over18              | Indicates whether the employee is over 18 years old.                                            |
| OverTime            | Indicates whether the employee works overtime (“Yes” or “No”).                                  |
| PercentSalaryHike   | The percentage of salary increase for the employee.                                             |
| PerformanceRating   | Employee performance rating.                                                                   |
| RelationshipSatisfaction | Employee satisfaction level in interpersonal relationships.                                   |
| StandardHours       | Standard working hours.                                                                        |
| StockOptionLevel    | Employee stock option level.                                                                    |
| TotalWorkingYears   | Total years of work experience for the employee.                                                |
| TrainingTimesLastYear | Number of times the employee received training last year.                                       |
| WorkLifeBalance     | Balance between work and personal life for the employee.                                         |
| YearsAtCompany      | Number of years the employee has worked at the current company.                                  |
| YearsInCurrentRole  | Number of years the employee has been in their current role.                                     |
</details>

## Fases del Proyecto 🔄

_Para completar el desarrollo de este proyecto y garantizar la integridad de los datos proporcionados por el cliente, se llevaron a cabo cinco fases:_

* **Fase 1: Exploración y Limpieza de Datos**
* **Fase 2: Transformación de Datos**
* **Fase 3: Diseño e Implementación de la Base de Datos**
* **Fase 4: Pruebas A/B**
* **Fase 5: Creación de ETL (Extracción, Transformación y Carga)**
* **Fase 6: Generación de Informes**




## Requisitos para Ejecutar el Proyecto 🐍 y 🐬
_Para trabajar o abrir este proyecto, necesitarás tener instaladas versiones de Python y MySQL._

##  Librerías a Importar: 📚

<details>
<summary>Librerías para comenzar a trabajar:</summary>

1. **Manipulación de Datos** 🧮 🐼
   - **Pandas**
   - **Numpy**

2. **Imputación de datos** 🕵️‍♂️
   - Scikit-learn
     -**SimpleImputer:** _Imputa valores faltantes en un conjunto de datos utilizando estrategias simples como la media, la mediana o la moda, entre             otras._
     -**IterativeImputer:** _Utiliza técnicas iterativas, especialmente útiles cuando las relaciones entre variables son complejas._
     -**KNNImputer:** _Estima valores faltantes utilizando el método de los vecinos más cercanos (K-Nearest Neighbors)._
       
3. **Visualización de datos** 📊
   -**Seaborn**: _Proporciona una interfaz de alto nivel para crear gráficos estadísticos atractivos e informativos._
   -**Matplotlib**: _Es una biblioteca de visualización de datos en Python que permite crear gráficos estáticos de alta calidad adecuados para publicaciones e informes._

4. **Estadísticas y Pruebas** 🧪
-**Scipy:** _Proporciona funciones estadísticas y pruebas de hipótesis (por ejemplo, pruebas t, pruebas de chi-cuadrado, etc.)_
   
5. **Conexión a la Base de Datos** ⚡
-**mysql.connector:** _Conector para MySQL que permite establecer conexiones y realizar operaciones en bases de datos MySQL desde Python._

</details>

## Estructura de la Base de Datos 📁

_En este repositorio encontrarás una estructura en forma de estrella, que simplifica las consultas analíticas y es útil para el análisis de grandes volúmenes de datos._

<details>
  <summary>Estructura</summary>
  <img src='https://github.com/nuriancg/project-da-promo-H-module-3-team-1/blob/master/Imagenes/Diagrama%20BBDD.png' alt="Diagrama BBDD">
</details>

## Descripción de la Información en la Base de Datos Final 📌

_En este desplegable, encontrarás la descripción y distribución de cada una de las columnas del documento final._ 😊


  <details>
<summary> Diccionario:</summary>

| Nombre de la columna         | Descripción                                                                                 |
| ------------------- | --------------------------------------------------------------------------------------------- |
| Age                 | The employee’s age.                                                                           |
| Age_Group           |Referring to categorizing employees based on their age range. There are five labels: (18-25), (26-35), (36-45), (45-55) and (56-65).|
|Attrition|Indicates whether the employee has left the company (“False” means they haven’t left, and “True” means they have).|
Business_Travel|Describes the frequency of work-related travel for the employee (e.g., “Travel_Rarely” for infrequent travel).|
Daily_Rate|The employee’s daily rate.|
Department|The department in which the employee works.|
Distance_From_Home|The distance from the employee’s home to their workplace.|
Education|The employee’s education level.(On a scale from 1 to 5)|
Education_Field|The field of education or specialization for the employee.|
Employee_Number|A unique identification number for the employee.|
Environment_Satisfaction|Employee satisfaction level related to their work environment.( Ranging from 1 to 4, with 4 being the highest satisfaction)|
Gender|The employee’s gender.(Where ‘M’ corresponds to “male” and ‘F’ to “female”).|
Hourly_Rate|The employee’s hourly rate.|
Job_Involvement|The level of employee involvement in their work.(On scale from 1 to 5).|
Job_Level|The employee’s hierarchical level within the company, (On scale from 1 to 5).|
Job_Role1|The employee’s position.|
Job_Satisfaction|Employee satisfaction level with their job.(Ranging from 1 to 4, with 4 being the highest satisfaction).|
Marital_Status|The employee’s marital status.(Accepts these values ‘Married’, ’Divorced’, and 'Unknown').|
Monthly_Rate| The employee’s monthly rate.|
Num_Companies_Worked|The number of companies where the employee has worked.|
Over_Time|Indicates whether the employee works overtime.(Accepts these values “True”,  “False” and 'Unknown').|
Percent_Salary_Hike1|The percentage of salary increase for the employee.(Accepts values between 0 - 1)|
Performance_Rating|Employee performance rating.(On scale from 1 to 5).|
Relationship_Satisfaction| Employee satisfaction level in interpersonal relationships.(On scale from 1 to 5).|
Stock_Option_Level|Employee stock option level.(On a scale from 0 to 4).|
Total_Working_Years|Total years of work experience for the employee.|
Training_Times_Last_Year|Number of times the employee received training last year.|
Work_Life_Balance|Balance between work and personal life for the employee.(On scale from 1 to 5).|
Years_At_Company|Number of years the employee has worked at the current company.|
Years_Since_Last_Promotion|Years since the employee’s last promotion.|
Years_With_Curr_Manager|Years under the supervision of the current manager.|
Date_Birth|The employee’s birth year. (considering data collected in 2023).|
RemoteWork| Whether the employee can work remotely or not.|

</details>

## Resolución del Objetivo  🎯🎯


* _Para abordar nuestro objetivo, se llevó a cabo un análisis estadístico con el propósito de determinar si existe una diferencia significativa en la tasa de rotación de los empleados según su nivel de satisfacción en la empresa. Para ello, se dividió a los empleados en dos grupos según su nivel de satisfacción, y posteriormente se calculó la tasa de rotación para cada uno de estos grupos._

  
|Grupo|Categoría|Descripción|
|------------------------|--------------------------------------------------------------------------|-------------------|
|Grupo A| Satisfechos| Empleados con un nivel de satisfacción en el trabajo igual o superior a 3 en una escala de 1 a 5.|
|Grupo B |Descontentos|Empleados con un nivel de satisfacción en el trabajo inferior a 3 en una escala de 1 a 5.|



* ### _Se establecieron dos hipótesis:_
  

 | _Hipótesis_|_Descripción_|
 |------------------------|--------------------------------------------------------------------------| 
|_Hipótesis Nula (H0)_| _Afirmamos que no hay diferencia; la tasa de rotación no afecta al nivel de satisfacción._|
|_Hipótesis Alternativa (H1)_|_Afirmamos que sí hay diferencia, el nivel de satisfacción afecta significativamente a la tasa de rotación._|


* ### Test: 📈📝

|_Tipo de prueba_| _Descripción_|
 |--------------------|---------|
 |ttest_ind()| _Es una prueba estadística que se utiliza para comparar dos grupos y determinar si hay una diferencia significativa entre ellos en términos de una variable que estamos midiendo._|
|ztest()| _Indica si el resultado observado está lejos del valor esperado bajo la hipótesis nula mediante la desviación estándar._| 
|chi2()|_La prueba chi cuadrado se utiliza para determinar el comportamiento de cierta variable y también para evaluar si dos o más variables son estadísticamente independientes_|



<details>
<summary> Analisis completo Tasa de Rotación</summary>

_De toda la información que tenemos, extraemos la tasa de rotación. Es el indicador que mide la frecuencia con la que los empleados dejan la organización y son reemplazados por otros nuevos en el período de tiempo del que tenemos datos.**._

- _La tasa de rotación en el Grupo A (con una satisfacción media y alta) es de 0.16%._
- _La tasa de rotación en el Grupo B(satisfaccion baja) es de 0.24%._
  
**Según estos datos, vemos que el descontento o la insatisfacción laboral está asociada con una mayor propensión a dejar la empresa.**


  <img src='https://github.com/nuriancg/project-da-promo-H-module-3-team-1/blob/master/Imagenes/tasa%20de%20rotacion%20segun%20el%20nivel%20de%20satisfaccion.png' alt="Gráfico Tasas de Rotación">

  
### Test:_📈📝


_Realizamos diferentes test para comparar nuestros dos grupos y seguir explorando si hay una diferencia significativa o no en la tasa de rotación según la satisfacción._

*  **El t-test de Student:**
  
      - _Con p_value de: (0.004),  indica que SÍ hay diferencia significativa entre los dos grupos. Por lo tanto, en este estudio se rechaza la H0._

    
* **Z-test:**
     - _Con un stadistic de -2.94 y un p-value de 0.0032. Indica que la proporción de personas que dejaron la empresa en el Grupo A (empleados satisfechos) es menor que en el Grupo B (empleados descontentos). Esto refuerza la idea de que una mayor satisfacción laboral está asociada con una menor rotación de empleados. Así que de nuevo se rechaza la H0. Este valor es negativo, lo que indica que la proporción de personas que dejaron la empresa en el Grupo A (empleados satisfechos) es menor que en el Grupo B (empleados descontentos). El valor absoluto que es mayor que 2 sugiere que la diferencia es significativa, pero la dirección de la diferencia es contraria a la del incremento numérico en los datos (es decir, hay menos rotación donde podríamos esperar más, o viceversa)._


* **Chi2 test**:
     - _Chi-squared Test Statistic: con un valor de 8.2479 y un p-value: 0.0041, que nos indica nuevamente que existe una diferencia significativa en los niveles de satisfacción y la tasa de rotación. Hay evidencia suficiente para rechazar la hipótesisi nula._
 
## _Pruebas adicionales_

Llevamos a cabo nuevas pruebas para conocer en mayor profundidad las razones por las que hay empleados descontentos. 

Buscamos la corelación entre nuestras diferentes variables, y extraemos las siguientes conclusiones:

1. _A más nivel de desempeño, más aumenta el porcentaje de subida de los salarios. Es señal de prácticas saludables de la empresa, que recompensan a los empleados que se esfuerzan y sacan el trabajo adelante._

_Como se puede apreciar en la siguiente gráfica, la presencia de outliers en ambos valores (3 y 4), más notorios en el 3, denotan ciertas excepciones en la política de aumento de salario de la empresa para los empleados que tienen un nivel de desempeño medio. Esto podría ser un tema que despertase diferentes sentimientos entre los empleados, por lo que podría ser interesante realizar estudios al respecto. 
En base a ambas conclusiones, por ahora no podemos establecer motivos de descontento._

  <img src='https://github.com/nuriancg/project-da-promo-H-module-3-team-1/blob/master/Imagenes/relacion%20desempe%C3%B1o%20y%20aumento%20de%20sueldo.png' alt="Relación entre desempeño y aumento de sueldo">

 
  2. _A más años trabajados, más aumenta el cargo de las personas empleadas. Lo que indica que la empresa promociona a sus personas trabajadoras a medida que pasa el tiempo. Esto también es una buena práctica y no se puede asociar con un motivo de descontento._

  <img src='https://github.com/nuriancg/project-da-promo-H-module-3-team-1/blob/master/Imagenes/4%20Graficas.png' alt="diferentes graficas">

3.  _A más años trabajados y a más años en la empresa, más años con el/la actual manager. Esto podría indicar que los/las managers mantienen su puesto de trabajo, es decir que hay cierta estabilidad. En principio también podría considerarse una buena práctica de la empresa, aunque podría estudiarse en mayor profundidad. No encontramos motivos de descontento._

    <img src='https://github.com/nuriancg/project-da-promo-H-module-3-team-1/blob/master/Imagenes/Relaci%C3%B3n%20a%C3%B1os%20en%20la%20compa%C3%B1ia%20y%20con%20actual%20manager.png' alt="Relación entre años en la compañia y años con actual manager">


4.  _A más edad, más experiencia en diferentes empresas. Los empleados entre 40 y 44 años han trabajado en más empresas que los empleados más jóvenes que ellos. Esto tiene sentido y no debería ser motivo de descontento._

<img src='https://github.com/nuriancg/project-da-promo-H-module-3-team-1/blob/master/Imagenes/relacion%20entre%20edad%20y%20total%20empresas%20trabajadas.png' alt="Relación entre edad y total de empresas en las que ha trabajado"> 

5.  _A más estudios, mayor cargo en la empresa. Esto también tiene sentido y no debería ser un problema para los empleados/as._

<img src='https://github.com/nuriancg/project-da-promo-H-module-3-team-1/blob/master/Imagenes/Relacion%20entreb%20estudio%20y%20nivel%20jer%C3%A1rquico.png' alt="Relación entre estudios y nivel jerárquico"> 
   
</details>
   
## Conclusión: ✅

_Basándonos en los resultados obtenidos, podemos inferir que la empresa implementa prácticas favorables hacia sus empleados, como aumentos salariales o ascensos. Sin embargo, el descontento de los empleados podría estar relacionado con otras variables que no se han estudiado en la actualidad._

_Por lo tanto, recomendamos llevar a cabo encuestas dirigidas a los empleados, permitiéndoles expresar los motivos de su insatisfacción. Esto proporcionaría una visión más completa y ayudaría a abordar cualquier problema subyacente de manera efectiva_



_______________________________________________________________________________________________________________________________________

<details>
   
<summary> English </summary>

# ABC Corporation's Talent Optimization!!!

_ABC Corporation's Talent Optimization Initiative aims to respond to different aspects related to the human resources of their company. For which he has hired the services of our company Data Gatgets._

_**Data Gatgets** is a company formed by a group of data analysts who use agile methodology to meet each proposed objective efficiently and in record time._

### Data Gatgets Team: 📈🔍

|Names|GitHub_link_user_name|
|-----|------------------|
|_Patricia González_|https://github.com/Patri-EGG|
|_Paola Sánchez_|https://github.com/paolasanchezsolorzano|
|_Fernanda Martí_|https://github.com/fernandaMarti|
|_Nuria Cano_| https://github.com/nuriancg|
|_Raquel Castellanos_|https://github.com/RachelCaste|


### Client Description: 👨‍💻

_ABC Corporation, founded in 1980 in California, is a technology consulting firm specializing in providing artificial intelligence (AI) and machine learning solutions to companies in various industries._

### Target: 🎯

_Present the results of exploratory data analysis, design an A/B experiment to test critical hypotheses, and analyze the results to provide ABC Corporation with valuable and truthful information._

### Initial Documentation: 📌

_In this dropdown, you will find the description of each of the columns of the original document._  😊


<details>
<summary> Dictionary:</summary>

| Column_Name         | Description                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------- |
| Age                 | The employee’s age.                                                                           |
| Attrition           | Indicates whether the employee has left the company (“No” means they haven’t left, and “Yes” means they have). |
| BusinessTravel      | Describes the frequency of work-related travel for the employee (e.g., “Travel_Rarely” for infrequent travel). |
| DailyRate           | The employee’s daily rate.                                                                    |
| Department          | The department in which the employee works (e.g., “Research & Development,” “Sales,” etc.). |
| DistanceFromHome    | The distance from the employee’s home to their workplace.                                     |
| Education           | The employee’s education level (usually on a scale from 1 to 5).                               |
| EducationField      | The field of education or specialization for the employee.                                     |
| EmployeeCount       | A counter (usually set to 1) used for counting employees.                                      |
| EmployeeNumber      | A unique identification number for the employee.                                              |
| EnvironmentSatisfaction | Employee satisfaction level related to their work environment, ranging from 1 to 4 (with 4 being the highest satisfaction). |
| Gender              | The employee’s gender (where 0 corresponds to “male” and 1 to “female”).                        |
| HourlyRate          | The employee’s hourly rate.                                                                   |
| JobInvolvement      | The level of employee involvement in their work.                                               |
| JobLevel            | The employee’s hierarchical level within the company.                                          |
| JobRole             | The employee’s job role or position.                                                           |
| JobSatisfaction     | Employee satisfaction level with their job.                                                    |
| MaritalStatus       | The employee’s marital status (e.g., “Single,” “Married,” etc.).                                |
| MonthlyIncome       | The employee’s monthly income.                                                                 |
| MonthlyRate         | The employee’s monthly rate.                                                                   |
| NumCompaniesWorked  | The number of companies where the employee has worked.                                          |
| Over18              | Indicates whether the employee is over 18 years old.                                            |
| OverTime            | Indicates whether the employee works overtime (“Yes” or “No”).                                  |
| PercentSalaryHike   | The percentage of salary increase for the employee.                                             |
| PerformanceRating   | Employee performance rating.                                                                   |
| RelationshipSatisfaction | Employee satisfaction level in interpersonal relationships.                                   |
| StandardHours       | Standard working hours.                                                                        |
| StockOptionLevel    | Employee stock option level.                                                                    |
| TotalWorkingYears   | Total years of work experience for the employee.                                                |
| TrainingTimesLastYear | Number of times the employee received training last year.                                       |
| WorkLifeBalance     | Balance between work and personal life for the employee.                                         |
| YearsAtCompany      | Number of years the employee has worked at the current company.                                  |
| YearsInCurrentRole  | Number of years the employee has been in their current role.                                     |
</details>

### Phases: 🔄 

_To complete development of this project  and ensure the integrity of the data provided by the client, five phases were carried out._


   
* **Phase 1: _Data Exploration and Cleaning_**
  
* **Phase 2: _Data Transformation_**
  
* **Phase 3: _Database Design and Implementation_**
  
* **Phase 4: _A/B Testing_**
  
* **Phase 5: _ETL Creation_**
  
* **Phase 6: _Reporting_**


### To play this project on your computer: 🐍 and 🐬

_For the project you will need to have a version of Python and MySQL and get to work._

###  Libraries to Import: 📚


<details>
<summary>Libraries to start working:</summary>

1. **Data Manipulation** 🧮 🐼
   - **Pandas**
   - **Numpy**
     

2. **Imputación de datos** 🕵️‍♂️
   - Scikit-learn
     - **SimpleImputer**:_Imputes missing values in a dataset using simple strategies such as mean, median, mode, and others._
     - **IterativeImputer**:_Utilizes iterative techniques, especially useful when relationships between variables are complex._
     - **KNNImputer**:_Uses the K-Nearest Neighbors method to estimate missing values._

       
3. **Data visualization** 📊
   -**Seaborn**: _Provides a high-level interface for creating attractive and informative statistical graphics._
   -**Matplotlib**:_Allows the creation of high-quality static plots suitable for publications and reports._


4. **Stadistics and tests** 🧪
   - **Scipy**:_Provides statistical functions and hypothesis tests (e.g., t-tests, chi-square tests, etc.)._

     
5. **Database Connection** ⚡   
   - **mysql.connector**:_A connector for MySQL that allows establishing connections and performing operations on MySQL databases from Python._


</details>


### BBDD Structure: 📁

_In this repository you will find a star-shaped structure, which simplifies analytical queries and is useful for the analysis of large volumes of data._


<details>
  <summary>Structure</summary>
  <img src="https://github.com/nuriancg/project-da-promo-H-module-3-team-1/blob/master/Imagenes/Diagrama%20BBDD.png" alt="Diagrama BBDD">
</details>


### Description of the information you will find in the final BBDD: 📌


_In this dropdown, you will find the description and distribution of each of the columns of the  final document._ 😊


  <details>
<summary> Dictionary:</summary>

| Column_Name         | Description                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------- |
| Age                 | The employee’s age.                                                                           |
| Age_Group           |Referring to categorizing employees based on their age range. There are five labels: (18-25), (26-35), (36-45), (45-55) and (56-65).|
|Attrition|Indicates whether the employee has left the company (“False” means they haven’t left, and “True” means they have).|
Business_Travel|Describes the frequency of work-related travel for the employee (e.g., “Travel_Rarely” for infrequent travel).|
Daily_Rate|The employee’s daily rate.|
Department|The department in which the employee works.|
Distance_From_Home|The distance from the employee’s home to their workplace.|
Education|The employee’s education level.(On a scale from 1 to 5)|
Education_Field|The field of education or specialization for the employee.|
Employee_Number|A unique identification number for the employee.|
Environment_Satisfaction|Employee satisfaction level related to their work environment.( Ranging from 1 to 4, with 4 being the highest satisfaction)|
Gender|The employee’s gender.(Where ‘M’ corresponds to “male” and ‘F’ to “female”).|
Hourly_Rate|The employee’s hourly rate.|
Job_Involvement|The level of employee involvement in their work.(On scale from 1 to 5).|
Job_Level|The employee’s hierarchical level within the company, (On scale from 1 to 5).|
Job_Role1|The employee’s position.|
Job_Satisfaction|Employee satisfaction level with their job.(Ranging from 1 to 4, with 4 being the highest satisfaction).|
Marital_Status|The employee’s marital status.(Accepts these values ‘Married’, ’Divorced’, and 'Unknown').|
Monthly_Rate| The employee’s monthly rate.|
Num_Companies_Worked|The number of companies where the employee has worked.|
Over_Time|Indicates whether the employee works overtime.(Accepts these values “True”,  “False” and 'Unknown').|
Percent_Salary_Hike1|The percentage of salary increase for the employee.(Accepts values between 0 - 1)|
Performance_Rating|Employee performance rating.(On scale from 1 to 5).|
Relationship_Satisfaction| Employee satisfaction level in interpersonal relationships.(On scale from 1 to 5).|
Stock_Option_Level|Employee stock option level.(On a scale from 0 to 4).|
Total_Working_Years|Total years of work experience for the employee.|
Training_Times_Last_Year|Number of times the employee received training last year.|
Work_Life_Balance|Balance between work and personal life for the employee.(On scale from 1 to 5).|
Years_At_Company|Number of years the employee has worked at the current company.|
Years_Since_Last_Promotion|Years since the employee’s last promotion.|
Years_With_Curr_Manager|Years under the supervision of the current manager.|
Date_Birth|The employee’s birth year. (considering data collected in 2023).|
RemoteWork| Whether the employee can work remotely or not.|

</details>


### Target Resolution 🎯🎯


_A statistical analysis was carried out in order to determine if there is a significant difference in the rotation rate of employees according to their level of satisfaction in the company.To do this, employees were divided into two groups according to their level of satisfaction, and then the rotation rate for each of these groups was calculated._


  
|Group|Category|Description|
|------------------------|--------------------------------------------------------------------------|-------------------|
|Group A| Satisfied| Employees with a job satisfaction level equal to or greater than 3 on a scale of 1 to 5.|
|Group B |Discontents|Employees with a job satisfaction level of less than 3 on a scale of 1 to 5.|


* ## _Two hypotheses were established:_


  
| _Hypothesis_|_Description_|
 |------------------------|--------------------------------------------------------------------------| 
|_ Null hypothesis  (H0)_ | _Affirm  that there is no difference; Turnover rate does not affect the level of satisfacción._|
|_ Alternative hypothesis  (H1)_| _Affirmthere is a difference, the level of satisfaction significantly affects the rate of rotación._|



### Test: 📈 📝

|Test Type|	Description|
|---------|------------|
_ttest_ind()_|	_It is a statistical test used to compare two groups and determine if there is a significant difference between them in terms of a variable we are measuring._|
|_ztest()_|	_Indicates how many standard deviations the observed result deviates from the expected value under the null hypothesis._|
|_chi2()_|_The chi-squared test is used to determine the behavior of a certain variable and also to evaluate whether two or more variables are statistically independent_|




<details>
<summary> Full Rotation Rate Analysis</summary> 

_Of the information we have, we extract the rotation rate. It is the indicator that measures how often employees leave the organization and are replaced by new ones in the time period  being analyzed_.

- _Rotation rate in Group A (with medium and high satisfaction) is 0.16%._
- _Rotation rate in Group B (low satisfaction) is 0.24%._
  
**_Based on this data, we see that job dissatisfaction or dissatisfaction is associated with a greater propensity to leave the company._**

 <img src="https://github.com/nuriancg/project-da-promo-H-module-3-team-1/blob/master/Imagenes/Rotation%20rate%20by%20Satisfaction%20Level.png" alt="Rotation Rate Chart">

### Test:_📈📝

* **ttest:**
     - _With a p-value of 0.004, it indicates that there is a significant difference between the two groups. Therefore, in this study, we reject the null hypothesis (H0)._

  
* **Z-test:**
  
  - _With a statistic of -2.94 and a p-value of 0.0032, it indicates that the proportion of people who left the company in Group A (satisfied employees) is lower than in Group B (dissatisfied employees). This reinforces the idea that higher job satisfaction is associated with lower employee turnover. Therefore, we once again reject the null hypothesis. The negative value suggests that the proportion of people who left the company in Group A (satisfied employees) is lower than in Group B (dissatisfied employees). The absolute value, greater than 2, implies that the difference is significant, but the direction of the difference contradicts the numerical increase in the data (i.e., there is less turnover where we might expect more, or vice versa)._

      
* **Chi2 test:**
  
   - _A value of 8.2479 with a p-value of 0.0041 indicates once again that there is a significant difference in satisfaction levels and turnover rate. There is sufficient evidence to reject the null hypothesis._
 
 ### ADDITIONAL TESTS

We made new tests to aquire a deeper understanding of the reasons why employees are dissatisfied; we looked for correlations among the different variables and extracted the following conclusions:

1. _The higher the performance level, the greater the percentage increase in salaries. This is a sign of healthy company practices that reward employees who put in effort on their work._

_In the following chart, the presence of outliers in both values (3 and 4), major in 3, indicates certain exceptions in the company’s salary increase policy for employees with a medium performance level. This could be a topic that evokes different feelings among employees, so it might be interesting  to make future studies to explore this topic further._

_Based on both conclusions, we cannot currently establish reasons for discontent._

<img src='https://github.com/nuriancg/project-da-promo-H-module-3-team-1/blob/master/Imagenes/Relation%20between%20Performance%20Rating%20and%20Salary%20Hike.png' alt="Performance Rating and salary Hike"> 

2. _The longer employees work, the higher their position within the company. This indicates that the company promotes its employees over time. This practice is also positive and cannot be associated with discontent._

<img src='https://github.com/nuriancg/project-da-promo-H-module-3-team-1/blob/master/Imagenes/4%20charts.png' alt="Diferents charts"> 


3. _The longer an employee has worked and the longer they have been with the company, the more years they spend with their current manager. This could indicate that managers maintain their positions, suggesting a certain level of stability. Initially, this could also be considered a good practice by the company, although it might warrant further study. We don’t find any reasons for discontent._

<img src='https://github.com/nuriancg/project-da-promo-H-module-3-team-1/blob/master/Imagenes/Relation%20between%20Years%20at%20the%20Company%20and%20Years%20with%20Current%20Manager.png' alt="Relation Between years at company and years with current manager">    

 4. _As employees get older, they accumulate more experience across different companies. Employees between 40 and 44 years old have worked in more companies than their younger counterparts. This makes sense and should not be a cause for discontent._

<img src='https://github.com/nuriancg/project-da-promo-H-module-3-team-1/blob/master/Imagenes/Relation%20between%20Age%20and%20Total%20Companies%20Worked.png' alt="Relation Between age total companies worked">

5. _The higher the level of education, the more senior the position within the company. This also makes sense and should not be a problem for employees._

<img src='https://github.com/nuriancg/project-da-promo-H-module-3-team-1/blob/master/Imagenes/Relation%20between%20Education%20and%20Job%20Level.png' alt="Relation Between Education Level andJob Level">




### Conclusion: ✅

_Based on the results obtained, we can infer that the company implements favorable practices for its employees, such as salary increases or promotions. However, employee dissatisfaction may be related to other variables that have not been studied currently._

_Therefore, we recommend conducting surveys targeted at employees, allowing them to express the reasons for their dissatisfaction. This would provide a more comprehensive view and help address any underlying issues effectively._

</details> 
