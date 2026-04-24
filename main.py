import os
import logging
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# ========== НАСТРОЙКИ ==========
BOT_TOKEN = "8711059649:AAF7ysdDRw3rbWo9INoHvekeSCwy49QYhWE"
MINI_APP_URL = "https://quiet-otter-e7de5f.netlify.app"
# ===============================

bot = TeleBot(BOT_TOKEN)
logging.basicConfig(level=logging.INFO)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton(
        text="🚀 Start",
        web_app={"url": MINI_APP_URL},
        style="success"  # ← РАБОТАЕТ В telebot
    )
    keyboard.add(button)
    
    bot.send_message(
        message.chat.id,
        "Welcome! Click the button below to open JAMPER SIGNAL:",
        reply_markup=keyboard
    )

print("✅ Бот запущен!")
bot.infinity_polling()
