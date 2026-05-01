import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

# Security: whitelist Vivian's Telegram user ID
# Leave empty to allow all users (not recommended for production)
_raw_ids = os.getenv("ALLOWED_TELEGRAM_USER_IDS", "")
ALLOWED_USER_IDS: set[int] = (
    {int(uid.strip()) for uid in _raw_ids.split(",") if uid.strip()}
    if _raw_ids.strip()
    else set()
)

# Conversation history: number of messages to retain per user
MAX_HISTORY_MESSAGES = 40  # 20 turns
