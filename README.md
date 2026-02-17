# Canvas → Discord Notification Webhook

Get notified in Discord when your Canvas assignments and discussions are coming due. This script checks your Canvas courses and sends a clean summary to a Discord channel.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

## What You'll Get

When you run this script, it posts a message to your Discord channel that looks like this:

- A **blue header** showing how many items are due soon
- **Course-by-course breakdown** with each assignment/discussion listed
- **Direct links** to each item on Canvas (just click to open it)
- A **countdown** next to each item (e.g. `2d 5h left` or `45m left!`)
- Items due very soon show up in **red** so you don't miss them

---

## Before You Start — Install Python

You need Python installed on your computer. If you already have it, skip to Step 1.

### Check if you already have Python

<details>
<summary><strong>Windows</strong></summary>

1. Press the **Windows key** on your keyboard (the key with the Windows logo, bottom-left).
2. Type `cmd` and press **Enter**. This opens the **Command Prompt** (a black window where you type commands).
3. Type this and press **Enter**:
   ```
   python --version
   ```
4. If you see something like `Python 3.10.6`, you're good — skip to **Step 1**.
5. If you see `'python' is not recognized...`, you need to install Python. Keep reading.

</details>

<details>
<summary><strong>macOS</strong></summary>

1. Press **Cmd + Space** to open Spotlight Search.
2. Type `Terminal` and press **Enter**. This opens the **Terminal** (a window where you type commands).
3. Type this and press **Enter**:
   ```
   python3 --version
   ```
4. If you see something like `Python 3.10.6`, you're good — skip to **Step 1**.
5. If you get an error, you need to install Python. Keep reading.

</details>

<details>
<summary><strong>Linux</strong></summary>

1. Open your **Terminal** (usually Ctrl+Alt+T).
2. Type this and press **Enter**:
   ```
   python3 --version
   ```
3. If you see something like `Python 3.10.6`, you're good — skip to **Step 1**.
4. If not, install it:
   ```
   sudo apt update && sudo apt install python3 python3-pip python3-venv
   ```

</details>

### Installing Python (if you don't have it)

<details>
<summary><strong>Windows — Install Python</strong></summary>

1. Open your web browser and go to: **https://www.python.org/downloads/**
2. Click the big yellow **"Download Python 3.x.x"** button.
3. Open the downloaded file (it'll be in your Downloads folder).
4. **IMPORTANT**: On the first screen of the installer, check the box that says **"Add python.exe to PATH"** at the bottom. This is critical!
5. Click **"Install Now"**.
6. Wait for it to finish, then click **"Close"**.
7. Close any open Command Prompt windows and open a new one (Windows key → type `cmd` → Enter).
8. Verify it worked:
   ```
   python --version
   ```
   You should see `Python 3.x.x`.

</details>

<details>
<summary><strong>macOS — Install Python</strong></summary>

1. Open your web browser and go to: **https://www.python.org/downloads/**
2. Click the big yellow **"Download Python 3.x.x"** button.
3. Open the downloaded `.pkg` file from your Downloads folder.
4. Click through the installer (Continue → Continue → Agree → Install).
5. Enter your Mac password when prompted.
6. Close any open Terminal windows and open a new one (Cmd+Space → type `Terminal` → Enter).
7. Verify it worked:
   ```
   python3 --version
   ```
   You should see `Python 3.x.x`.

</details>

---

## Step 1 — Download This Project

You have two options: **use git** (if you have it) or **download the ZIP** (easier).

### Option A — Download the ZIP (easiest)

1. On this GitHub page, click the green **"<> Code"** button near the top.
2. Click **"Download ZIP"**.
3. Find the downloaded ZIP file in your **Downloads** folder.
4. **Extract/unzip** it:
   - **Windows**: Right-click the ZIP → **"Extract All..."** → click **"Extract"**.
   - **macOS**: Double-click the ZIP file. It will create a folder automatically.
5. You now have a folder called `Canvas-Noti-main` (or similar). Remember where it is — you'll need the path in a moment.

### Option B — Clone with git

If you have git installed, open your terminal and run:

```bash
git clone https://github.com/lunad3lsol/Canvas-Noti.git
```

---

## Step 2 — Open a Terminal in the Project Folder

You need to open a terminal/command prompt and navigate to the project folder.

<details>
<summary><strong>Windows</strong></summary>

1. Open **File Explorer** and navigate to the `Canvas-Noti` folder you downloaded/cloned.
2. Click on the **address bar** at the top of File Explorer (where it shows the folder path).
3. Type `cmd` and press **Enter**. A Command Prompt window will open, already pointed at the right folder.

**Alternatively**, you can do it manually:

1. Press the **Windows key**, type `cmd`, press **Enter**.
2. Type `cd ` (with a space after it), then drag the `Canvas-Noti` folder from File Explorer into the Command Prompt window — it will paste the folder path for you.
3. Press **Enter**.

You should see something like:
```
C:\Users\YourName\Downloads\Canvas-Noti>
```

</details>

<details>
<summary><strong>macOS</strong></summary>

1. Open **Terminal** (Cmd+Space → type `Terminal` → Enter).
2. Type `cd ` (with a space after it).
3. Open **Finder**, find the `Canvas-Noti` folder, and **drag the folder into the Terminal window** — it will paste the path for you.
4. Press **Enter**.

You should see something like:
```
user@MacBook Canvas-Noti %
```

</details>

<details>
<summary><strong>Linux</strong></summary>

1. Open your **Terminal** (Ctrl+Alt+T).
2. Navigate to the project folder:
   ```
   cd ~/Downloads/Canvas-Noti
   ```
   (Adjust the path if you put it somewhere else.)

</details>

---

## Step 3 — Set Up a Virtual Environment and Install Dependencies

This creates an isolated space for the project's packages so they don't mess with anything else on your computer.

<details>
<summary><strong>Windows</strong></summary>

In your Command Prompt (which should already be in the Canvas-Noti folder), type these commands **one at a time**, pressing **Enter** after each:

```
python -m venv venv
```

Wait for it to finish (it may take a few seconds with no output — that's normal). Then:

```
venv\Scripts\activate
```

You should see `(venv)` appear at the beginning of your command line. That means it worked! Now install the dependencies:

```
pip install -r requirements.txt
```

You'll see some download/install output. Wait until it finishes and you see your prompt again.

</details>

<details>
<summary><strong>macOS / Linux</strong></summary>

In your Terminal (which should already be in the Canvas-Noti folder), type these commands **one at a time**, pressing **Enter** after each:

```
python3 -m venv venv
```

Wait for it to finish (it may take a few seconds with no output — that's normal). Then:

```
source venv/bin/activate
```

You should see `(venv)` appear at the beginning of your command line. That means it worked! Now install the dependencies:

```
pip install -r requirements.txt
```

You'll see some download/install output. Wait until it finishes and you see your prompt again.

</details>

---

## Step 4 — Get Your Canvas API Token

You need a special "key" from Canvas that lets this script read your course data. Here's exactly how to get it:

1. **Open your web browser** and go to your school's Canvas website.
   - This is the same site you use to check grades, submit assignments, etc.
   - The URL looks something like `https://myschool.instructure.com` or `https://canvas.myschool.edu`.

2. **Log in** with your normal school credentials.

3. **Click your profile picture** (or initials) in the **top-left corner** of the page.

4. Click **"Settings"** in the menu that appears.

5. **Scroll down** the Settings page. Look for a section called **"Approved Integrations"**.

6. Click the **"+ New Access Token"** button.

7. In the popup:
   - **Purpose**: Type something like `Discord Notifier` (this is just a label for you).
   - **Expires**: You can leave this blank (it won't expire) or set a date if you prefer.
   - Click **"Generate Token"**.

8. **You'll see your token** — it's a long string of characters and numbers.
   **COPY IT RIGHT NOW** and paste it somewhere safe (like a notepad). You will **never** be able to see this token again after you close this popup.

9. Also **note your Canvas URL** — look at your browser's address bar. You need the part before any `/courses/...` path. For example:
   - If your address bar shows `https://myschool.instructure.com/courses/12345`, your Canvas URL is `https://myschool.instructure.com`

**Save both of these — you'll need them in Step 6:**
- Your **Canvas URL** (e.g. `https://myschool.instructure.com`)
- Your **API token** (the long string you just copied)

---

## Step 5 — Create a Discord Webhook

A webhook is like a special URL that lets this script post messages to your Discord channel. Here's how to create one:

1. **Open Discord** (the app on your computer or https://discord.com in your browser).

2. **Go to the server** where you want the notifications to appear.
   - If you don't have a server, you can create one: click the **"+"** button on the left sidebar → **"Create My Own"** → **"For me and my friends"** → give it a name → **"Create"**.

3. **Find the channel** you want notifications in (e.g. `#general` or create a new channel like `#canvas-notifications`).
   - To create a new channel: click the **"+"** next to "TEXT CHANNELS" → name it `canvas-notifications` → **"Create Channel"**.

4. **Click the gear icon** next to the channel name (it appears when you hover over the channel name). This opens **Channel Settings**.

5. In the left sidebar of Channel Settings, click **"Integrations"**.

6. Click **"Webhooks"**.

7. Click **"New Webhook"**.

8. You can optionally:
   - Click on the webhook name (e.g. "Spidey Bot") to rename it to something like `Canvas Notifier`.
   - Click the circle icon to upload a profile picture for the webhook.

9. Click the **"Copy Webhook URL"** button. The URL will be copied to your clipboard.

**Save this URL — you'll need it in Step 6.** It looks something like:
```
https://discord.com/api/webhooks/1234567890/abcdefghijklmnop...
```

10. Click **"Save Changes"** at the bottom, then close the settings.

---

## Step 6 — Configure the `.env` File

The `.env` file is where you paste your Canvas token and Discord webhook URL. Here's exactly how to set it up:

### 6a — Create the `.env` file

<details>
<summary><strong>Windows</strong></summary>

In your Command Prompt (still in the Canvas-Noti folder), run:

```
copy .env.example .env
```

</details>

<details>
<summary><strong>macOS / Linux</strong></summary>

In your Terminal (still in the Canvas-Noti folder), run:

```
cp .env.example .env
```

</details>

### 6b — Edit the `.env` file

Now you need to open the `.env` file in a text editor and paste in your values.

<details>
<summary><strong>Windows — Using Notepad</strong></summary>

In your Command Prompt, run:
```
notepad .env
```

This will open the file in Notepad.

</details>

<details>
<summary><strong>macOS — Using TextEdit</strong></summary>

In your Terminal, run:
```
open -a TextEdit .env
```

This will open the file in TextEdit.

</details>

<details>
<summary><strong>Linux — Using nano</strong></summary>

In your Terminal, run:
```
nano .env
```

This will open the file in the terminal text editor. (When done editing, press `Ctrl+O` to save, then `Ctrl+X` to exit.)

</details>

<details>
<summary><strong>Any OS — Using VS Code</strong></summary>

If you have VS Code installed, run:
```
code .env
```

</details>

### 6c — Fill in your values

The file will look like this:

```env
CANVAS_API_URL=https://YOUR_SCHOOL.instructure.com
CANVAS_API_TOKEN=your_canvas_api_token_here
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/your_webhook_id/your_webhook_token
DAYS_AHEAD=7
NOTIFY_ASSIGNMENTS=true
NOTIFY_DISCUSSIONS=true
```

**Replace the placeholder values** with your actual values. Here is what to change:

| Line | What to do |
|---|---|
| `CANVAS_API_URL=` | Replace `https://YOUR_SCHOOL.instructure.com` with your actual Canvas URL from Step 4 |
| `CANVAS_API_TOKEN=` | Replace `your_canvas_api_token_here` with the token you copied in Step 4 |
| `DISCORD_WEBHOOK_URL=` | Replace the placeholder with the webhook URL you copied in Step 5 |
| `DAYS_AHEAD=` | How many days ahead to look. `7` means show items due in the next week. Change to `3` for 3 days, `14` for 2 weeks, etc. |
| `NOTIFY_ASSIGNMENTS=` | Set to `true` to see assignments, `false` to hide them |
| `NOTIFY_DISCUSSIONS=` | Set to `true` to see discussions, `false` to hide them |

**Example of a filled-in `.env` file:**

```env
CANVAS_API_URL=https://university.instructure.com
CANVAS_API_TOKEN=7~AbCdEfGhIjKlMnOpQrStUvWxYz1234567890abcdef
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/1145234567890/aB3dE_fGhIjK-lMnOpQrStUvWxYz12345
DAYS_AHEAD=7
NOTIFY_ASSIGNMENTS=true
NOTIFY_DISCUSSIONS=true
```

**Important:**
- Do NOT add quotes around the values.
- Do NOT add spaces around the `=` sign.
- Make sure there's no extra whitespace at the end of each line.

**Save the file** and close the editor.

---

## Step 7 — Run It!

Make sure you're still in the `Canvas-Noti` folder in your terminal and that your virtual environment is active (you should see `(venv)` at the start of your prompt).

> **Don't see `(venv)`?** Re-activate it:
> - Windows: `venv\Scripts\activate`
> - macOS/Linux: `source venv/bin/activate`

Now run the script:

<details>
<summary><strong>Windows</strong></summary>

```
python canvas_notifier.py
```

</details>

<details>
<summary><strong>macOS / Linux</strong></summary>

```
python3 canvas_notifier.py
```

</details>

### What you should see

If everything is set up correctly, the output will look like this:

```
Fetching upcoming items (next 7 days) from Canvas...
Found 4 upcoming item(s).
Sent 3 embed(s) to Discord.
Done!
```

**Now go check your Discord channel** — you should see a nicely formatted message with your upcoming assignments and discussions!

### If something went wrong

| Error message | What it means | How to fix it |
|---|---|---|
| `Error: missing environment variables: CANVAS_API_URL` | The `.env` file is missing or incomplete | Go back to Step 6 and make sure the `.env` file exists and has all 3 required values filled in |
| `401 Client Error` or `Unauthorized` | Your Canvas API token is wrong | Go back to Step 4, generate a **new** token, and update your `.env` file |
| `404 Client Error` or `Not Found` | Your Canvas URL is wrong | Double-check `CANVAS_API_URL` in your `.env`. It should be just the base URL like `https://myschool.instructure.com` with no `/` at the end and no `/courses/...` path |
| `401` error from Discord | Your webhook URL is wrong or expired | Go back to Step 5, create a new webhook, copy the URL, and update your `.env` file |
| `Found 0 upcoming item(s).` | No items are due in your look-ahead window | This might be correct! Try setting `DAYS_AHEAD=30` in your `.env` to look further ahead. Also make sure you have active course enrollments in Canvas |
| `ModuleNotFoundError: No module named 'requests'` | Dependencies aren't installed | Run `pip install -r requirements.txt` again. Make sure your venv is active (you see `(venv)` in your prompt) |
| `python is not recognized` or `command not found` | Python isn't installed or not in PATH | Go back to the "Before You Start" section and install Python. On macOS/Linux, try `python3` instead of `python` |

---

## (Optional) Run It Automatically Every Day

Instead of running the script manually each time, you can set it up to run automatically — for example, every morning at 8 AM.

<details>
<summary><strong>Windows — Task Scheduler</strong></summary>

1. Press the **Windows key**, type `Task Scheduler`, and press **Enter**.
2. In the right panel, click **"Create Basic Task..."**.
3. **Name**: type `Canvas Discord Notifier` → click **Next**.
4. **Trigger**: select **Daily** → click **Next**.
5. **Start time**: set it to when you want notifications (e.g. `8:00:00 AM`) → click **Next**.
6. **Action**: select **"Start a program"** → click **Next**.
7. Fill in:
   - **Program/script**: Click **Browse**, navigate to your `Canvas-Noti` folder → `venv` → `Scripts` → select `python.exe`.
     - The full path will look something like: `C:\Users\YourName\Downloads\Canvas-Noti\venv\Scripts\python.exe`
   - **Add arguments**: type `canvas_notifier.py`
   - **Start in**: type the full path to your Canvas-Noti folder, like `C:\Users\YourName\Downloads\Canvas-Noti`
8. Click **Next** → check **"Open the Properties dialog"** → click **Finish**.
9. In the Properties dialog, under the **General** tab, check **"Run whether user is logged on or not"**.
10. Click **OK**. Enter your Windows password if prompted.

Your computer will now run the script every day at the time you chose (as long as the computer is on).

</details>

<details>
<summary><strong>macOS / Linux — cron</strong></summary>

1. First, find the full path to your project and Python. In your Terminal (with venv active), run these two commands and **write down the output**:

   ```
   pwd
   ```
   This prints your project folder path (e.g. `/Users/yourname/Downloads/Canvas-Noti`).

   ```
   which python3
   ```
   This prints the path to Python in your venv (e.g. `/Users/yourname/Downloads/Canvas-Noti/venv/bin/python3`).

2. Open the cron editor:
   ```
   crontab -e
   ```
   - If it asks you to choose an editor, type `1` for nano (the easiest) and press Enter.

3. Add this line at the bottom of the file (replace the paths with your actual paths from step 1):

   ```
   0 8 * * * cd /Users/yourname/Downloads/Canvas-Noti && /Users/yourname/Downloads/Canvas-Noti/venv/bin/python3 canvas_notifier.py
   ```

   This means: "At minute 0, hour 8 (8:00 AM), every day, every month, every weekday."

   **Want a different time?** Change the `0 8` part:
   - `0 7` = 7:00 AM
   - `30 9` = 9:30 AM
   - `0 20` = 8:00 PM

4. Save and exit:
   - If using nano: press **Ctrl+O**, then **Enter** to save, then **Ctrl+X** to exit.

5. Verify it was saved:
   ```
   crontab -l
   ```
   You should see your line listed.

Your Mac/Linux machine will now run the script every day at the time you chose (as long as the computer is on).

</details>

---

## Customization

| Setting | Where to change it | What it does |
|---|---|---|
| `DAYS_AHEAD=7` | In your `.env` file | Controls how far ahead to look. `3` = 3 days, `14` = 2 weeks, `30` = 1 month |
| `NOTIFY_ASSIGNMENTS=false` | In your `.env` file | Set to `false` to hide assignments and only show discussions |
| `NOTIFY_DISCUSSIONS=false` | In your `.env` file | Set to `false` to hide discussions and only show assignments |

### Discord embed colors

The messages use colors to help you quickly see what's urgent:

- **Blue** — the summary header ("5 upcoming items")
- **Orange** — a course with upcoming items (you have time)
- **Red** — a course with items due **very soon** (under 1 hour or past due)
- **Green** — nothing due (you're all caught up!)

---

## Project Structure

```
Canvas-Noti/
├── canvas_notifier.py   # The main script (you run this)
├── .env.example         # Template — copy this to .env
├── .env                 # YOUR config with secrets (not tracked by git)
├── requirements.txt     # Python packages needed
├── .gitignore           # Tells git to ignore .env and other junk
└── README.md            # This file
```

## License

Do whatever you want with it.
