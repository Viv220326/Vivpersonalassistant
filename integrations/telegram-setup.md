# Telegram Integration — Setup Guide

## Bot Details

- **Bot Username**: @Vivian_Personal_Assistantbot
- **Bot URL**: t.me/Vivian_Personal_Assistantbot

---

## What's Needed

| Item | Status | Notes |
|---|---|---|
| Bot token (from BotFather) | ⏳ Pending | Format: `123456789:ABCdef...` |
| Webhook or polling setup | ⏳ Pending | Depends on hosting decision |
| Notion API key | ⏳ Pending | For task logging from Telegram |

---

## Intended Workflow

```
Vivian sends message on Telegram
        ↓
Bot receives message
        ↓
AI operator interprets intent
        ↓
Drafts output / asks clarifying question
        ↓
Vivian approves or redirects
        ↓
(If approved) Logs task to Notion
```

---

## Command Structure (Planned)

| Command | Action |
|---|---|
| `/task [description]` | Log a new task to Notion Master Board |
| `/caption [brand] [context]` | Draft a caption using the brand template |
| `/campaign [brand] [brief]` | Start a campaign plan structure |
| `/brief` | Get today's task and calendar summary |
| `/status` | Get status of active campaigns |
| `/report [brand]` | Request latest performance summary |

---

## Environment Variables Required

Store securely — never commit to repository:

```
TELEGRAM_BOT_TOKEN=<from BotFather>
NOTION_API_KEY=<from Notion integration settings>
NOTION_TASKS_DB_ID=<from Notion database URL>
NOTION_CAMPAIGNS_DB_ID=<from Notion database URL>
NOTION_CONTENT_DB_ID=<from Notion database URL>
```

---

## Security Notes

- Bot token must never be committed to the repository
- Store in `.env` file (gitignored) or a secrets manager
- Restrict bot to Vivian's Telegram account only (whitelist by user ID)
