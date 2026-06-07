from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import keyboard
import os
import json
import getpass

all_searches = [
    "how much vram does cyberpunk 2077 use at 1440p",
    "why does thermal throttling happen in gaming laptops",
    "difference between pcie 4.0 and pcie 5.0 bandwidth",
    "how many watts does an rtx 4070 consume under load",
    "why is apple m4 chip faster than intel i9",
    "what is cache memory and why does it matter for cpus",
    "how does variable refresh rate work on monitors",
    "why do gaming laptops have worse battery life than normal laptops",
    "what is the difference between oled and amoled screens",
    "how does ram dual channel mode improve performance",
    "why does ssd speed matter for game loading times",
    "what is tdp and how does it affect laptop performance",
    "how does intel turbo boost work under load",
    "what is the difference between lpddr5 and ddr5",
    "why do laptops throttle when unplugged from power",
    "how does nvidia dlss 3.5 work technically",
    "how does a mechanical hard drive store data",
    "why is nvme faster than sata ssd",
    "what causes screen tearing while gaming",
    "what is the difference between stack and heap memory in c++",
    "how does garbage collection work in python",
    "what is the time complexity of quicksort worst case",
    "how does a hash table handle collisions",
    "what is the difference between tcp and udp protocols",
    "how does binary search work step by step",
    "what is a pointer in c and why is it dangerous",
    "how does git track changes in files internally",
    "what is the difference between process and thread",
    "how does recursion use the call stack",
    "what is dynamic programming explained with example",
    "how does a compiler turn code into machine language",
    "what is the difference between sql and nosql databases",
    "how does public key cryptography work",
    "what is big o notation explained simply",
    "how does the python interpreter execute code",
    "what is a linked list and when should you use one",
    "difference between breadth first and depth first search",
    "how does https encrypt data between browser and server",
    "what is the difference between multiprocessing and multithreading python",
    "what graphics settings affect fps the most in pc games",
    "how does ray tracing affect game performance",
    "how does anti aliasing work in games",
    "what is the difference between 60fps and 120fps gaming",
    "what makes souls games so difficult by design",
    "how does matchmaking work in competitive games",
    "what is the difference between dpi and sensitivity in fps games",
    "what causes stuttering in open world games",
    "how does procedural generation work in minecraft",
    "what is the story of elden ring explained",
    "how does the unreal engine 5 nanite system work",
    "how does the event horizon of a black hole work",
    "what did the james webb telescope discover in 2025",
    "how does nuclear fusion produce more energy than fission",
    "what is the difference between a neutron star and black hole",
    "how long does light take to travel from sun to earth",
    "how does the international space station maintain orbit",
    "what is dark energy and how is it different from dark matter",
    "how does crispr gene editing actually work",
    "what causes earthquakes at tectonic plate boundaries",
    "what is the fermi paradox and why does it matter",
    "what is the cutoff for nit trichy computer science 2026",
    "how does josaa counselling work for iit nit admission",
    "what is the syllabus difference between jee mains and advanced",
    "best way to prepare for gate exam computer science",
    "what internships can first year cs engineering students apply for",
    "how to get a research internship at iit as an undergrad",
    "what is the placement record of bits pilani 2025",
    "best online courses for machine learning indian students",
    "how does the startup ecosystem in bangalore work",
    "how to apply for google summer of code india 2026",
    "what is the chronological watch order for attack on titan",
    "how does the power system in jujutsu kaisen work",
    "what happened at the end of fullmetal alchemist brotherhood",
    "is chainsaw man manga worth reading after the anime",
    "how does the one piece devil fruit system work",
    "what are the best psychological thriller anime of all time",
    "what is the tragedy of darth plagueis the wise full story",
    "how did palpatine survive after return of the jedi",
    "what is the difference between sith rule of two and rule of one",
    "how does the force dyad work between rey and kylo ren",
    "what happened to ahsoka after order 66",
    "how powerful is grand admiral thrawn compared to other villains",
    "how did anakin skywalker become more powerful than obi wan",
    "what is the history of mandalore in star wars canon",
    "why do humans need sleep and what happens if you dont",
    "how does the placebo effect actually work in medicine",
    "how does noise cancelling work in sony wh1000xm5",
    "why does spicy food feel hot even though it isnt",
    "how do free apps make money without charging users",
    "what is the psychology behind why games are addictive",
    "how does the algorithm on youtube decide what to recommend",
    "why does time feel faster as you get older psychology",
    "how does the immune system recognize a virus it has never seen",
]

# ---- auto detect username and paths ----
username = getpass.getuser()
USER_DATA_DIR = rf"C:\Users\{username}\AppData\Local\Microsoft\Edge\User Data"
BOT_DATA_DIR  = rf"C:\Users\{username}\AppData\Local\Microsoft\Edge\RewardsBot"

def get_edge_profiles(user_data_dir):
    profiles = []
    if not os.path.exists(user_data_dir):
        print(f"Edge User Data not found at: {user_data_dir}")
        exit()

    for folder in sorted(os.listdir(user_data_dir)):
        if folder == "Default" or folder.startswith("Profile "):
            prefs_path = os.path.join(user_data_dir, folder, "Preferences")
            if os.path.exists(prefs_path):
                try:
                    with open(prefs_path, 'r', encoding='utf-8') as f:
                        prefs = json.load(f)
                    name = prefs.get("profile", {}).get("name", folder)
                except Exception:
                    name = folder
                profiles.append({"name": name, "folder": folder})

    return profiles

# ---- detect and display profiles ----
profiles = get_edge_profiles(USER_DATA_DIR)

if not profiles:
    print("No Edge profiles found, exiting.")
    exit()

print("\nDetected Edge profiles:")
for i, p in enumerate(profiles, 1):
    print(f"  {i} — {p['name']} ({p['folder']})")

choice = input("\nEnter profile number: ").strip()
if not choice.isdigit() or not (1 <= int(choice) <= len(profiles)):
    print("Invalid choice, exiting.")
    exit()

selected = profiles[int(choice) - 1]
NUM_SEARCHES = int(input("How many searches? "))

# ---- launch selenium with separate bot dir ----
options = Options()
options.add_argument(f"--user-data-dir={BOT_DATA_DIR}")
options.add_argument(f"--profile-directory={selected['folder']}")
options.add_argument("--no-first-run")
options.add_argument("--no-default-browser-check")

service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service, options=options)

# ---- first time login check ----
marker_path = os.path.join(BOT_DATA_DIR, selected['folder'], "setup_done.txt")

if not os.path.exists(marker_path):
    print(f"\nFirst time setup for {selected['name']}!")
    print("1. Log into your Microsoft account in the browser window that just opened")
    print("2. Go to rewards.microsoft.com and confirm everything looks good")
    input("3. Press Enter here when done...\n")
    os.makedirs(os.path.dirname(marker_path), exist_ok=True)
    with open(marker_path, 'w') as f:
        f.write("done")
    print("Setup saved! Won't ask again for this profile.\n")

print(f"Running {NUM_SEARCHES} searches on: {selected['name']} ({selected['folder']})")
print("Press P to pause/resume, Q to quit.\n")

searches = random.sample(all_searches, min(NUM_SEARCHES, len(all_searches)))
paused = False
quitting = False

def toggle_pause():
    global paused
    paused = not paused
    print("\n⏸ PAUSED — press P to resume" if paused else "\n▶ RESUMED")

def quit_script():
    global quitting
    quitting = True
    print("\nQuitting...")

keyboard.add_hotkey('p', toggle_pause)
keyboard.add_hotkey('q', quit_script)

for i, query in enumerate(searches):
    if quitting:
        break

    while paused:
        time.sleep(0.5)
        if quitting:
            driver.quit()
            exit()

    print(f"[{i+1}/{NUM_SEARCHES}] Searching: {query}")

    driver.get("https://www.bing.com")
    time.sleep(3)

    try:
        search_box = driver.find_element(By.NAME, "q")
        search_box.click()
        for char in query:
            search_box.send_keys(char)
            time.sleep(random.uniform(0.05, 0.12))
        search_box.send_keys(Keys.RETURN)
    except Exception as e:
        print(f"Search box not found, skipping: {e}")
        continue

    time.sleep(random.uniform(10, 16))

    driver.execute_script("window.open('');")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)

print("\nAll done!")
driver.quit()
