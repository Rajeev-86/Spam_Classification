import cloudpickle
from src.preprocessing import preprocess_column

import os

# loading the model
current_dir = os.path.dirname(os.path.realpath(__file__))

file_path = os.path.join(current_dir, 'spam_classifier_cloud.pkl')

with open(file_path, 'rb') as file:
    model = cloudpickle.load(file)


# Test the model
test_message = ["You won Nokia 500!"]
prediction = model.predict(test_message)
print("Prediction:", "Spam" if prediction[0] == 1 else "Not Spam")
