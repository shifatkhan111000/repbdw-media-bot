import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Bot
BOT_TOKEN = os.getenv("BOT_TOKEN")

# MongoDB Atlas
MONGO_URI = os.getenv("MONGO_URI")

# Admin ID
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

# Bot Settings
BOT_NAME = "RepBDW Media Bot"
BOT_VERSION = "2.0 Stable"
