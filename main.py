import os
import telebot


bot = telebot.Telebot("1939991142:AAGf4Jd6fANpne1YU2zCMT_nsquEQefSwgo")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm Uvindu Bro Chat Bot")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message, "https://youtube.com/c/Uvindubro")



bot.polling()
