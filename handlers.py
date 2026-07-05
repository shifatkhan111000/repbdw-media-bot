from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from database import get_movie, add_movie
from config import ADMIN_ID

# Conversation States
MOVIE_NAME, MOVIE_YEAR, MOVIE_FILE = range(3)

# Conversation States
MOVIE_NAME = 1
MOVIE_YEAR = 2
MOVIE_FILE = 3


# -------------------- START --------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to RepBDW Media Bot!\n\n"
        "🎬 Send me any movie name.\n"
        "Example:\nAvatar"
    )


# -------------------- SEARCH --------------------

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
            "❌ Movie not found."
        )


# -------------------- ADD MOVIE --------------------

async def addmovie(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("❌ You are not Admin.")
        return ConversationHandler.END

    await update.message.reply_text(
        "🎬 Enter Movie Name:"
    )

    return MOVIE_NAME


async def movie_name(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data["movie_name"] = update.message.text.strip()

    await update.message.reply_text(
        "📅 Enter Release Year:"
    )

    return MOVIE_YEAR


async def movie_year(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data["movie_year"] = update.message.text.strip()

    await update.message.reply_text(
        "🎥 Send the Movie File (Video or Document):"
    )

    return MOVIE_FILE


async def movie_file(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.video:
        file_id = update.message.video.file_id

    elif update.message.document:
        file_id = update.message.document.file_id

    else:
        await update.message.reply_text(
            "❌ Please send a Video or Document."
        )
        return MOVIE_FILE

    add_movie(
        context.user_data["movie_name"],
        context.user_data["movie_year"],
        file_id
    )

    await update.message.reply_text(
        "✅ Movie Saved Successfully!"
    )

    context.user_data.clear()

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data.clear()

    await update.message.reply_text(
        "❌ Movie adding cancelled."
    )

    return ConversationHandler.END
