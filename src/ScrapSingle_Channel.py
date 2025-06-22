from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

# === REPLACE THESE WITH YOUR OWN VALUES ===
api_id = 9985562  # Get this from https://my.telegram.org
api_hash = '830372933750ad4f043b2dc5d0899848'  # Also from https://my.telegram.org
phone_number = '+251922609325'  # Your Telegram phone number
channel_username = '@Shageronlinestore'  # Replace with the actual channel username (without @), e.g., 'EthioDeals'

# === Create a Telegram client ===
client = TelegramClient('my_scraper_session', api_id, api_hash)

# === Log in and scrape ===
with client:
    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        code = input("Enter the code you received on Telegram: ")
        try:
            client.sign_in(phone_number, code)
        except SessionPasswordNeededError:
            password = input("Enter your 2FA password: ")
            client.sign_in(password=password)

    # Fetch messages
    print("📥 Scraping messages...")
    messages = client.iter_messages(channel_username, limit=100)  # Change limit as needed

    with open("telegram_messages.txt", "w", encoding="utf-8") as f:
        for message in messages:
            if message.text:
                clean = message.text.strip().replace('\n', ' ')
                f.write(clean + "\n")

print("✅ Messages saved to telegram_messages.txt")
