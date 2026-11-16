# Daily Dynamics Job Alert — Rohini Ramtekkar

A self-contained Python system that scans job sources every day, matches postings
against Rohini's resume (Dynamics 365, Power Apps, Power Automate, Azure DevOps,
CRM, PL-400, etc.), and alerts about **new** relevant jobs — never duplicates.

This is a **separate repository** from your own job-alert system. It has its own
Telegram bot, chat ID, resume, and `seen_jobs.json` for deduplication.

## Files

```
job-alert-rohini/
├── resume.txt                  # Rohini's resume
├── config.yaml                 # your real config (created from config.yaml.example)
├── config.yaml.example
├── .env                        # your secrets (JOBALERT_* env vars)
├── .env.example
├── main.py                     # entry point
├── requirements.txt
├── README.md
├── .gitignore
├── .github/workflows/daily-job-alert.yml   # GitHub Actions: daily at 9 AM IST
└── src/
    ├── config.py               # config loading
    ├── models.py               # Job, Profile data models
    ├── resume_parser.py        # extracts skills/experience from resume.txt
    ├── matcher.py              # scores jobs (skills, title, location, recency)
    ├── state.py                # data/seen_jobs.json — remembers notified jobs
    ├── notify.py               # console + Telegram notifications
    ├── scheduler.py            # local Task Scheduler / cron helper
    └── sources/
        ├── base.py             # Source ABC
        ├── demo.py             # sample jobs for testing
        ├── rapidapi.py         # RapidAPI JSearch adapter
        └── rss.py              # generic RSS feed adapter
```

## Quick start (local test)

```powershell
cd "path\to\job-alert-rohini"
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install requests pyyaml

# Edit config.yaml with your RapidAPI key and Telegram settings
# Edit .env with your secrets (optional)

# Test with built-in demo jobs
python main.py --demo

# Real scan with RapidAPI
python main.py --run-once
```

## Run daily on GitHub Actions (recommended)

The workflow runs every day at **9:00 AM IST** (03:30 UTC).

### One-time setup

1. **Push this repo to GitHub** as `job-alert-rohini` (separate repo from your job-alert).

2. **Create a Telegram bot** — message [@BotFather](https://t.me/botfather), run `/newbot`, note the bot token.

3. **Get your chat ID** — send a message to your bot, then visit:
   `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
   Find `"chat":{"id":...}` — that's the chat ID.

4. **Add GitHub repo secrets** — Settings → Secrets and variables → Actions → New repository secret:
   | Secret | Value |
   |--------|-------|
   | `RAPIDAPI_KEY` | your RapidAPI key (from rapidapi.com) |
   | `TELEGRAM_BOT_TOKEN` | from @BotFather |
   | `TELEGRAM_CHAT_ID` | the chat ID from step 3 |

5. The workflow commits `data/seen_jobs.json` back after each run, so deduplication
   persists across days — you only see *new* jobs.

## Telegram message format

Each relevant job is sent as its own message:

```
💼 Job 1/3
💼 Role: Dynamics 365 Developer
🏢 Company: XYZ Ltd.
📍 Location: Pune, Maharashtra, IN
🔑 Key skills: Dynamics 365, Power Apps, Power Automate, Azure DevOps | 📅 Experience: Not specified
⭐ Match score: 0.95
🔗 Apply: https://linkedin.com/jobs/view/...
```

A header message is sent first with the date, time, and counts:

```
🔔 Dynamics Job Alert — Daily Digest
📅 Date: 13 Nov 2026
🕐 Time: 09:00 AM IST
✅ Relevant jobs found: 3
📎 Maybe / lower confidence: 1
🔄 Duplicates removed: 2
```

## Customizing

Edit `resume.txt` whenever skills change. Edit `config.yaml` to add/remove search
queries, locations, or blocked domains (e.g. paywalled job boards).

## Disclaimer

This tool is for personal job-search assistance. Respect each job board's
Terms of Service; do not add scrapers that bypass login walls or rate limits.
