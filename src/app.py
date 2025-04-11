import pandas as pd
import numpy as np
import streamlit as st
import joblib

# Load the model and preprocessor
model = joblib.load(r'C:/Users/DELL/OneDrive/Desktop/ML_Project/model/churn_model.pkl')
preprocessor = joblib.load(r'C:/Users/DELL/OneDrive/Desktop/ML_Project/model/preprocessor.pkl')

# Streamlit app
def main():
    st.title("Customer Churn Prediction")

    # User input for prediction
    st.header("Enter Customer Information")
    gender = st.selectbox("Gender", ["Female", "Male"])
    Partner = st.selectbox("Partner", ["Yes", "No"])
    Dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.slider("Tenure (months)", 0, 72, 1)
    PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
    MultipleLines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
    InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
    DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
    Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
    PaymentMethod = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
    MonthlyCharges = st.number_input("Monthly Charges", 0.0)
    TotalCharges = st.number_input("Total Charges", 0.0)

    # Prepare input data for prediction
    input_data = {
        'gender': gender,
        'Partner': Partner,
        'Dependents': Dependents,
        'tenure': tenure,
        'PhoneService': PhoneService,
        'MultipleLines': MultipleLines,
        'InternetService': InternetService,
        'OnlineSecurity': OnlineSecurity,
        'OnlineBackup': OnlineBackup,
        'DeviceProtection': DeviceProtection,
        'TechSupport': TechSupport,
        'StreamingTV': StreamingTV,
        'StreamingMovies': StreamingMovies,
        'Contract': Contract,
        'PaperlessBilling': PaperlessBilling,
        'PaymentMethod': PaymentMethod,
        'MonthlyCharges': MonthlyCharges,
        'TotalCharges': TotalCharges
    }

    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data])

    # Preprocess the input data
    input_processed = preprocessor.transform(input_df)

    # Make prediction
    if st.button("Predict"):
        prediction = model.predict(input_processed)
        st.write("Prediction: ", "Churn" if prediction[0] == 1 else "No Churn")

if __name__ == "__main__":
    main()