import streamlit as st
import pickle
import os

# Load the trained model once during startup
MODEL_PATH = (r"C:\Users\Neeraj\OneDrive\Pictures\Student_Performance\model.pickle")
if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, "rb") as model_file:
        model = pickle.load(model_file)
else:
    model = None
    st.error("Model file not found. Ensure 'model.pickle' is in the specified directory.")

# Title of the web app
st.title('Performance Index Prediction')

# Get user inputs for the prediction
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=1, max_value=100, step=1)
hours_studied = st.number_input("Hours Studied", min_value=0, step=1)
previous_scores = st.number_input("Previous Scores (%)", min_value=0, max_value=100, step=1)
extracurricular = st.selectbox("Extracurricular Activities", ["No", "Yes"])
sleep_hours = st.number_input("Sleep Hours", min_value=0, max_value=24, step=1)
sample_papers_practiced = st.number_input("Sample Question Papers Practiced", min_value=0, step=1)

# Convert categorical inputs to numeric values (0 for No, 1 for Yes)
input_dict = {
    "gender": 1 if gender == "Female" else 0,
    "extracurricular": 1 if extracurricular == "Yes" else 0
}

# Add all inputs into a feature list
input_features = [
    input_dict["gender"],
    age,
    hours_studied,
    previous_scores,
    input_dict["extracurricular"],
    sleep_hours,
    sample_papers_practiced
]

# Prediction
if st.button("Predict"):
    if model:
        prediction = model.predict([input_features])[0]
        st.write(f"Predicted Performance Index: {prediction}")
    else:
        st.error("Prediction model is not available.")



