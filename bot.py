import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import random
from CONSTANTS import *

""" forked from liuhh02 https://medium.com/@liuhh02 """

PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = TELEGRAM_BOT_TOKEN

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.


def start(update, context):
    name = update.message.from_user
    update.message.reply_text('Hi {}'.format(name['username']))


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def help(update, context):
    message = """View list of available commands by typing slash character into the chat
    \nOr view source code at Sourcecode: https://github.com/fareezMaple/motivation-quote-bot-Telegram (leave a STAR ok)
    \nand also watch this bot speedcoding: https://youtu.be/laHspJzlpDQ"""
    update.message.reply_text(message)


def getstudymotiv(update, context):
    # content by https://www.daniel-wong.com/2015/10/05/study-motivation-quotes/
    quotes = ["Believe you can and you’re halfway there.", "You have to expect things of yourself before you can do them.",
              "It always seems impossible until it’s done.", "Don’t let what you cannot do interfere with what you can do. – John Wooden",
              "Start where you are. Use what you have. Do what you can. – Arthur Ashe", "Successful and unsuccessful people do not vary greatly in their abilities.",
              "They vary in their desires to reach their potential. – John Maxwell", "The secret of success is to do the common things uncommonly well. – John D. Rockefeller",
              "Good things come to people who wait, but better things come to those who go out and get them.", "Strive for progress, not perfection.",
              "I find that the harder I work, the more luck I seem to have. – Thomas Jefferson", "Success is the sum of small efforts, repeated day in and day out. – Robert Collier",
              "Don’t wish it were easier; wish you were better. – Jim Rohn",
              "I don’t regret the things I’ve done. I regret the things I didn’t do when I had the chance.",
              "There are two kinds of people in this world: those who want to get things done and those who don’t want to make mistakes. – John Maxwell",
              "The secret to getting ahead is getting started.", "You don’t have to be great to start, but you have to start to be great.",
              "The expert in everything was once a beginner.", "There are no shortcuts to any place worth going. – Beverly Sills",
              "Push yourself, because no one else is going to do it for you.", "Some people dream of accomplishing great things. Others stay awake and make it happen.",
              "There is no substitute for hard work. – Thomas Edison", "The difference between ordinary and extraordinary is that little “extra.”",
              "You don’t always get what you wish for; you get what you work for.", "It’s not about how bad you want it. It’s about how hard you’re willing to work for it.",
              "The only place where success comes before work is in the dictionary. – Vidal Sassoon", "There are no traffic jams on the extra mile. – Zig Ziglar",
              "If people only knew how hard I’ve worked to gain my mastery, it wouldn’t seem so wonderful at all. – Michelangelo",
              "“All our dreams can come true, if we have the courage to pursue them.” – Walt Disney.",
              "If it’s important to you, you’ll find a way. If not, you’ll find an excuse.", "Don’t say you don’t have enough time. You have exactly the same number of hours per day that were given to Helen Keller, Pasteur, Michelangelo, Mother Teresea, Leonardo da Vinci, Thomas Jefferson, and Albert Einstein. – H. Jackson Brown Jr.",
              "Challenges are what make life interesting. Overcoming them is what makes life meaningful. – Joshua J. Marine",
              "Life has two rules: 1) Never quit. 2) Always remember Rule #1.", "I’ve failed over and over and over again in my life. And that is why I succeed. – Michael Jordan",
              "I don’t measure a man’s success by how high he climbs, but how high he bounces when he hits the bottom. – George S. Patton",
              "If you’re going through hell, keep going. – Winston Churchill", "Don’t let your victories go to your head, or your failures go to your heart.",
              "Failure is the opportunity to begin again more intelligently. – Henry Ford",
              "You don’t drown by falling in the water; you drown by staying there. – Ed Cole", "The difference between a stumbling block and a stepping-stone is how high you raise your foot.",
              "The pain you feel today is the strength you will feel tomorrow. For every challenge encountered there is opportunity for growth.",
              "“Be like a diamond, precious and rare, not like a stone, found everywhere.” Anonymous",
              "It’s not going to be easy, but it’s going to be worth it."]
    length = len(quotes)
    randomIndex = random.randint(0, length - 1)
    update.message.reply_text(quotes[randomIndex])


def getislamicmotiv(update, context):
    quotes = ["“If Allah wants to do good to somebody, he afflicts him with trials.” – Sahih Al Bukhari",
              "Doctors can treat you, but only ALLAH can heal you",
              "Allah is enough",
              "When things are too hard to handle, retreat & count your blessings instead.",
              "Allah’s timing is perfect in every matter. We don’t always understand the wisdom behind it. But we have to learn to trust it.",
              "Allah knows what is the best for you and when it’s best for you to have it.",
              "No matter what your physical appearance, when you have kindness in your heart, You’re the most beautiful person in the world. – Mufti Ismail Menk",
              "“Do not lose hope, nor be sad.” Quran 3:139",
              "“Call upon Me, I will respond to you.” Quran 40:60"
              "“Never underestimate the power of Dua (supplication).” Anonymous",
              "“Allah (God) does not burden a soul beyond that it can bear.” Quran 2:286",
              "“They plan, and Allah (God) plans. Surely, Allah (God) is the best of planners.” Quran 8:30"]
    length = len(quotes)
    randomIndex = random.randint(0, length - 1)
    update.message.reply_text(quotes[randomIndex])


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("getstudymotiv", getstudymotiv))
    dp.add_handler(CommandHandler("getislamicmotiv", getislamicmotiv))

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook(
        HEROKU_APP_LINK + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()
