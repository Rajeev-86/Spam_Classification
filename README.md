Title: Spam Classification Web App

Description: A simple web application built using Streamlit that classifies text messages as Spam or Not Spam using an SVM classifier with TF-IDF vectorization.

Project Overview
This project provides a spam classification web application that allows users to input text messages and get real-time predictions about whether the message is Spam or Not Spam. The model uses TF-IDF (Term Frequency-Inverse Document Frequency) for feature extraction and an SVM (Support Vector Machine) classifier for prediction. The app is built using Streamlit, a framework that makes it easy to create data apps with minimal effort. The model is trained directly in the app, so no external model files are needed.

Features
Real-time Spam Prediction: Classifies a user's text message as either Spam or Not Spam.
Dynamic Model Training: TF-IDF and SVM are trained on a small dataset of spam and non-spam messages directly in the web app.
Web Interface: Clean and simple UI powered by Streamlit, where users can easily interact with the app.

Technologies Used
Streamlit: For building the web interface.
Scikit-learn: For machine learning, including SVM and TF-IDF vectorization.
Pandas: For data manipulation and preparation.
Python: The core programming language.
Regular Expressions (Regex): For text preprocessing.

Setup and Installation
Follow these steps to set up the project locally:

- Clone the Repository:
git clone https://github.com/Rajeev-86/Spam-Classification.git
cd spam-classifier-web-app

- Create a Virtual Environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate

- Install Dependencies: They are listed in requirements.txt
Then run the following command to install the dependencies: pip install -r requirements.txt

- Run the Application:
After installing the required dependencies, you can run the Streamlit app:
streamlit run app.py
This will open the web app in your default browser.

- Usage
Open the app by running streamlit run app.py.
Enter a message in the provided text box.
Click the "Classify" button to receive a prediction of whether the message is Spam or Not Spam.

- Acknowledgements
Streamlit: For providing an easy and efficient way to create web applications for data science.
Scikit-learn: For providing powerful tools for machine learning and natural language processing.
Cloudpickle: Used to serialize the model for easy loading and deployment.





