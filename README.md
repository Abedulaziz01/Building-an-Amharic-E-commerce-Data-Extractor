Telegram Data Scraper for Ethiopian E-Commerce
📌 What This Does
Scrapes product listings from Ethiopian Telegram channels

Cleans and prepares Amharic text data

Organizes data for price/product/location analysis

🔧 Setup
Install requirements:

pip install telethon etnltk
Add your Telegram API info in config.py:

python
API_ID = 'your_id'
API_HASH = 'your_hash'
PHONE = '+251...'
▶️ How to Run
python main.py --channels "@Channel1 @Channel2" --limit 500
📂 What You Get
data.csv: All scraped messages

photos/: Downloaded product images

clean_data.csv: Preprocessed text ready for analysis

🌟 Key Features
Handles Amharic text properly

Preserves product prices and locations

Easy to extend for more channels

🛠️ Built With
Python 3

Telethon (for Telegram scraping)

ETNLTK (for Amharic NLP)

For questions or issues, please open a GitHub ticket.
