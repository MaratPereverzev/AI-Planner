import telebot
from dotenv import dotenv_values

config = dotenv_values(".env")

bot = telebot.TeleBot(config.get("telegram_token"), parse_mode="markdown")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


bot.infinity_polling()