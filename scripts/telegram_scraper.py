from telethon.sync import TelegramClient
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
client = TelegramClient('session', api_id, api_hash)

# Load channels from Excel
channels_df = pd.read_excel("channels_to_crawl.xlsx", engine='openpyxl')
channels = channels_df.iloc[:, 0].dropna().tolist()

client.start()

all_messages = []

for username in channels[:5]:  # pick 5 for now
    try:
        print(f"Fetching from {username}")
        for message in client.iter_messages(username, limit=100):  # tune limit
            if message.text:
                all_messages.append({
                    "channel": username,
                    "message_id": message.id,
                    "date": message.date,
                    "text": message.text
                })
    except Exception as e:
        print(f"Error fetching from {username}: {e}")

df = pd.DataFrame(all_messages)
df.to_csv("data/raw/telegram_raw.csv", index=False, encoding="utf-8-sig")
print("Saved data to data/raw/telegram_raw.csv")

client.disconnect()
