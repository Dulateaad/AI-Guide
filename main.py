import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "ВАШ_НОВЫЙ_TOKEN"   # после перевыпуска
WEBAPP_URL = "https://studio--studio-8899645624-9001d.us-central1.hosted.app"

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

@bot.message_handler(commands=['start'])
def start(message):
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton(
            text="🌍 Открыть AI-Гид",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )
    )
    bot.send_message(
        message.chat.id,
        """Сәлем! 👋

Я — Baiterek Guide, ваш персональный гид по Астане.
Составлю маршруты, покажу лучшие места и расскажу интересные факты.

Жмите кнопку ниже и начнём путешествие! 🚀""",
        reply_markup=kb
    )

bot.polling(none_stop=True, skip_pending=True)
