import pandas as pd

input_path = "data/cleaned/telegram_cleaned.csv"
output_path = "data/labels/sample_for_labeling.txt"

# Load the cleaned messages
df = pd.read_csv(input_path)

# Select a random sample of 40 messages (you can change the number)
sample_df = df.sample(n=40, random_state=42)

# Extract messages only
messages = sample_df["cleaned_text"].tolist()

# Save each message on its own line
with open(output_path, "w", encoding="utf-8-sig") as f:
    for msg in messages:
        f.write(msg.strip() + "\n\n")  # Separate messages by blank line

print(f"✅ 40 sample messages saved to {output_path} for labeling.")
