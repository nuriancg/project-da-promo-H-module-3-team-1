**(_información en Inglés al final de esta página_)**

# Iniciativa de Optimización de Talento de ABC Corporation
      
_La Iniciativa de Optimización de Talento de ABC Corporation tiene como objetivo abordar diferentes aspectos relacionados con los recursos humanos de su empresa. Para ello, han contratado los servicios de nuestra empresa, Data Gadgets._

_**Data Gadgets** es una empresa formada por un grupo de analistas de datos que utilizan metodología ágil para cumplir eficientemente con los objetivos propuestos en tiempo récord._

### Equipo Data Gatgets: 📈🔍

|Names|GitHub_link_user_name|
|-----|------------------|
|_Patricia González_|https://github.com/Patri-EGG|
|_Paola Sánchez_|https://github.com/paolasanchezsolorzano|
|_Fernanda Martí_|https://github.com/fernandaMarti|
|_Nuria Cano_| https://github.com/nuriancg|
|_Raquel Castellanos_|https://github.com/RachelCaste|


### Descripción del Cliente 👨‍💻

_ABC Corporation, fundada en 1980 en California, es una firma de consultoría tecnológica especializada en proporcionar soluciones de inteligencia artificial (IA) y aprendizaje automático a empresas de diversas industrias._

### Objetivo: 🎯
_Presentar los resultados del análisis exploratorio de datos, diseñar un experimento A/B para probar hipótesis críticas y analizar los resultados para proporcionar a ABC Corporation información valiosa y veraz._

### Documentación Inicial 📌
_En esta sección, encontrarás la descripción de cada una de las columnas del documento original._

<details>
<summary> Dictionary:</summary>

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

### Fases del Proyecto 🔄

_Para completar el desarrollo de este proyecto y garantizar la integridad de los datos proporcionados por el cliente, se llevaron a cabo cinco fases:_

* **Fase 1: Exploración y Limpieza de Datos**
* **Fase 2: Transformación de Datos**
* **Fase 3: Diseño e Implementación de la Base de Datos**
* **Fase 4: Pruebas A/B**
* **Fase 5: Creación de ETL (Extracción, Transformación y Carga)**
* **Fase 6: Generación de Informes**




### Requisitos para Ejecutar el Proyecto 🐍 y 🐬
_Para trabajar en este proyecto, necesitarás tener instaladas versiones de Python y MySQL._

###  Librerias a Importar: 📚

<details>
<summary>Librarias para comenzar a trabajar:</summary>

1. **Manipulación de Datos** 🧮 🐼
   - **Pandas**
   - **Numpy**

2. **Imputación de datos** 🕵️‍♂️
   - Scikit-learn
     -**SimpleImputer:** _Imputa valores faltantes en un conjunto de datos utilizando estrategias simples como la media, la mediana, la moda, entre             otras._
     -**IterativeImputer:** _Utiliza técnicas iterativas, especialmente útiles cuando las relaciones entre variables son complejas._
     -**KNNImputer:** _Estima valores faltantes utilizando el método de los vecinos más cercanos (K-Nearest Neighbors)._
       
3. **Visualización de datos** 📊
   -**Seaborn**: _Provides a high-level interface for creating attractive and informative statistical graphics._
   -**Matplotlib**:_Allows the creation of high-quality static plots suitable for publications and reports._

4. **Estadísticas y Pruebas** 🧪
-**Scipy:** _Proporciona funciones estadísticas y pruebas de hipótesis (por ejemplo, pruebas t, pruebas de chi-cuadrado, etc.)_
   
5. **Conexión a la Base de Datos** ⚡
-**mysql.connector:** _Un conector para MySQL que permite establecer conexiones y realizar operaciones en bases de datos MySQL desde Python._

</details>

### Estructura de la Base de Datos 📁

_En este repositorio encontrarás una estructura en forma de estrella, que simplifica las consultas analíticas y es útil para el análisis de grandes volúmenes de datos._

<details>
  <summary>Structura</summary>
  <img src="https://github.com/nuriancg/project-da-promo-H-module-3-team-1/blob/master/Diagrama%20BBDD.png" alt="Diagrama BBDD">
</details>

### Descripción de la Información en la Base de Datos Final 📌

_En este desplegable, encontrarás la descripción y distribución de cada una de las columnas del documento final._ 😊


  <details>
<summary> Dictionary:</summary>

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


<details>
   
<summary> English </summary>

# ABC Corporation's Talent Optimization!!!

__ABC Corporation's Talent Optimization Initiative aims to respond to different aspects related to the human resources of their company. For which he has hired the services of our company Data Gatgets._

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
  <img src="https://github.com/nuriancg/project-da-promo-H-module-3-team-1/blob/master/Diagrama%20BBDD.png" alt="Diagrama BBDD">
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
