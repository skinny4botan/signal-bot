import os
import logging
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

BOT_TOKEN = "8711059649:AAF7ysdDRw3rbWo9INoHvekeSCwy49QYhWE"
MINI_APP_URL = "https://quiet-otter-e7de5f.netlify.app"

bot = TeleBot(BOT_TOKEN)
logging.basicConfig(level=logging.INFO)

# Временная переменная для хранения file_id (потом заменишь в коде)
IMAGE_FILE_ID = None

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
    
    if IMAGE_FILE_ID:
        # Отправляем картинку по file_id
        bot.send_photo(
            message.chat.id,
            photo=IMAGE_FILE_ID,
            caption="Welcome! Click the button below to open JAMPER SIGNAL:",
            reply_markup=keyboard
        )
    else:
        # Если file_id еще нет — отправляем только текст
        bot.send_message(
            message.chat.id,
            "Welcome! Click the button below to open JAMPER SIGNAL:\n\n"
            "📸 *Чтобы добавить картинку*, отправь её мне, и я запомню!",
            reply_markup=keyboard,
            parse_mode="Markdown"
        )

# Ловим любую картинку, которую отправляют боту
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    global IMAGE_FILE_ID
    
    # Берем file_id самой большой версии картинки (последняя в списке)
    photo = message.photo[-1]
    file_id = photo.file_id
    
    # Сохраняем в глобальную переменную
    IMAGE_FILE_ID = file_id
    
    # Отправляем пользователю file_id и подтверждение
    bot.reply_to(
        message,
        f"✅ *Картинка сохранена!*\n\n"
        f"`{file_id}`\n\n"
        f"Теперь используй `/start` — картинка будет показываться!",
        parse_mode="Markdown"
    )
    
    # Дополнительно: сохраняем в файл на всякий случай
    with open("saved_file_id.txt", "w") as f:
        f.write(file_id)
    print(f"✅ file_id сохранен: {file_id}")

bot.infinity_polling()
