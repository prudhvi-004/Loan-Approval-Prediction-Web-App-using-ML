import streamlit as st
import numpy as np
import pickle

# Load the saved model and scaler
with open('loan_model.sav', 'rb') as file:
    model = pickle.load(file)

# App title
st.title("🏦 Loan Approval Prediction App")
st.write("Enter the details below to check if the loan is likely to be approved.")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Number of Dependents", [0, 1, 2, 3])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount (in thousands)", min_value=1)
loan_term = st.selectbox("Loan Term (in days)", [12, 36, 60, 84, 120, 180, 240, 300, 360, 480])
credit_history = st.selectbox("Credit History", [1, 0])
property_area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])

# Encode categorical values
gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0
property_area = 0 if property_area == "Rural" else 1 if property_area == "Semiurban" else 2
dependents = int(dependents)

# Predict button
if st.button("Predict"):
    # Create input array
    input_data = np.array([[gender, married, dependents, education, self_employed,
                            applicant_income, coapplicant_income, loan_amount,
                            loan_term, credit_history, property_area]])


    # Make prediction
    prediction = model.predict(input_data)

    # Show result
    if prediction[0] == 1:
        st.success("✅ Loan is Approved!")
    else:
        st.error("❌ Loan is Not Approved.")
