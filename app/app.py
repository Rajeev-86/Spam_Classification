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
    if user_input.strip():
        prediction = model.predict([user_input])
        result = "Spam" if prediction[0] == 1 else "Not Spam"
        
        if result == "Spam":
            st.markdown(f"""
                <div style="background-color: rgba(255, 205, 210, 0.8); padding: 40px; border-radius: 10px; text-align: center; width: 80%; margin: auto;">
                    <h4 style="color: red;">🚫 The message is classified as: {result}</h4>
                    <p style="font-size: 14px; color: #D32F2F;">This message is potentially harmful or unwanted. Please be cautious!</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div style="background-color: rgba(200, 230, 201, 0.8); padding: 40px; border-radius: 10px; text-align: center; width: 80%; margin: auto;">
                    <h4 style="color: green;">✅ The message is classified as: {result}</h4>
                    <p style="font-size: 14px; color: #388E3C;">This message is safe and not considered spam.</p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.write("Please enter a message.")
