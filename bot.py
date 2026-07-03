from dotenv import load_dotenv

load_dotenv()

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

import os from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to RepBDW Media Bot!\n\n🔎 Send a movie name to search."
    )
async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    movie = update.message.text

    await update.message.reply_text(
        f"🔎 You searched for: {movie}\n\n⚠️ Movie database is not connected yet."
    )
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
