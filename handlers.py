from telegram import Update
from telegram.ext import ContextTypes
from database import get_movie

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to RepBDW Media Bot!\n\n"
        "🎬 Send me any movie name.\n\n"
        "Example:\nAvatar"
    )

async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    movie_name = update.message.text.strip()

    movie = get_movie(movie_name)

    if movie:
        await update.message.reply_text(
            f"🎬 {movie['name']}\n"
            f"📅 {movie['year']}\n\n"
            f"📥 File ID:\n{movie['file_id']}"
        )
    else:
        await update.message.reply_text(
            "❌ Movie not found.\n\n"
            "Please try another movie name."
        )
