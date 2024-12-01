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
                    <div style="background-color: #FFCDD2; padding: 20px; border-radius: 10px; text-align: center;">
                        <h3 style="color: red;">🚫 The message is classified as: {result}</h3>
                        <p style="font-size: 16px; color: #D32F2F;">This message is potentially harmful or unwanted. Please be cautious!</p>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div style="background-color: #C8E6C9; padding: 20px; border-radius: 10px; text-align: center;">
                    <h3 style="color: green;">✅ The message is classified as: {result}</h3>
                    <p style="font-size: 16px; color: #388E3C;">This message is safe and not considered spam.</p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.error("Please enter a valid message.")



