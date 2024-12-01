import streamlit as st
import cloudpickle
import os
import sys

# To import the preprocessor module from src
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(BASE_DIR)
from src.preprocessing import preprocess_column

# Load the model
MODEL_PATH = os.path.join(BASE_DIR, 'model', 'spam_classifier_cloud.pkl')
with open(MODEL_PATH, 'rb') as file:
    model = cloudpickle.load(file)

# Streamlit app
st.title("Spam Message Classifier")
st.write("Enter a message below to check if it is spam or not.")

user_input = st.text_area("Message", placeholder="Type your message here...")

if st.button("Classify"):
    if user_input.strip() != "":
        prediction = model.predict([user_input])[0]

        if prediction == 1:
            result = "This message is Spam"
        else:
            result = "This message is Not Spam"

        st.write(f"Prediction: **{result}**")
    else:
        st.write("Please enter a message.")
