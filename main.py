from telethon import TelegramClient, events
import asyncio
import csv
import os
import re
import string

# Telegram API credentials
api_id = 19886142
api_hash = '93eeef554ba66ed581073d1cd86e0f71'
client = TelegramClient('ethiomart_session', api_id, api_hash)

# Target channels
channels = [
    -1001156873089, -1001781246058, -1001193582142,
    -1001377094832, -1001332690598, -1001288238074,
    -1002076677162, -1001916860157, -1001215311843,
    -1002221380088, -1002441688690, -1001499072259,
    -1001623501096, -1001101378903, -1001718832800
]

# Output config
csv_file = 'data/messages.csv'
fieldnames = ['date', 'chat', 'sender', 'message', 'cleaned_message', 'tokens']

# Init CSV with header
os.makedirs(os.path.dirname(csv_file), exist_ok=True)
with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

# Message limits
MAX_MESSAGES = 10
message_count = 0

# ========= 🧹 Preprocessing Functions ==========

def normalize_text(text):
    """Lowercase, remove extra spaces and normalize characters."""
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def remove_urls_emojis_punct(text):
    """Remove links, emojis, and punctuation (keep Amharic chars)."""
    text = re.sub(r'https?://\S+', '', text)  # URLs
    text = re.sub(r'[^\w\s\u1200-\u137F\u1380-\u139F\u2D80-\u2DDF]', '', text)  # keep Amharic + alphanum
    return text

def tokenize_text(text):
    """Split text into tokens for NER input."""
    return text.split()

def preprocess_for_ner(raw_text):
    """Run full preprocessing pipeline for raw Telegram text."""
    step1 = normalize_text(raw_text)
    step2 = remove_urls_emojis_punct(step1)
    tokens = tokenize_text(step2)
    return step2.strip(), tokens

# ========= 📥 Telegram Message Handler ==========

@client.on(events.NewMessage(chats=channels))
async def handler(event):
    global message_count

    sender = await event.get_sender()
    sender_name = sender.username or sender.first_name or str(sender.id)
    chat_name = event.chat.title if event.chat else str(event.chat_id)
    message_date = event.message.date.strftime('%Y-%m-%d %H:%M:%S')
    raw_text = event.raw_text.strip().replace('\n', ' ')

    cleaned_text, tokens = preprocess_for_ner(raw_text)

    # Save to CSV
    with open(csv_file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({
            'date': message_date,
            'chat': chat_name,
            'sender': sender_name,
            'message': raw_text,
            'cleaned_message': cleaned_text,
            'tokens': ' '.join(tokens)
        })

    print(f"[{message_date}] Message from {sender_name} in {chat_name}:\n→ {cleaned_text}")
    print("="*50)

    message_count += 1
    if message_count >= MAX_MESSAGES:
        print(f"\n✅ Reached {MAX_MESSAGES} messages. Disconnecting...")
        await client.disconnect()

# ========= 🏁 Main Async Run =========

async def main():
    await client.start()
    print("🚀 Client started. Listening for messages...\n")
    await client.run_until_disconnected()
    print("\n🔌 Client disconnected.")

if __name__ == '__main__':
    asyncio.run(main())
