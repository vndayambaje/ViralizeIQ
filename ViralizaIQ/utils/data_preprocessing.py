# utils/data_preprocessing.py
import pandas as pd
import re

def load_raw_data(file_path):
    """Loads raw data from CSV."""
    return pd.read_csv(file_path)

def preprocess_caption(caption):
    """Basic text preprocessing on captions."""
    caption = caption.lower()
    caption = re.sub(r"http\S+", "", caption)  # Remove URLs
    caption = re.sub(r"[^a-zA-Z0-9\s]", "", caption)  # Remove special chars
    return caption

def preprocess_data(file_path):
    """Loads, preprocesses data, and returns a DataFrame."""
    df = load_raw_data(file_path)
    df['clean_caption'] = df['caption'].apply(preprocess_caption)
    df['caption_length'] = df['clean_caption'].apply(len)  # Feature engineering
    return df

def save_processed_data(df, file_path):
    df.to_csv(file_path, index=False)

