import os
import shutil
import json
import glob

downloads_dir = r"C:\Users\ferha\Downloads"
repo_dir = r"C:\ProgramData\Py-Projeler\baby_sleep_sounds\baby-sleep-assets"
json_path = os.path.join(repo_dir, "sounds.json")

# Search by partial names
mappings = [
    ("*heartbeat*.mp3", "heartbeat.mp3", "Heartbeat", "Sleep", "https://img.icons8.com/color/96/heart-with-pulse.png"),
    ("*cat*purring*.mp3", "cat_purring.mp3", "Cat Purring", "Animal", "https://img.icons8.com/color/96/cat.png"),
    ("*washing*machine*.mp3", "washing_machine.mp3", "Washing Machine", "Home", "https://img.icons8.com/color/96/washing-machine.png"),
    ("*vacuum*cleaner*.mp3", "vacuum_cleaner.mp3", "Vacuum Cleaner", "Home", "https://img.icons8.com/color/96/vacuum-cleaner.png")
]

with open(json_path, 'r', encoding='utf-8') as f:
    sounds = json.load(f)

max_id = max([int(s['id']) for s in sounds]) if sounds else 0

for pattern, new_name, display_name, category, icon in mappings:
    matches = glob.glob(os.path.join(downloads_dir, pattern))
    if matches:
        src = matches[0]
        dst = os.path.join(repo_dir, new_name)
        shutil.copy2(src, dst)
        max_id += 1
        sounds.append({
            "id": str(max_id),
            "name": display_name,
            "category": category,
            "icon": icon,
            "url": f"https://raw.githubusercontent.com/ferhaterol94/baby-sleep-assets/main/{new_name}"
        })
        print(f"Added {new_name}")
    else:
        print(f"Match not found for {pattern}")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(sounds, f, indent=4, ensure_ascii=False)
