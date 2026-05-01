# Gmail Integration — Setup Guide

## Account

`220326vpa@gmail.com`

---

## Purpose

Surface email and calendar context to the AI operator so it can:
- Include meeting and deadline context in daily briefs
- Flag scheduling conflicts when planning campaigns
- Remind Vivian of upcoming deadlines tied to content or campaigns
- Draft email replies for Vivian's review (never send without approval)

---

## What's Needed

| Item | Status | Notes |
|---|---|---|
| Gmail account | ✅ Confirmed | 220326vpa@gmail.com |
| Google Cloud project | ⏳ Pending | Free to create at console.cloud.google.com |
| OAuth2 credentials | ⏳ Pending | Client ID + Secret from Google Cloud |
| Refresh token | ⏳ Pending | Obtained via one-time OAuth2 flow |

---

## Access Scopes

Read-only to start:
- `https://www.googleapis.com/auth/gmail.readonly` — read emails
- `https://www.googleapis.com/auth/calendar.readonly` — read Google Calendar events

Write access (draft only, never send):
- `https://www.googleapis.com/auth/gmail.compose` — create drafts only

No emails are sent without Vivian's explicit approval.

---

## Integration Flow

```
Daily brief requested (or scheduled)
        ↓
Gmail API: fetch unread emails + flagged items
Google Calendar API: fetch today's + this week's events
        ↓
AI operator surfaces relevant items:
  - Emails needing a response
  - Meetings with prep needed
  - Deadlines tied to active campaigns
        ↓
Delivered via Telegram morning brief
```

---

## Environment Variables Required

```
GMAIL_CLIENT_ID=<from Google Cloud console>
GMAIL_CLIENT_SECRET=<from Google Cloud console>
GMAIL_REFRESH_TOKEN=<obtained via OAuth2 flow>
GMAIL_USER_EMAIL=220326vpa@gmail.com
```

---

## Setup Steps (when ready to connect)

1. Go to console.cloud.google.com — create a new project
2. Enable Gmail API and Google Calendar API
3. Create OAuth2 credentials (Desktop app type)
4. Download the client secret JSON
5. Run the one-time auth flow to generate a refresh token
6. Store all credentials in `.env` (never in repo)

---

## Notes

- Google OAuth2 refresh tokens don't expire unless revoked or unused for 6 months
- Keep the account signed in and active to avoid token expiry
- All Gmail access is read-only by default — compose scope only added when email drafting is enabled
