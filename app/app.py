import streamlit as st
import cloudpickle
import os
import sys

# Get the absolute path of the directory two levels up
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Add the base directory to the Python path
sys.path.append(BASE_DIR)

# Now you can import your module
from src.preprocessing import preprocess_column

# Construct the absolute path to the model file
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'spam_classifier_cloud.pkl')

# Load the model
with open(MODEL_PATH, 'rb') as file:
    model = cloudpickle.load(file)

# Streamlit app
st.title("Spam Message Classifier")
st.write("Enter a message below to check if it is spam or not.")

user_input = st.text_area("Message", placeholder="Type your message here...")

if st.button("Classify"):
    if user_input.strip():
        prediction = model.predict([user_input])
        result = "Spam" if prediction[0] == 1 else "Not Spam"
        st.success(f"The message is classified as: **{result}**")
    else:
        st.error("Please enter a valid message.")



