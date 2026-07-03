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

TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")

if not TOKEN:
    raise ValueError("BOT_TOKEN missing!")

if not MONGO_URI:
    raise ValueError("MONGO_URI missing!")

client = MongoClient(MONGO_URI)

db = client["repbdw_bot"]

movies = db["movies"]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🎬 RepBDW Media Bot\n\n"
        "Send movie name."
    )


async def addmovie(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text.replace("/addmovie ", "")

    data = text.split("|")

    if len(data) != 3:
        await update.message.reply_text(
            "Example:\n"
            "/addmovie Avatar|2009|https://drive.google.com/xxxxx"
        )
        return

    name = data[0].strip()

    year = data[1].strip()

    link = data[2].strip()

    movies.insert_one({

        "name": name.lower(),

        "title": name,

        "year": year,

        "link": link

    })

    await update.message.reply_text("✅ Movie Added Successfully")


async def search(update: Update, context: ContextTypes.DEFAULT_TYPE):

    movie = update.message.text.lower()

    result = movies.find_one({"name": movie})

    if result:

        await update.message.reply_text(

            f"🎬 {result['title']}\n"

            f"📅 {result['year']}\n\n"

            f"📥 {result['link']}"

        )

    else:

        await update.message.reply_text(

            "❌ Movie Not Found"

        )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(CommandHandler("addmovie", addmovie))

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))

print("Bot Running...")

app.run_polling()
