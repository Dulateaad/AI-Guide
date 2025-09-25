import logging
from telegram import (
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext
)

# ── Вставьте сюда ваш токен ──────────────────────────────
TOKEN = "8261494879:AAGGHa-BiI03J1UGPntKvZ2i2lmNOM3fu8Q"
# ── URL вашего мини-приложения ───────────────────────────
WEBAPP_URL = "https://studio--studio-8899645624-9001d.us-central1.hosted.app"

# Логирование (удобно на Render)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    """Отправляем приветствие и кнопку для открытия мини-аппки"""
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton(
            text="🚀 Открыть мини-приложение",
            web_app=WebAppInfo(url=WEBAPP_URL)
        )]]
    )
    update.message.reply_text(
        "Привет! Нажми кнопку ниже, чтобы открыть мини-приложение:",
        reply_markup=keyboard
    )


def main() -> None:
    """Точка входа"""
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    # Для Render: PORT приходит из переменной окружения
    import os
    port = int(os.environ.get("PORT", "8443"))
    # Запускаем webhook (или можете оставить polling для локального теста)
    if os.environ.get("RENDER"):
        updater.start_webhook(
            listen="0.0.0.0",
            port=port,
            url_path=TOKEN,
            webhook_url=f"https://{os.environ['RENDER_EXTERNAL_HOSTNAME']}/{TOKEN}"
        )
    else:
        updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
