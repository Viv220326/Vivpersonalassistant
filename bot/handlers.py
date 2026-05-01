import logging

from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes

from bot.config import ALLOWED_USER_IDS
from bot.ai_operator import MarketingOperator

logger = logging.getLogger(__name__)

operator = MarketingOperator()

TELEGRAM_MAX_LENGTH = 4096


def _is_allowed(user_id: int) -> bool:
    if not ALLOWED_USER_IDS:
        return True
    return user_id in ALLOWED_USER_IDS


def _split_message(text: str) -> list[str]:
    if len(text) <= TELEGRAM_MAX_LENGTH:
        return [text]
    chunks = []
    while text:
        chunks.append(text[:TELEGRAM_MAX_LENGTH])
        text = text[TELEGRAM_MAX_LENGTH:]
    return chunks


async def _send(update: Update, text: str) -> None:
    for chunk in _split_message(text):
        await update.message.reply_text(chunk)


async def handle_start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    logger.info(f"SETUP_USER_ID={user_id}")
    if not _is_allowed(user_id):
        await update.message.reply_text("Access denied.")
        return
    await update.message.reply_text(
        f"Viv Personal Assistant online.\n\nYour Telegram user ID: {user_id}\n\n"
        "Commands:\n"
        "/clear — Reset conversation history\n"
        "/brief — Daily briefing request\n"
        "/task [description] — Log a task\n"
        "/caption [brand] [context] — Draft a caption\n"
        "/campaign [brand] [brief] — Start a campaign plan\n"
        "/help — Show this message"
    )


async def handle_help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await handle_start(update, context)


async def handle_clear(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if not _is_allowed(user_id):
        await update.message.reply_text("Access denied.")
        return
    operator.clear_history(user_id)
    await update.message.reply_text("Conversation history cleared.")


async def handle_brief(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if not _is_allowed(user_id):
        await update.message.reply_text("Access denied.")
        return
    await update.message.chat.send_action(ChatAction.TYPING)
    prompt = "Give me a morning briefing. Summarise what I should focus on today based on our recurring responsibilities and any open items."
    response = operator.get_response(user_id, prompt)
    await _send(update, response)


async def handle_task(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if not _is_allowed(user_id):
        await update.message.reply_text("Access denied.")
        return
    description = " ".join(context.args) if context.args else ""
    if not description:
        await update.message.reply_text("Usage: /task [description]")
        return
    await update.message.chat.send_action(ChatAction.TYPING)
    prompt = f"Log and structure this task: {description}"
    response = operator.get_response(user_id, prompt)
    await _send(update, response)


async def handle_caption(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if not _is_allowed(user_id):
        await update.message.reply_text("Access denied.")
        return
    args_text = " ".join(context.args) if context.args else ""
    if not args_text:
        await update.message.reply_text(
            "Usage: /caption [brand] [context]\n"
            "Example: /caption tbp Saturday dinner service with a new dish launch"
        )
        return
    await update.message.chat.send_action(ChatAction.TYPING)
    prompt = f"Draft a caption. {args_text}"
    response = operator.get_response(user_id, prompt)
    await _send(update, response)


async def handle_campaign(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if not _is_allowed(user_id):
        await update.message.reply_text("Access denied.")
        return
    args_text = " ".join(context.args) if context.args else ""
    if not args_text:
        await update.message.reply_text(
            "Usage: /campaign [brand] [brief]\n"
            "Example: /campaign udon shin Q3 relaunch targeting young professionals"
        )
        return
    await update.message.chat.send_action(ChatAction.TYPING)
    prompt = f"Build a campaign plan. {args_text}"
    response = operator.get_response(user_id, prompt)
    await _send(update, response)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if not _is_allowed(user_id):
        await update.message.reply_text("Access denied.")
        return
    text = update.message.text or ""
    if not text.strip():
        return
    await update.message.chat.send_action(ChatAction.TYPING)
    response = operator.get_response(user_id, text)
    await _send(update, response)
