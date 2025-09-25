import telebot
from telebot import types

# --- Ваш реальный токен ---
TOKEN = "8261494879:AAGGHa-BiI03J1UGPntKvZ2i2lmNOM3fu8Q"

# --- URL мини-приложения ---
WEBAPP_URL = "https://studio--studio-8899645624-9001d.us-central1.hosted.app"

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")


@bot.message_handler(commands=["start"])
def start(message: types.Message):
    """
    Отправляем приветствие и кнопку для открытия мини-приложения.
    """
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(
        text="🚀 Открыть мини-приложение",
        web_app=types.WebAppInfo(url=WEBAPP_URL)
    )
    markup.add(btn)

    bot.send_message(
        message.chat.id,
        "Привет! Нажми кнопку ниже, чтобы открыть мини-приложение:",
        reply_markup=markup
    )


if __name__ == "__main__":
    # Для локального запуска — обычный polling.
    # На Render можно выставить переменную окружения RENDER, чтобы при необходимости
    # переключиться на webhook.
    import os
    port = int(os.environ.get("PORT", "8443"))

    if os.environ.get("RENDER"):
        # --- Пример простого webhook ---
        WEBHOOK_URL = f"https://{os.environ['RENDER_EXTERNAL_HOSTNAME']}/{TOKEN}"
        bot.remove_webhook()
        bot.set_webhook(url=WEBHOOK_URL)
    else:
        bot.infinity_polling(skip_pending=True)

