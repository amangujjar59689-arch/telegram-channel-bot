from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# ==========================
# EDIT THESE LINKS
# ==========================

START_IMAGE = "https://YOUR_IMAGE_LINK_HERE"

PROCESS_LINK = "https://t.me/YOUR_PROCESS_CHANNEL"

PHOTO_VIDEO_LINK = "https://t.me/YOUR_PHOTO_VIDEO_CHANNEL"

BUY_LINK = "https://t.me/YOUR_ADMIN_USERNAME"

FEEDBACK_LINK = "https://t.me/YOUR_FEEDBACK_CHANNEL"

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
