# Outlook Calendar Integration — Setup Guide

## Purpose

Surface daily and weekly calendar context to the AI operator so it can:
- Include meeting and deadline context in daily briefs
- Flag scheduling conflicts when planning campaigns
- Remind Vivian of upcoming deadlines tied to content or campaigns

---

## What's Needed

| Item | Status | Notes |
|---|---|---|
| Microsoft account type | ⏳ Confirm | Personal or business/M365? |
| Microsoft Graph API access | ⏳ Pending | Required for calendar read access |
| App registration (Azure AD) | ⏳ Pending | Needed for OAuth2 token |

---

## Access Model

The operator only needs **read** access to your calendar.

Scopes required:
- `Calendars.Read` — read calendar events

No write access unless explicitly enabled by Vivian.

---

## Integration Flow

```
Daily brief requested (or scheduled)
        ↓
Graph API call: fetch today's + this week's events
        ↓
AI operator surfaces relevant items:
  - Meetings with prep needed
  - Deadlines tied to active campaigns
  - Gaps suitable for deep work / reviews
        ↓
Delivered via Telegram morning brief
```

---

## Environment Variables Required

```
MICROSOFT_CLIENT_ID=<from Azure app registration>
MICROSOFT_CLIENT_SECRET=<from Azure app registration>
MICROSOFT_TENANT_ID=<your tenant ID or "common" for personal>
MICROSOFT_REFRESH_TOKEN=<obtained via OAuth2 flow>
```

---

## Setup Steps

1. Confirm account type (personal Microsoft or M365 business)
2. Register an app in Azure Active Directory (or use personal OAuth)
3. Grant `Calendars.Read` permission
4. Complete OAuth2 flow to obtain refresh token
5. Store credentials in `.env` (never in repo)

---

## Notes

- For personal Microsoft accounts, app registration is done at portal.azure.com
- For M365 business accounts, IT admin may need to grant consent
- Refresh tokens expire — system should handle re-auth gracefully
