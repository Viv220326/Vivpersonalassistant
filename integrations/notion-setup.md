# Notion Workspace Setup — Viv Personal Assistant

## Workspace Architecture

Design for two brands: **The Black Pearl (TBP)** and **Udon Shin Singapore (USS)**

---

## Database Structure

### 1. Master Task Board
**Purpose**: Daily and weekly task management across both brands.

**Properties:**
| Property | Type | Notes |
|---|---|---|
| Task | Title | Clear action verb + outcome |
| Brand | Select | The Black Pearl / Udon Shin / Both |
| Status | Select | To Do / In Progress / Awaiting Approval / Done |
| Priority | Select | High / Medium / Low |
| Due Date | Date | |
| Category | Select | Content / Campaign / Admin / Reporting / Meeting |
| Linked Campaign | Relation | → Campaigns DB |
| Notes | Text | Context or blockers |

**Views:**
- Today's Tasks (filter: due = today)
- This Week (filter: due = this week, group by brand)
- Awaiting Approval (filter: status = awaiting approval)
- By Brand (group by brand)

---

### 2. Campaigns Database
**Purpose**: Track all campaigns for both brands end-to-end.

**Properties:**
| Property | Type | Notes |
|---|---|---|
| Campaign Name | Title | |
| Brand | Select | The Black Pearl / Udon Shin |
| Status | Select | Planning / Active / Paused / Completed |
| Objective | Select | Awareness / Engagement / Reservations / Loyalty / Launch |
| Start Date | Date | |
| End Date | Date | |
| Channels | Multi-select | Instagram / Meta Ads / Google Ads / Email / PR |
| Budget | Number | Requires Vivian approval before committing |
| Key Message | Text | One-sentence campaign message |
| Campaign Brief | Files | Link to Google Drive |
| Linked Content | Relation | → Content Calendar |
| Linked Report | Relation | → Performance Reports |

**Views:**
- Active Campaigns (filter: status = active)
- Upcoming (filter: start date = next 30 days)
- By Brand
- Calendar view (by start/end date)

---

### 3. Content Calendar
**Purpose**: All content posts, approvals, and scheduling.

**Properties:**
| Property | Type | Notes |
|---|---|---|
| Post Description | Title | Brief description of content |
| Brand | Select | The Black Pearl / Udon Shin |
| Platform | Select | Instagram / Meta Ad / Google Ad / Email |
| Publish Date | Date | |
| Status | Select | Draft / Copy Ready / Assets Ready / Pending Approval / Approved / Scheduled / Published |
| Caption | Text | Final approved copy |
| Visual Brief | Text | Image/video direction |
| Asset Link | URL | Google Drive link |
| Linked Campaign | Relation | → Campaigns DB |
| Approved By | Person | Vivian Choo |

**Views:**
- Calendar (by publish date)
- Pending Approval (filter: status = pending approval)
- This Week by Brand
- Published Archive

---

### 4. Performance Reports
**Purpose**: Weekly and monthly report storage, linked to campaigns.

**Properties:**
| Property | Type | Notes |
|---|---|---|
| Report Name | Title | e.g. "TBP Weekly — W18 2026" |
| Brand | Select | |
| Period | Select | Weekly / Monthly |
| Date | Date | Report covers up to this date |
| Status | Select | Draft / In Review / Final |
| Linked Campaign | Relation | → Campaigns DB |
| Report Doc | Files | Notion page or Drive link |

---

### 5. Brand Assets Registry
**Purpose**: Quick-access links to all asset folders and reference docs.

**Properties:**
| Property | Type | Notes |
|---|---|---|
| Asset Name | Title | |
| Brand | Select | |
| Type | Select | Photography / Video / Logo / Template / Guidelines |
| Drive Link | URL | |
| Last Updated | Date | |

---

## Sidebar Navigation Structure

```
📌 Home
├── 🗓 Today's Tasks
├── 📋 This Week
└── ⏳ Awaiting Approval

📁 The Black Pearl
├── Campaigns
├── Content Calendar
└── Reports

📁 Udon Shin Singapore
├── Campaigns
├── Content Calendar
└── Reports

🗄 All Databases
├── Master Task Board
├── Campaigns DB
├── Content Calendar
├── Performance Reports
└── Brand Assets
```

---

## Setup Steps (Manual in Notion)

1. Create a new Notion workspace: **"Viv Marketing Hub"**
2. Create each database as a full-page database (not inline)
3. Set up all properties per the schema above
4. Create relations between databases (Campaigns ↔ Content ↔ Reports)
5. Build the sidebar navigation
6. Share workspace with any team members who need access
7. Add Google Drive shortcut links for each brand's asset folder

---

## Integration Notes

- Notion API key required for AI operator to log tasks programmatically
- Once API key is provided, tasks from Telegram can be auto-logged to Master Task Board
- Reports can be auto-structured and pushed to Performance Reports DB
