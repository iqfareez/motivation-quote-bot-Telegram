# motivation quote bot Telegram

## http://t.me/motivate_us_bot

- Send `/start` **or**
- Tap on **START** button

## Hi. Goodluck! :wink:

Alhamdulillah ramai sukaaa T_T. Ni yg terharu ni thanks my friendsss.

## Steps to deploy

⚠️ **NOTE:** As of November 2022, Heroku will [no longer provide a free tier plan](https://blog.heroku.com/next-chapter) anymore. You can use [Railway](https://railway.app/) for your deployment instead. It does not have free plan, **but** it gives you $5 monthly credit (it's enough for our use cases). The deployment steps are easy and almost similar to the steps below.

1. Create a new Telegram bot from [BotFather](http://t.me/BotFather)
2. Follow the process and at the end, you'll see your bot token. **Copy** this token.
3. Go to signup/login to [Heroku](https://www.heroku.com/), click <kbd>New</kbd> to create new app.
4. Enter the **name** (eg: `my-tele-bot-200`) and choose the **region**. Then, click <kbd>Create App</kbd>.
5. Remember the bot token we copied earlier in step 2? Great! Since the token is private and sensitive, we don't want to hardcoded in our program. Now, still in the Heroku, go to **Settings**, and then **Config Vars**.
6. Click <kbd>Reveal Config Vars</kbd>
7. Fill in the KEY and VALUE
   - **KEY**: `MY_BOT_TOKEN` (This variable is what we are going to use in our app)
   - **TOKEN**: _paste you Telegram bot token_
8. Click on <kbd>Open App</kbd> (located at upper right corner). Then, **copy** the link. It will look something like `https://my-tele-bot-200.herokuapp.com/`
9. Now, **fork** and **clone** this repo into your local machine.
10. Open `bot.py` file. You'll need to replace value in `SERVER_URL` and `BOT_TOKEN`.
    - **SERVER_URL**: _Paste the link you've copied in step 8_
    - **BOT_TOKEN**: Replace value inside [''] with your config vars, it will looks like `os.environ['MY_BOT_TOKEN']`

Now, we are good to go to deploy to the Heroku, there are generally two ways to deploy it, by using **Heroku CLI** or **GitHub**. You can use whatever you like but I'm going to use the latter.

12. **Push** your changes to the GitHub.
13. In the Heroku, go to **Deploy** section, then go to **Deployment method**
14. Choose the **second** option, connect with your GitHub repository and follow all the process.
15. You can setup automatic/manual deployment.
16. All set! Go to your Telegram bot, press <kbd>**START**</kbd>, the bot will respond to you in seconds. :wink:

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
