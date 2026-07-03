from telegram import Update
from telegram.ext import ContextTypes
from database import get_movie


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to RepBDW Media Bot!\n\n"
        "🎬 Send me any movie name.\n"
        "Example:\nAvatar"
    )


async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Check if message exists
        if not update.message or not update.message.text:
            return

        movie_name = update.message.text.strip()

        # Empty message
        if movie_name == "":
            await update.message.reply_text("❌ Please enter a movie name.")
            return

        # Search MongoDB
        movie = get_movie(movie_name)

        if movie:
            name = movie.get("name", "Unknown")
            year = movie.get("year", "Unknown")
            file_id = movie.get("file_id", "Not Available")

            await update.message.reply_text(
                f"🎬 {name}\n"
                f"📅 {year}\n\n"
                f"📥 File ID:\n{file_id}"
            )

        else:
            await update.message.reply_text(
                f"🔍 You searched: {movie_name}\n\n"
                "❌ Movie not found."
            )

    except Exception as e:
        print("ERROR:", e)

        await update.message.reply_text(
            f"⚠️ Internal Error:\n{e}"
        )
