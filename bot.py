from dotenv import load_dotenv
import os

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# Load .env
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN not found!")

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to RepBDW Media Bot!\n\n"
        "🎬 Send me any movie name.\n\n"
        "Example:\nAvatar"
    )

# Movie search (temporary)
async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    movie = update.message.text

    await update.message.reply_text(
        f"🔍 You searched: {movie}\n\n"
        "🚧 Movie database is not connected yet.\n"
        "Next step: MongoDB + Google Drive."
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
