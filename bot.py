from database import movies
from dotenv import load_dotenv
import os
from pymongo import MongoClient

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["repbdw_bot"]
movies = db["movies"]

# ---------------- START ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎬 RepBDW Media Bot\n\n"
        "Send any movie name.\n\n"
        "Admin:\n"
        "/addmovie Movie|Year|Link"
    )

# ---------------- ADD MOVIE ----------------
async def addmovie(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text.replace("/addmovie ", "")

    try:
        name, year, link = text.split("|")

        movies.insert_one({
            "name": name.strip().lower(),
            "year": year.strip(),
            "link": link.strip()
        })

        await update.message.reply_text("✅ Movie Added!")

    except:
        await update.message.reply_text(
            "Usage:\n"
            "/addmovie Avatar|2009|https://drive.google.com/..."
        )

# ---------------- SEARCH ----------------
async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.message.text.lower()

    movie = movies.find_one({"name": query})

    if movie:

        await update.message.reply_text(
            f"🎬 {movie['name'].title()}\n"
            f"📅 {movie['year']}\n\n"
            f"⬇️ Download:\n{movie['link']}"
        )

    else:

        await update.message.reply_text("❌ Movie not found.")

# ---------------- MAIN ----------------
def main():

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("addmovie", addmovie))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))

    print("Bot Running...")
    app.run_polling()

if __name__ == "__main__":
    main()
