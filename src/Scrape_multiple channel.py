from telethon import TelegramClient
import csv
import os


# Load environment variables once

api_id = ('9985562')
api_hash =('830372933750ad4f043b2dc5d0899848')
phone = ('251922609325')

# Function to scrape data from a single channel
async def scrape_channel(client, channel_username, writer, media_dir):
    entity = await client.get_entity(channel_username)
    channel_title = entity.title  # Extract the channel's title
    async for message in client.iter_messages(entity, limit=10000):
        media_path = None
        if message.media and hasattr(message.media, 'photo'):
            # Create a unique filename for the photo
            filename = f"{channel_username}_{message.id}.jpg"
            media_path = os.path.join(media_dir, filename)
            # Download the media to the specified directory if it's a photo
            await client.download_media(message.media, media_path)
        
        # Write the channel title along with other data
        writer.writerow([channel_title, channel_username, message.id, message.message, message.date, media_path])

# Initialize the client once
client = TelegramClient('scraping_session', api_id, api_hash)

async def main():
/*************  ✨ Windsurf Command ⭐  *************/
    """
    Asynchronously starts the Telegram client and scrapes data from specified channels.

    This function performs the following actions:
    1. Starts the Telegram client.
    2. Creates a directory for saving media files if it doesn't exist.

/*******  cee6ec5e-a227-4c45-b6c0-d3a1b5d658ed  *******/
    await client.start()
    
    # Create a directory for media files
    media_dir = 'photos'
    os.makedirs(media_dir, exist_ok=True)

    # Open the CSV file and prepare the writer
    with open('telegram_data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Channel Title', 'Channel Username', 'ID', 'Message', 'Date', 'Media Path'])  # Include channel title in the header
        
        # List of channels to scrape
        channels = [
            '@Shageronlinestore',  # Existing channel
                 # You can add more channels here
            
        ]
        
        # Iterate over channels and scrape data into the single CSV file
        for channel in channels:
            await scrape_channel(client, channel, writer, media_dir)
            print(f"Scraped data from {channel}")

with client:
    client.loop.run_until_complete(main())