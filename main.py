import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

TOKEN = "8434444079:AAGxd-vjy4dqLiCl84LKSqSbEaEQDyJxH10"
bot = telebot.TeleBot(TOKEN)

# Главное меню с кнопкой "Открыть AI-Гид"
@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    webapp_btn = KeyboardButton(
        text="🌍 Открыть AI-Гид",
        web_app=WebAppInfo(url="https://studio--studio-8899645624-9001d.us-central1.hosted.app")
    )
    markup.add(webapp_btn)
    bot.send_message(message.chat.id, "
Сәлем! 👋

Я — Baiterek Guide, ваш персональный гид по Астане.
Составлю маршруты, покажу лучшие места и расскажу интересные факты.

Жмите кнопку ниже и начнём путешествие! 🚀", reply_markup=markup)

bot.polling()
