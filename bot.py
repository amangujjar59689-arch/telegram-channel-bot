from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# ==========================
# EDIT THESE LINKS
# ==========================

START_IMAGE = "https://i.postimg.cc/T3wMhCPn/IMG-20260626-022222-003.jpg"

PROCESS_LINK = "https://t.me/shreeganeshbazarrr"

PHOTO_VIDEO_LINK = "https://t.me/qulitychek"

BUY_LINK = "https://t.me/shreeganeshbazarr"

FEEDBACK_LINK = "https://t.me/custmorfeedback"

# ==========================


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("💰 Process", url=PROCESS_LINK)],
        [InlineKeyboardButton("🎥 Photo And Video", url=PHOTO_VIDEO_LINK)],
        [InlineKeyboardButton("💵 Buy Currency", url=BUY_LINK)],
        [InlineKeyboardButton("👍 Customer Feedback", url=FEEDBACK_LINK)]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    caption = (
        "✨ *Welcome!*\n\n"
        "Please choose an option below."
    )

    await update.message.reply_photo(
        photo=START_IMAGE,
        caption=caption,
        parse_mode="Markdown",
        reply_markup=reply_markup
    )


def main():

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("✅ Bot Started Successfully...")

    app.run_polling()


if __name__ == "__main__":
    main()
