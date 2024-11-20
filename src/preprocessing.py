import re
import pandas as pd

def preprocess_string(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

def preprocess_column(df_column):
    if not isinstance(df_column, pd.Series):
        df_column = pd.Series(df_column)

    return df_column.apply(preprocess_string)