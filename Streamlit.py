# Streamlit

import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ====================================
# PAGE CONFIG
# ====================================
st.set_page_config(
    page_title="Employee Attrition Prediction",
    layout="wide"
)

st.title("📊 Employee Attrition Analysis & Prediction")
st.write("Predict whether an employee is at risk of leaving the organization.")

# ====================================
# LOAD TRAINED MODEL
# ====================================
model = joblib.load("models/attrition_model.pkl")

# ====================================
# SIDEBAR INPUTS
# ====================================
st.sidebar.header("Employee Details")

Age = st.sidebar.slider("Age", 18, 60, 30)
Daily_Rate = st.sidebar.number_input("Daily Rate", 100, 2000, 800)
Distance_From_Home = st.sidebar.slider("Distance From Home", 1, 30, 10)
Education = st.sidebar.slider("Education Level (1–5)", 1, 5, 3)
Environment_Satisfaction = st.sidebar.slider("Environment Satisfaction (1–4)", 1, 4, 3)
Hourly_Rate = st.sidebar.number_input("Hourly Rate", 30, 200, 70)
Job_Involvement = st.sidebar.slider("Job Involvement (1–4)", 1, 4, 3)
Job_Level = st.sidebar.slider("Job Level", 1, 5, 2)
Job_Satisfaction = st.sidebar.slider("Job Satisfaction (1–4)", 1, 4, 3)
Monthly_Income = st.sidebar.number_input("Monthly Income", 1000, 50000, 15000)
Num_Companies_Worked = st.sidebar.slider("No. of Companies Worked", 0, 10, 2)
Percent_Salary_Hike = st.sidebar.slider("Percent Salary Hike", 10, 25, 15)
Performance_Rating = st.sidebar.slider("Performance Rating (1–4)", 1, 4, 3)
Relationship_Satisfaction = st.sidebar.slider("Relationship Satisfaction (1–4)", 1, 4, 3)
Stock_Option_Level = st.sidebar.slider("Stock Option Level", 0, 3, 1)
Total_Working_Years = st.sidebar.slider("Total Working Years", 0, 40, 10)
Training_Times_Last_Year = st.sidebar.slider("Trainings Last Year", 0, 6, 3)
Work_Life_Balance = st.sidebar.slider("Work Life Balance (1–4)", 1, 4, 3)
Years_At_Company = st.sidebar.slider("Years at Company", 0, 40, 5)
Years_In_Current_Role = st.sidebar.slider("Years in Current Role", 0, 18, 3)
Years_Since_Last_Promotion = st.sidebar.slider("Years Since Last Promotion", 0, 15, 2)
Years_With_Curr_Manager = st.sidebar.slider("Years with Current Manager", 0, 17, 3)

Gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
Over_Time = st.sidebar.selectbox("Over Time", ["Yes", "No"])
Over_18 = "Y"

Business_Travel = st.sidebar.selectbox(
    "Business Travel",
    ["Travel_Rarely", "Travel_Frequently", "Non-Travel"]
)

Department = st.sidebar.selectbox(
    "Department",
    ["Sales", "Research & Development", "Human Resources"]
)

Education_Field = st.sidebar.selectbox(
    "Education Field",
    ["Life Sciences", "Medical", "Marketing", "Technical Degree", "Other"]
)

Job_Role = st.sidebar.selectbox(
    "Job Role",
    [
        "Sales Executive", "Research Scientist", "Laboratory Technician",
        "Manufacturing Director", "Healthcare Representative",
        "Manager", "Sales Representative", "Research Director", "Human Resources"
    ]
)

Marital_Status = st.sidebar.selectbox(
    "Marital Status",
    ["Single", "Married", "Divorced"]
)

# ====================================
# CREATE INPUT DATAFRAME
# ====================================
input_data = pd.DataFrame({
    "Age": [Age],
    "Daily_Rate": [Daily_Rate],
    "Distance_From_Home": [Distance_From_Home],
    "Education": [Education],
    "Environment_Satisfaction": [Environment_Satisfaction],
    "Hourly_Rate": [Hourly_Rate],
    "Job_Involvement": [Job_Involvement],
    "Job_Level": [Job_Level],
    "Job_Satisfaction": [Job_Satisfaction],
    "Monthly_Income": [Monthly_Income],
    "Num_Companies_Worked": [Num_Companies_Worked],
    "Percent_Salary_Hike": [Percent_Salary_Hike],
    "Performance_Rating": [Performance_Rating],
    "Relationship_Satisfaction": [Relationship_Satisfaction],
    "Stock_Option_Level": [Stock_Option_Level],
    "Total_Working_Years": [Total_Working_Years],
    "Training_Times_Last_Year": [Training_Times_Last_Year],
    "Work_Life_Balance": [Work_Life_Balance],
    "Years_At_Company": [Years_At_Company],
    "Years_In_Current_Role": [Years_In_Current_Role],
    "Years_Since_Last_Promotion": [Years_Since_Last_Promotion],
    "Years_With_Curr_Manager": [Years_With_Curr_Manager],
    "Gender": [1 if Gender == "Male" else 0],
    "Over_Time": [1 if Over_Time == "Yes" else 0],
    "Over_18": [1],
    "Business_Travel": [Business_Travel],
    "Department": [Department],
    "Education_Field": [Education_Field],
    "Job_Role": [Job_Role],
    "Marital_Status": [Marital_Status]
})

# ====================================
# ONE-HOT ENCODING
# ====================================
input_data = pd.get_dummies(
    input_data,
    columns=[
        "Business_Travel",
        "Department",
        "Education_Field",
        "Job_Role",
        "Marital_Status"
    ],
    drop_first=True
)

# Align with training features
input_data = input_data.reindex(
    columns=model.feature_names_in_,
    fill_value=0
)

# ====================================
# PREDICTION
# ====================================
st.markdown("---")

if st.button("🔍 Predict Attrition"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Employee is **LIKELY TO LEAVE**")
        st.write(f"**Attrition Probability:** {probability:.2%}")
    else:
        st.success(f"✅ Employee is **LIKELY TO STAY**")
        st.write(f"**Attrition Probability:** {probability:.2%}")

st.markdown("---")
st.caption("Built using Machine Learning & Streamlit")