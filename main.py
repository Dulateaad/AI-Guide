import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# ✅ Читаем токен из окружения (для теста можно временно вписать строкой)
TOKEN = os.getenv("BOT_TOKEN", "8261494879:AAGGHa-BiI03J1UGPntKvZ2i2lmNOM3fu8Q")

# URL твоего мини-приложения
WEBAPP_URL = "https://studio--studio-8899645624-9001d.us-central1.hosted.app"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Команда /start – отправляем кнопку для открытия мини-приложения"""
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(
            text="🚀 Открыть мини-приложение",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )]
    ])
    await update.message.reply_text(
        "Привет! Нажми кнопку ниже, чтобы открыть мини-приложение:",
        reply_markup=keyboard
    )


def main() -> None:
    app = Application.builder().token(TOKEN).build()

    # Регистрируем обработчик команды /start
    app.add_handler(CommandHandler("start", start))

    # Render обычно передает порт в переменной PORT
    port = int(os.environ.get("PORT", "8443"))

    if os.environ.get("RENDER"):   # если деплой на Render
        app.run_webhook(
            listen="0.0.0.0",
            port=port,
            url_path=TOKEN,
            webhook_url=f"https://{os.environ['RENDER_EXTERNAL_HOSTNAME']}/{TOKEN}"
        )
    else:                          # локальный запуск
        app.run_polling()


if __name__ == "__main__":
    main()
