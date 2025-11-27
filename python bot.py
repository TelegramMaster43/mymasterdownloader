from flask import Flask, request
import telebot
import os
import threading

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

def start_bot():
    bot.polling(none_stop=True, interval=0, timeout=20)

if __name__ == "__main__":
    # Bot को अलग thread में चलाएँ
    threading.Thread(target=start_bot).start()

    # Flask app को run करें ताकि Render को port मिले
    app.run(host="0.0.0.0", port=10000)
