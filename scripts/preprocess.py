import pandas as pd
import re
import os

input_path = "data/raw/telegram_raw.csv"
output_path = "data/cleaned/telegram_cleaned.csv"

# Load raw data
df = pd.read_csv(input_path)

# Define cleaning function
def clean_text(text):
    text = str(text)
    text = re.sub(r'[\t\n\r]+', ' ', text)
    text = re.sub(r'http\S+', '', text)  # remove URLs
    text = re.sub(r'@\w+', '', text)  # remove @mentions
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

df["cleaned_text"] = df["text"].apply(clean_text)
df.to_csv(output_path, index=False, encoding="utf-8-sig")
print(f"Cleaned data saved to {output_path}")
