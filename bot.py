import logging
import os
import json
import random
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Load environment variables from .env file
load_dotenv()

PORT = int(os.environ.get('PORT', 5000))
SERVER_URL = os.environ.get('SERVER_URL', 'https://motivationbot.up.railway.app/')
BOT_TOKEN = os.environ['TELE_BOT_TOKEN']

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Load quotes from JSON files
def load_quotes(filename):
    try:
        with open(f'data/{filename}', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        logger.error(f"Could not find {filename}")
        return []

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    name = update.effective_user
    await update.message.reply_text(f'Hi {name.username} <3')

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.warning('Update "%s" caused error "%s"', update, context.error)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = """View list of available commands by typing slash character into the chat
    \nOr view source code at Sourcecode: https://github.com/iqfareez/motivation-quote-bot-Telegram (leave a STAR ok)
    \nand also watch this bot speedcoding: https://youtu.be/laHspJzlpDQ"""
    await update.message.reply_text(message)

async def getstudymotiv(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    quotes = load_quotes('study_quotes.json')
    if quotes:
        random_quote = random.choice(quotes)
        await update.message.reply_text(random_quote)
    else:
        await update.message.reply_text("Sorry, no study quotes available at the moment.")

async def getislamicmotiv(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    quotes = load_quotes('islamic_quotes.json')
    if quotes:
        random_quote = random.choice(quotes)
        await update.message.reply_text(random_quote)
    else:
        await update.message.reply_text("Sorry, no Islamic quotes available at the moment.")

def main():
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("getstudymotiv", getstudymotiv))
    application.add_handler(CommandHandler("getislamicmotiv", getislamicmotiv))
    application.add_error_handler(error_handler)

    # Start the bot with webhook
    # application.run_webhook(
    #     listen="0.0.0.0",
    #     port=PORT,
    #     url_path=BOT_TOKEN,
    #     webhook_url=f"{SERVER_URL}{BOT_TOKEN}"
    # )

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
