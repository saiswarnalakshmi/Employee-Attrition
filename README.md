Project focuses on analyzing employee data and predicting employee attrition using Machine Learning, MySQL, and Streamlit.
Data Processing
Employee data is loaded from an Excel file.
Missing values are handled using forward/backward fill and mean imputation.
Categorical variables are encoded, and numerical features are scaled.
Cleaned data is saved for reuse and consistency.
Database Integration (MySQL)
A MySQL database and table are created to store cleaned employee data.
Relevant fields such as age, income, job role, satisfaction levels, and attrition status are inserted.
This allows structured storage and future querying for analysis
Feature Engineering
New features like Tenure Category and Annual Income are derived.
These features help improve the model’s understanding of employee behavior.
Machine Learning Model:
A Random Forest Classifier is trained to predict employee attrition.
The dataset is split into training and testing sets.
Model performance is evaluated using:
Accuracy
Confusion Matrix
Classification Report
AUC-ROC score
The trained model is saved for deployment.
Model Evaluation
Streamlit Application
Outcome:
Data cleaning
Database management
Machine learning modeling
Real-time prediction through a web interface
