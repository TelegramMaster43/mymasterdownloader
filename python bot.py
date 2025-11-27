from flask import Flask, request
import telebot
import os

# Environment variable से TOKEN पढ़ें
TOKEN = os.getenv("TOKEN")  

if not TOKEN:
    raise ValueError("TOKEN not found. Please set the environment variable on Render.")

bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Downloader Bot Ready! Send any link to download.")

@app.route('/')
def home():
    return "Bot running on Render!"

if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0, timeout=20)
