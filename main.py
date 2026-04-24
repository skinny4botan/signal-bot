import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# ========== НАСТРОЙКИ ==========
BOT_TOKEN = "8711059649:AAF7ysdDRw3rbWo9INoHvekeSCwy49QYhWE"
MINI_APP_URL = "https://quiet-otter-e7de5f.netlify.app"
# ===============================

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Создаем зеленую инлайн-кнопку — style="success" добавляется сюда
    keyboard = [[
        InlineKeyboardButton(
            text="Start", 
            web_app={"url": MINI_APP_URL},
            style="success"      # <--- СЮДА ДОБАВЬ ЭТУ СТРОКУ
        )
    ]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Welcome! Click the button below to open JAMPER SIGNAL",
        reply_markup=reply_markup
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ "__main__":
    main()
