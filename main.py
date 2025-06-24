from telethon import TelegramClient, events
import asyncio
import csv
import os

# Telegram API credentials
api_id = 19886142
api_hash = '93eeef554ba66ed581073d1cd86e0f71'

# Initialize Telegram client
client = TelegramClient('ethiomart_session', api_id, api_hash)

# Updated list of Telegram channel IDs
channels = [
    -1001156873089,  # Tulips Event & sales
    -1001193582142,  # Afriwork (Freelance Ethiopia)
    -1001377094832,  # Afriwork (Amharic)
    -1001332690598,  # Adama Jobs
    -1001288238074,  # INVEST ZONE
    -1002076677162,  # HTU Registrar
    -1002441688690,  # ASTU Talks & Thoughts
    -1001623501096,  # Emmersive Learning
    -1001499072259,  # ATC NEWS
    -1001101378903,  # UDEMY FREE | Coursevania
]

MAX_MESSAGES = 8
message_count = 0

# CSV output config
csv_file = 'data/messages.csv'
fieldnames = ['date', 'chat', 'sender', 'message']

# Ensure output directory exists
os.makedirs(os.path.dirname(csv_file), exist_ok=True)

# Write headers before listening
with open(csv_file, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()

@client.on(events.NewMessage(chats=channels))
async def handler(event):
    global message_count
    sender = await event.get_sender()
    sender_name = sender.username or sender.first_name or str(sender.id)
    chat_name = event.chat.title if event.chat else str(event.chat_id)
    message_date = event.message.date.strftime('%Y-%m-%d %H:%M:%S')
    message_text = event.raw_text.replace('\n', ' ')

    # Save to CSV
    with open(csv_file, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({
            'date': message_date,
            'chat': chat_name,
            'sender': sender_name,
            'message': message_text
        })

    print(f"[{message_date}] Message from {sender_name} in {chat_name}: {message_text}")
    print("=" * 50)

    message_count += 1
    if message_count >= MAX_MESSAGES:
        print(f"Reached {MAX_MESSAGES} messages. Disconnecting...")
        await client.disconnect()

async def main():
    await client.start()
    print("Client started, listening for messages...")
    await client.run_until_disconnected()
    print("Client disconnected.")

if __name__ == '__main__':
    asyncio.run(main())
