# Canvas → Discord Notification Webhook

Get notified in Discord when Canvas assignments and discussions are coming due. This script scrapes the Canvas LMS API for your enrolled courses and posts a clean summary to a Discord channel via webhook.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

## What It Does

- Pulls all your **active courses** from Canvas
- Finds **assignments** and **discussions** due within a configurable window (default 7 days)
- Sorts everything by due date (soonest first)
- Groups items by course and posts color-coded embeds to Discord
- Shows a countdown (e.g. `2d 5h left`) and links directly to each item on Canvas

## Prerequisites

- **Python 3.8+** installed on your machine
- A **Canvas LMS** account with API access
- A **Discord** server where you can create webhooks

---

## Setup Guide

### Step 1 — Clone the Repository

```bash
git clone https://github.com/lunad3lsol/Canvas-Noti.git
cd Canvas-Noti
```

### Step 2 — Create a Python Virtual Environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate          # Windows
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Generate a Canvas API Token

1. Log in to your school's Canvas site (e.g. `https://myschool.instructure.com`).
2. Click your **profile picture** (top-left) → **Settings**.
3. Scroll down to **Approved Integrations**.
4. Click **+ New Access Token**.
5. Give it a purpose (e.g. `Discord Notifier`) and click **Generate Token**.
6. **Copy the token immediately** — you won't be able to see it again.

> Your Canvas base URL is whatever is in your browser's address bar before `/courses/...`
> Example: `https://myschool.instructure.com`

### Step 5 — Create a Discord Webhook

1. Open **Discord** and go to the server/channel where you want notifications.
2. Click the **gear icon** next to the channel name → **Integrations** → **Webhooks**.
3. Click **New Webhook**.
4. Give it a name (e.g. `Canvas Notifier`) and optionally set an avatar.
5. Click **Copy Webhook URL**.

### Step 6 — Configure Environment Variables

```bash
cp .env.example .env
```

Open `.env` in your editor and fill in your values:

```env
CANVAS_API_URL=https://myschool.instructure.com
CANVAS_API_TOKEN=paste_your_canvas_token_here
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
DAYS_AHEAD=7
NOTIFY_ASSIGNMENTS=true
NOTIFY_DISCUSSIONS=true
```

| Variable | Required | Description |
|---|---|---|
| `CANVAS_API_URL` | Yes | Your school's Canvas base URL |
| `CANVAS_API_TOKEN` | Yes | The API token from Step 4 |
| `DISCORD_WEBHOOK_URL` | Yes | The webhook URL from Step 5 |
| `DAYS_AHEAD` | No | Number of days to look ahead (default `7`) |
| `NOTIFY_ASSIGNMENTS` | No | Include assignments (`true`/`false`, default `true`) |
| `NOTIFY_DISCUSSIONS` | No | Include discussions (`true`/`false`, default `true`) |

### Step 7 — Run It

```bash
python canvas_notifier.py
```

You should see output like:

```
Fetching upcoming items (next 7 days) from Canvas...
Found 4 upcoming item(s).
Sent 3 embed(s) to Discord.
Done!
```

Check your Discord channel — you'll see color-coded embeds grouped by course.

---

## Running on a Schedule (Optional)

To get notifications automatically (e.g. every morning), set up a cron job or Task Scheduler.

### Linux / macOS — cron

```bash
crontab -e
```

Add a line to run every day at 8 AM:

```
0 8 * * * cd /path/to/Canvas-Noti && /path/to/venv/bin/python canvas_notifier.py
```

> Replace `/path/to/` with your actual paths. Use `which python` inside your venv to find the full python path.

### Windows — Task Scheduler

1. Open **Task Scheduler** and create a new task.
2. Set the trigger to **Daily** at your preferred time.
3. Set the action to run:
   - Program: `C:\path\to\venv\Scripts\python.exe`
   - Arguments: `canvas_notifier.py`
   - Start in: `C:\path\to\Canvas-Noti`

---

## Customization

### Change the look-ahead window

Set `DAYS_AHEAD` in your `.env` to any number. For example, `DAYS_AHEAD=3` only shows items due in the next 3 days.

### Disable discussions or assignments

Set `NOTIFY_DISCUSSIONS=false` or `NOTIFY_ASSIGNMENTS=false` in `.env` to skip those types.

### Embed colors

The embeds use these colors:
- **Blue** — summary header
- **Orange** — course with upcoming items
- **Red** — course with items due very soon (under 1 hour or past due)
- **Green** — nothing due (all caught up)

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `Error: missing environment variables` | Make sure you copied `.env.example` to `.env` and filled in all required values |
| `401 Unauthorized` from Canvas | Your API token is invalid or expired — generate a new one in Canvas Settings |
| `404 Not Found` from Canvas | Double-check your `CANVAS_API_URL` — it should be the base URL with no trailing slash |
| `400/401` from Discord | Your webhook URL is wrong or the webhook was deleted — create a new one |
| No items found | Try increasing `DAYS_AHEAD`, or check that you have active course enrollments |

---

## Project Structure

```
Canvas-Noti/
├── canvas_notifier.py   # Main script
├── .env.example         # Template for environment variables
├── .env                 # Your local config (git-ignored)
├── requirements.txt     # Python dependencies
├── .gitignore
└── README.md
```

## License

Do whatever you want with it.
