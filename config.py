import os
from dotenv import load_dotenv

# Load .env file (local use only)
load_dotenv()

# =========================
# BOT TOKEN (Telegram)
# =========================
BOT_TOKEN = os.getenv("BOT_TOKEN")

# =========================
# MONGO DB CONNECTION
# =========================
MONGO_URI = os.getenv("MONGO_URI")

# =========================
# SAFETY CHECK (IMPORTANT)
# =========================
if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN not found! Check Railway Variables or .env file.")

if not MONGO_URI:
    raise ValueError("❌ MONGO_URI not found! Check Railway Variables or .env file.")

print("✅ Config Loaded Successfully")
