<img width="5806" height="3870" alt="repo cover photo screenshot telegram" src="https://github.com/user-attachments/assets/c9060005-97e3-46da-b620-69075dcdfa91" />

[![Telegram](https://img.shields.io/badge/%40motivate_us_bot-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](http://t.me/motivate_us_bot)

# Motivation Quote Bot for Telegram

A Telegram bot for getting motivation, including Islamic motivational reminders. Originally built in lieu of my upcoming final exams back during my university days.

## Getting Started

Follow these steps to run the bot locally on your machine. You can choose the [conventional](#using-python) way or [Docker](#using-docker) way.

### Using Python

You'll need Python 3.7 or higher installed on your system.

1. **Clone the repository**

   ```bash
   git clone https://github.com/iqfareez/motivation-quote-bot-Telegram
   cd motivation-quote-bot-Telegram
   ```

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root and add your bot token:

   ```
   TELE_BOT_TOKEN=your_telegram_bot_token_here
   ```

   To have a bot token, you need to have a bot on Telegram. You can create one using [BotFather](https://t.me/BotFather) on Telegram.

5. **Run the bot**
   ```bash
   python bot.py
   ```

### Using Docker

More simpler approach to quickly run the bot is using [Docker](https://www.docker.com/). Make sure you have Docker installed on your system.

1. Create a `.env` file in the project root and add your bot token:

   ```
   TELE_BOT_TOKEN=your_telegram_bot_token_here
   ```

2. Run the command below to start the bot using Docker Compose:

   ```bash
   docker compose -f compose.yaml up --build
   ```

Either way, the bot will start running in polling mode and respond to commands in your Telegram chat.

## Usages

- `/start` - Start the bot
- `/help` - Show help message
- `/getstudymotiv` - Get a random study motivation quote
- `/getislamicmotiv` - Get a random Islamic motivation quote

## Deployment

You can use [`compose.prod.yml`](compose.prod.yml) to deploy the bot using Docker Compose in production. Make sure to set the `TELE_BOT_TOKEN` environment variable in your deployment environment.

See [packages](https://github.com/users/iqfareez/packages/container/package/motivation-quote-bot-telegram) for more details.

## Quotes Sources

1. https://technobb.com/100-inspirational-islamic-quotes-with-beautiful-images/
2. https://www.daniel-wong.com/2015/10/05/study-motivation-quotes/
3. https://mvslim.com/you-can-still-make-the-most-of-ramadan-32-inspirational-and-motivational-islamic-quotes-to-help-you-how/
4. https://www.daniel-wong.com/2015/10/05/study-motivation-quotes/

### Watch speedcoding on YouTube!

https://youtu.be/laHspJzlpDQ
