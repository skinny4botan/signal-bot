import os
import logging
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

BOT_TOKEN = "8711059649:AAF7ysdDRw3rbWo9INoHvekeSCwy49QYhWE"
MINI_APP_URL = "https://quiet-otter-e7de5f.netlify.app"

IMAGE_FILE_ID = "AgACAgIAAxkBAAMnaerfdcONzphkmIjPyJaB-a0ItJMAAmASaxtkGVhLsG0N-a1Fe3oBAAMCAAN5AAM7BA"

bot = TeleBot(BOT_TOKEN)
logging.basicConfig(level=logging.INFO)

ADMIN_ID = 1472818360

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
        photo=IMAGE_FILE_ID,
        caption="Welcome! Click the button below to open JAMPER SIGNAL:",
        reply_markup=keyboard
    )

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "❌ Access denied.")
        return
    
    photo = message.photo[-1]
    new_file_id = photo.file_id
    bot.reply_to(
        message,
        f"✅ New file_id (admin only):\n`{new_file_id}`",
        parse_mode="Markdown"
    )

@bot.message_handler(content_types=['video', 'document', 'audio', 'voice', 'animation'])
def block_media(message):
    if message.from_user.id != ADMIN_ID:
        bot.reply_to(message, "❌ Access denied.")

bot.infinity_polling()
