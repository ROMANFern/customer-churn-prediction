import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open("smote_xgboost_churn_model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit UI
st.title("Customer Churn Prediction App")
st.markdown("Enter customer details to predict churn probability.")

# Collect user input **before** calling the function
senior_citizen = st.radio("Is the customer a Senior Citizen?", ["No", "Yes"])
dependents = st.radio("Does the customer have dependents?", ["No", "Yes"])
tenure = st.number_input("Tenure (months)", min_value=0, max_value=72, value=12)
phone_service = st.radio("Does the customer have Phone Service?", ["No", "Yes"])
multiple_lines = st.radio("Does the customer have Multiple Lines?", ["No", "Yes"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
online_backup = st.radio("Does the customer use Online Backup?", ["No", "Yes"])
device_protection = st.radio("Does the customer use Device Protection?", ["No", "Yes"])
tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
streaming_tv = st.radio("Does the customer use Streaming TV?", ["No", "Yes"])
streaming_movies = st.radio("Does the customer use Streaming Movies?", ["No", "Yes"])
contract = st.selectbox("Contract Type", ["Month-to-Month", "One Year", "Two Years"])
paperless_billing = st.radio("Is Paperless Billing enabled?", ["No", "Yes"])
payment_method = st.selectbox("Payment Method", ["Credit Card", "Electronic Check", "Mailed Check"])
monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, value=50.0)
total_charges = st.number_input("Total Charges ($)", min_value=0.0, value=600.0)

# Convert categorical inputs to numerical format
def preprocess_input():
    """Convert user inputs into model-compatible format"""

    contract_map = {"Month-to-Month": [0, 0], "One Year": [1, 0], "Two Years": [0, 1]}
    internet_service_map = {"DSL": [1, 0], "Fiber optic": [0, 1], "No": [0, 0]}
    security_map = {"Yes": 1, "No": 0, "No internet service": 0}
    tech_map = {"Yes": 1, "No": 0, "No internet service": 0}
    payment_map = {"Credit Card": [1, 0, 0], "Electronic Check": [0, 1, 0], "Mailed Check": [0, 0, 1]}
    
    input_data = np.array([
        1 if senior_citizen == "Yes" else 0,
        1 if dependents == "Yes" else 0,
        tenure,
        1 if phone_service == "Yes" else 0,
        1 if paperless_billing == "Yes" else 0,
        monthly_charges,
        total_charges,
        1 if multiple_lines == "Yes" else 0,
        internet_service_map[internet_service][0],  # Fiber optic
        internet_service_map[internet_service][1],  # No internet
        security_map[online_security],  # Online Security Yes
        1 if online_backup == "Yes" else 0,
        1 if device_protection == "Yes" else 0,
        tech_map[tech_support],  # Tech Support Yes
        1 if streaming_tv == "Yes" else 0,
        1 if streaming_movies == "Yes" else 0,
        contract_map[contract][0],  # Contract One Year
        contract_map[contract][1],  # Contract Two Year
        payment_map[payment_method][0],  # Credit Card
        payment_map[payment_method][1],  # Electronic Check
        payment_map[payment_method][2],  # Mailed Check
        total_charges / (tenure + 1),  # AvgSpendPerMonth
        (1 if streaming_tv == "Yes" else 0) + (1 if streaming_movies == "Yes" else 0),  # StreamingService_Combined
        int((monthly_charges > 70) and (contract == "Month-to-Month") and (tenure < 12))  # ChurnRisk_High
    ]).reshape(1, -1)
    
    return input_data

# Button to trigger prediction
if st.button("Predict Churn"):
    input_data = preprocess_input()
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0, 1]

    if prediction[0] == 1:
        st.error(f"This customer is likely to churn with a probability of {probability:.2f}")
    else:
        st.success(f"This customer is unlikely to churn. Churn probability: {probability:.2f}")