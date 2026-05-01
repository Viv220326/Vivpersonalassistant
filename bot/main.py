import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from bot.config import TELEGRAM_BOT_TOKEN
from bot.handlers import (
    handle_start,
    handle_help,
    handle_clear,
    handle_brief,
    handle_task,
    handle_caption,
    handle_campaign,
    handle_message,
)

logging.basicConfig(
    format="%(asctime)s — %(name)s — %(levelname)s — %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def main() -> None:
    if not TELEGRAM_BOT_TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN is not set. Add it to your .env file.")

    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", handle_start))
    app.add_handler(CommandHandler("help", handle_help))
    app.add_handler(CommandHandler("clear", handle_clear))
    app.add_handler(CommandHandler("brief", handle_brief))
    app.add_handler(CommandHandler("task", handle_task))
    app.add_handler(CommandHandler("caption", handle_caption))
    app.add_handler(CommandHandler("campaign", handle_campaign))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("Viv Personal Assistant starting...")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
