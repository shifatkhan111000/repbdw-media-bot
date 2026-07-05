from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ConversationHandler,
    filters,
)

from config import BOT_TOKEN
from handlers import (
    start,
    search,
    addmovie,
    movie_name,
    movie_year,
    movie_file,
    cancel,
    MOVIE_NAME,
    MOVIE_YEAR,
    MOVIE_FILE,
)


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # Conversation Handler
    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler("addmovie", addmovie)
        ],
        states={
            MOVIE_NAME: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, movie_name)
            ],
            MOVIE_YEAR: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, movie_year)
            ],
            MOVIE_FILE: [
                MessageHandler(filters.VIDEO | filters.Document.ALL, movie_file)
            ],
        },
        fallbacks=[
            CommandHandler("cancel", cancel)
        ],
    )

    # Commands
    app.add_handler(CommandHandler("start", start))

    # Add Movie Conversation
    app.add_handler(conv_handler)

    # Search
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            search,
        )
    )

    print("🚀 RepBDW Media Bot Started Successfully!")

    app.run_polling()


if __name__ == "__main__":
    main()
