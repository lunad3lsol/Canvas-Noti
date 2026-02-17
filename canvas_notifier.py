#!/usr/bin/env python3
"""
Canvas → Discord Webhook Notifier

Scrapes your Canvas LMS courses for upcoming assignments and discussions,
then posts a summary to a Discord channel via webhook.
"""

import os
import sys
import requests
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()

# ── Configuration ───────────────────────────────────────────────────────────
CANVAS_API_URL = os.getenv("CANVAS_API_URL", "").rstrip("/")
CANVAS_API_TOKEN = os.getenv("CANVAS_API_TOKEN", "")
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL", "")
DAYS_AHEAD = int(os.getenv("DAYS_AHEAD", "7"))
NOTIFY_ASSIGNMENTS = os.getenv("NOTIFY_ASSIGNMENTS", "true").lower() == "true"
NOTIFY_DISCUSSIONS = os.getenv("NOTIFY_DISCUSSIONS", "true").lower() == "true"


def validate_config():
    """Make sure all required env vars are set."""
    missing = []
    if not CANVAS_API_URL:
        missing.append("CANVAS_API_URL")
    if not CANVAS_API_TOKEN:
        missing.append("CANVAS_API_TOKEN")
    if not DISCORD_WEBHOOK_URL:
        missing.append("DISCORD_WEBHOOK_URL")
    if missing:
        print(f"Error: missing environment variables: {', '.join(missing)}")
        print("Copy .env.example to .env and fill in your values.")
        sys.exit(1)


# ── Canvas API helpers ──────────────────────────────────────────────────────
HEADERS = {}


def init_headers():
    global HEADERS
    HEADERS = {"Authorization": f"Bearer {CANVAS_API_TOKEN}"}


def canvas_get(endpoint):
    """GET a Canvas API endpoint, handling pagination."""
    url = f"{CANVAS_API_URL}/api/v1/{endpoint}"
    results = []
    while url:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        results.extend(resp.json())
        # Canvas uses Link header for pagination
        url = None
        if "Link" in resp.headers:
            for part in resp.headers["Link"].split(","):
                if 'rel="next"' in part:
                    url = part.split("<")[1].split(">")[0]
    return results


def get_courses():
    """Return the user's active courses."""
    courses = canvas_get(
        "courses?enrollment_state=active&per_page=100"
    )
    return courses


def get_assignments(course_id):
    """Return assignments for a course."""
    return canvas_get(
        f"courses/{course_id}/assignments"
        f"?per_page=100&order_by=due_at"
    )


def get_discussions(course_id):
    """Return graded discussion topics for a course."""
    return canvas_get(
        f"courses/{course_id}/discussion_topics"
        f"?per_page=100&order_by=recent_activity"
    )


# ── Filtering ───────────────────────────────────────────────────────────────
def is_upcoming(due_str):
    """Check whether a due date string falls within the look-ahead window."""
    if not due_str:
        return False
    try:
        due = datetime.fromisoformat(due_str.replace("Z", "+00:00"))
    except ValueError:
        return False
    now = datetime.now(timezone.utc)
    delta = due - now
    return 0 <= delta.total_seconds() <= DAYS_AHEAD * 86400


def friendly_date(due_str):
    """Convert an ISO date to a readable string."""
    if not due_str:
        return "No due date"
    try:
        due = datetime.fromisoformat(due_str.replace("Z", "+00:00"))
    except ValueError:
        return due_str
    return due.strftime("%a %b %d, %I:%M %p %Z")


def time_until(due_str):
    """Return a human-readable countdown string."""
    if not due_str:
        return ""
    try:
        due = datetime.fromisoformat(due_str.replace("Z", "+00:00"))
    except ValueError:
        return ""
    now = datetime.now(timezone.utc)
    delta = due - now
    total_seconds = int(delta.total_seconds())
    if total_seconds < 0:
        return "**PAST DUE**"
    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    if days > 0:
        return f"{days}d {hours}h left"
    if hours > 0:
        minutes = (total_seconds % 3600) // 60
        return f"{hours}h {minutes}m left"
    minutes = total_seconds // 60
    return f"**{minutes}m left!**"


# ── Collect upcoming items ──────────────────────────────────────────────────
def collect_upcoming():
    """Scrape Canvas and return categorised upcoming items."""
    courses = get_courses()
    items = []

    for course in courses:
        course_id = course.get("id")
        course_name = course.get("name", "Unknown Course")

        # Assignments
        if NOTIFY_ASSIGNMENTS:
            try:
                assignments = get_assignments(course_id)
            except requests.HTTPError:
                assignments = []

            for a in assignments:
                due = a.get("due_at")
                if is_upcoming(due):
                    items.append({
                        "type": "Assignment",
                        "course": course_name,
                        "name": a.get("name", "Untitled"),
                        "due": due,
                        "url": a.get("html_url", ""),
                        "points": a.get("points_possible"),
                    })

        # Discussions
        if NOTIFY_DISCUSSIONS:
            try:
                discussions = get_discussions(course_id)
            except requests.HTTPError:
                discussions = []

            for d in discussions:
                due = d.get("assignment", {}).get("due_at") if d.get("assignment") else None
                if due and is_upcoming(due):
                    items.append({
                        "type": "Discussion",
                        "course": course_name,
                        "name": d.get("title", "Untitled"),
                        "due": due,
                        "url": d.get("html_url", ""),
                        "points": d.get("assignment", {}).get("points_possible"),
                    })

    # Sort by due date (soonest first)
    items.sort(key=lambda x: x["due"])
    return items


# ── Discord message builder ────────────────────────────────────────────────
def build_embeds(items):
    """Build Discord embed objects from collected items."""
    if not items:
        return [{
            "title": "Canvas Notifications",
            "description": (
                f"No upcoming assignments or discussions "
                f"in the next **{DAYS_AHEAD} day(s)**. You're all caught up!"
            ),
            "color": 0x2ECC71,  # green
        }]

    # Group items by course
    by_course = {}
    for item in items:
        by_course.setdefault(item["course"], []).append(item)

    embeds = []
    # Summary embed
    embeds.append({
        "title": f"📋 Canvas — {len(items)} upcoming item(s)",
        "description": f"Due within the next **{DAYS_AHEAD} day(s)**",
        "color": 0x3498DB,  # blue
    })

    for course, course_items in by_course.items():
        lines = []
        for item in course_items:
            icon = "📝" if item["type"] == "Assignment" else "💬"
            pts = f" ({int(item['points'])} pts)" if item.get("points") else ""
            countdown = time_until(item["due"])
            link = f"[{item['name']}]({item['url']})" if item["url"] else item["name"]
            lines.append(
                f"{icon} **{item['type']}**: {link}{pts}\n"
                f"   ⏰ {friendly_date(item['due'])} — {countdown}"
            )

        embeds.append({
            "title": course,
            "description": "\n\n".join(lines),
            "color": 0xE74C3C if any(
                "PAST DUE" in time_until(i["due"]) or
                "m left!" in time_until(i["due"])
                for i in course_items
            ) else 0xF39C12,  # red for urgent, orange otherwise
        })

    return embeds


def send_discord(embeds):
    """Post embeds to the Discord webhook."""
    # Discord allows max 10 embeds per message
    for i in range(0, len(embeds), 10):
        payload = {"embeds": embeds[i:i + 10]}
        resp = requests.post(DISCORD_WEBHOOK_URL, json=payload, timeout=30)
        resp.raise_for_status()
    print(f"Sent {len(embeds)} embed(s) to Discord.")


# ── Main ────────────────────────────────────────────────────────────────────
def main():
    validate_config()
    init_headers()

    print(f"Fetching upcoming items (next {DAYS_AHEAD} days) from Canvas...")
    items = collect_upcoming()
    print(f"Found {len(items)} upcoming item(s).")

    embeds = build_embeds(items)
    send_discord(embeds)
    print("Done!")


if __name__ == "__main__":
    main()
