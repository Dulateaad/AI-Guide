import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# <<<=== ВПИШИ СВОЙ ТОКЕН и ссылку на мини-апп ===>>>
TOKEN = "8261494879:AAGGHa-BiI03J1UGPntKvZ2i2lmNOM3fu8Q"
WEBAPP_URL = "https://studio--studio-8899645624-9001d.us-central1.hosted.app"

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text="🚀 Открыть мини-приложение",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    )
    bot.send_message(
        message.chat.id,
        "Привет! Нажми кнопку ниже, чтобы открыть мини-приложение:",
        reply_markup=keyboard
    )

if __name__ == "__main__":
    print("Бот запущен. Нажмите Ctrl+C для остановки.")
    bot.infinity_polling()
