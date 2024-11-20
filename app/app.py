import streamlit as st
import cloudpickle
from preprocessing import preprocess_column #custom module
import os

# loading the model
current_dir = os.path.dirname(os.path.realpath(__file__))

file_path = os.path.join(current_dir, 'spam_classifier_cloud.pkl')

with open(file_path, 'rb') as file:
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



