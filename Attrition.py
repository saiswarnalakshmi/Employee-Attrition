import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import mysql.connector

# Read the Excel file

file_path = r"C:\Users\IBuild\OneDrive\ドキュメント\Saiswarnalakshmi files\DS Guvi\Mini Project 3\Employee-Attrition.xlsx"
df = pd.read_excel(file_path)
df.head()
df = df.bfill().ffill()
df = df.replace(0, np.nan)
df = df.fillna(df.mean(numeric_only=True))
df
df.to_excel("cleaned_data(1).xlsx", index=False)
df.to_excel(r"C:\Users\IBuild\OneDrive\ドキュメント\Saiswarnalakshmi files\DS Guvi\Mini Project 3\cleaned_data.xlsx", index=False)
df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})
cols = [
    "Age", "Attrition", "Business_Travel", "Daily_Rate",
    "Department", "Distance_From_Home", "Education", "Education_Field",
    "Employee_Count", "Employee_Number", "Environment_Satisfaction", "Gender",
    "Hourly_Rate", "Job_Involvement", "Job_Level", "Job_Role",
    "Job_Satisfaction", "Marital_Status", "Monthly_Income", "Monthly_Rate",
    "Num_Companies_Worked", "Over_18", "Over_Time", "Percent_Salary_Hike",
    "Performance_Rating", "Relationship_Satisfaction", "Standard_Hours",
    "Stock_Option_Level", "Total_Working_Years", "Training_Times_Last_Year",
    "Work_Life_Balance", "Years_At_Company", "Years_In_Current_Role",
    "Years_Since_Last_Promotion", "Years_With_Curr_Manager"
]

data_list = df[cols].values.tolist()

# connecting to MYSQL
import mysql.connector
conn_mysql = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Saiswarna@28599"
)
cursor_mysql=conn_mysql.cursor()
print("Mysql connection established successfully")

#Creating a data base in Mysql
cursor_mysql.execute("CREATE DATABASE Employee_Attrition_6")
print("Database created successfully")

#Creating a table in mysql
cursor_mysql.execute("USE Employee_Attrition_6")

cursor_mysql.execute("""
CREATE TABLE Employee_attrition(
    Age INT,
    Attrition BOOLEAN,
    Business_Travel VARCHAR(50),
    Daily_Rate INT,
    Department VARCHAR(50),
    Distance_From_Home VARCHAR(50),
    Education VARCHAR(10),
    Education_Field VARCHAR(30),
    Employee_Count VARCHAR(20),
    Employee_Number INT PRIMARY KEY,
    Environment_Satisfaction INT,
    Gender VARCHAR(10),
    Hourly_Rate INT,
    Job_Involvement INT,
    Job_Level INT,
    Job_Role VARCHAR(50),
    Job_Satisfaction INT,
    Marital_Status VARCHAR(20),
    Monthly_Income INT,
    Monthly_Rate INT,
    Num_Companies_Worked INT,
    Over_18 VARCHAR(20),
    Over_Time VARCHAR(10),
    Percent_Salary_Hike INT,
    Performance_Rating VARCHAR(30),
    Relationship_Satisfaction INT,
    Standard_Hours INT,
    Stock_Option_Level INT,
    Total_Working_Years INT,
    Training_Times_Last_Year INT,
    Work_Life_Balance INT,
    Years_At_Company INT,
    Years_In_Current_Role INT,
    Years_Since_Last_Promotion INT,
    Years_With_Curr_Manager INT
);
"""
)   
conn_mysql.commit()
print("Table has created successfully in mysql")

insert_query = """
INSERT INTO Employee_attrition (
    Age, Attrition, Business_Travel, Daily_Rate,
    Department, Distance_From_Home,Education, Education_Field,Employee_Count,Employee_Number,Environment_Satisfaction, Gender,
    Hourly_Rate, Job_Involvement, Job_Level, Job_Role, Job_Satisfaction,
    Marital_Status, Monthly_Income, Monthly_Rate, Num_Companies_Worked, Over_18,Over_Time,
    Percent_Salary_Hike,Performance_Rating, Relationship_Satisfaction,Standard_Hours,Stock_Option_Level,
    Total_Working_Years,Training_Times_Last_Year, Work_Life_Balance, Years_At_Company,
    Years_In_Current_Role, Years_Since_Last_Promotion, Years_With_Curr_Manager
)
VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s
)
"""

# Use the correct variable in executemany
cursor_mysql.executemany(insert_query, data_list)
conn_mysql.commit()
print("Data inserted successfully into MySQL")





