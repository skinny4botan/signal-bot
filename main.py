import os
import logging
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

BOT_TOKEN = "8711059649:AAF7ysdDRw3rbWo9INoHvekeSCwy49QYhWE"
MINI_APP_URL = "https://quiet-otter-e7de5f.netlify.app"
IMAGE_URL = "https://i.postimg.cc/T3D3QBkx/2026-04-24-07-00-13.jpg"

bot = TeleBot(BOT_TOKEN)
logging.basicConfig(level=logging.INFO)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = InlineKeyboardMarkup()
    web_app = WebAppInfo(url=MINI_APP_URL)
    button = InlineKeyboardButton(
        text="🚀 Start",
        web_app=web_app,
        style="success"
    )
    keyboard.add(button)
    
    bot.send_photo(
        message.chat.id,
        photo=IMAGE_URL,
        caption="Welcome! Click the button below to open JAMPER SIGNAL:",
        reply_markup=keyboard
    )

bot.infinity_polling()
