# bing-rewards-bot

Automates daily Bing searches on Microsoft Rewards across multiple Edge profiles. Runs in a completely separate browser window so you can use your main Edge normally while it grinds points in the background.

---

## Features

- Auto-detects all your Edge profiles — no manual config
- Completely separate from your real Edge — no conflicts, no crashes
- One-time login setup per profile, then fully automated forever
- Randomized searches from a pool of 90+ queries every run
- Set how many searches to run each time
- Pause / Resume with `P`
- Quit early with `Q`
- Closes each tab after searching

---

## Requirements

- Windows
- Python 3.x → [python.org](https://www.python.org/downloads/)
- Microsoft Edge
- Edge WebDriver (must match your Edge version)

---

## Installation

### 1. Clone the repo

```bash
git clone https://github.com/Aarush-Arora/bing-rewards-bot.git
cd bing-rewards-bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## How Profile Detection Works

The script automatically scans your Edge installation and lists all profiles it finds — no hardcoding, no config files, works on any machine out of the box.

When you run it, you'll see something like:

```
Detected Edge profiles:
  1 — John (Default)
  2 — Doe (Profile 3)
  3 — Will (Profile 8)
  4 — Smith (Profile 9)

Enter profile number:
```

**Important:** The script runs on one profile per run. To set up multiple profiles, just run it again and pick a different one each time. Each profile only needs the one-time login setup once — after that it's remembered forever.

---

## First-Time Login (per profile)

The bot uses a completely separate Edge directory (`RewardsBot`) so it never conflicts with your real Edge. The downside is you need to log in once per profile the first time.

Here's what happens on first run for any profile:

1. Run the script and select a profile
2. A new Edge window opens
3. Log into your Microsoft account in that window
4. Go to [rewards.microsoft.com](https://rewards.microsoft.com) and confirm everything looks good
5. Press Enter in the terminal
6. Done — session is saved, won't ask again for that profile

Repeat for each profile you want to use. After that, every run is fully automatic.

> Don't delete the `RewardsBot` folder at `C:\Users\yourname\AppData\Local\Microsoft\Edge\RewardsBot` or you'll have to log in again.

---

## Running

```bash
cd bing-rewards-bot
rewards script.py
```

You'll be prompted to:
1. Pick a profile from the auto-detected list
2. Enter how many searches to run

Then just leave it — use your PC normally while it runs in the background.

**Controls while running:**
| Key | Action |
|-----|--------|
| `P` | Pause / Resume |
| `Q` | Quit early |

---

## Notes

- Gold members get **60 points/day** from searches (20 searches × 3pts)
- Silver members cap at **30 points/day** (10 searches × 3pts)
- Basic members cap at **15 points/day** (5 searches × 3pts)
- Searches are randomized every run so the pattern never looks the same
- Delays between searches are randomized to look human
- If Microsoft flags unusual activity, increase the delay values in the script (`random.uniform(10, 16)`)
- Referral points from friends' searches are separate from your own daily cap

---

## Disclaimer

This is for personal use. Automating searches technically violates Microsoft Rewards ToS — use at your own risk. Don't go crazy with it.
