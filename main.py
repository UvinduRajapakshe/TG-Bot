import os
import telebot


bot = telebot.TeleBot("1989413995:AAFL78oGj7IQJB18lBGNRvfd5HoYVotnk-I")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm MR SHAGGY Chat Bot")


@bot.message_handler(commands=["hi"])
def send_message(message):
  bot.reply_to(message, "Join our group and get the answer to your question brother! type /grouplink to get our grop link! ")

@bot.message_handler(commands=["grouplink"])
def send_message(message):
  bot.send_message(message, "Our group link - https://t.me/SL_MEDIA_TECH_GRUOP")

bot.polling()

