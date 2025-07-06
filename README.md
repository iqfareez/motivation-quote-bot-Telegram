![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](http://t.me/motivate_us_bot)

# Motivation Quote Bot for Telegram

Try now: http://t.me/motivate_us_bot

- Send `/start` **or**
- Tap on **START** button

## Getting Started

Follow these steps to run the bot locally on your machine:

### Prerequisites

- Python 3.7 or higher
- Git

### Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/motivation-quote-bot-Telegram.git
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

   To get a bot token:

   - Message [@BotFather](https://t.me/BotFather) on Telegram
   - Create a new bot with `/newbot`
   - Copy the token provided

5. **Run the bot**
   ```bash
   python bot.py
   ```

The bot will start running in polling mode and respond to commands in your Telegram chat.

### Available Commands

- `/start` - Start the bot
- `/help` - Show help message
- `/getstudymotiv` - Get a random study motivation quote
- `/getislamicmotiv` - Get a random Islamic motivation quote

## Deployment

For deployment instructions, see:

- [Heroku Deployment](docs/deployment/Heroku.md)
- [VPS Cloudpanel Deployment](docs/deployment/VPS-Cloudpanel.md)

### Sources

1. https://technobb.com/100-inspirational-islamic-quotes-with-beautiful-images/
2. https://www.daniel-wong.com/2015/10/05/study-motivation-quotes/
3. https://mvslim.com/you-can-still-make-the-most-of-ramadan-32-inspirational-and-motivational-islamic-quotes-to-help-you-how/
4. https://www.daniel-wong.com/2015/10/05/study-motivation-quotes/

### Watch speedcoding on YouTube!

https://youtu.be/laHspJzlpDQ

### Honourable mentions

Credit to this page https://towardsdatascience.com/how-to-deploy-a-telegram-bot-using-heroku-for-free-9436f89575d2 for tutorial on deploying to Heroku
... and of course StackOverflow hahaha
