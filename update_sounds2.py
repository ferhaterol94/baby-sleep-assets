import os
import shutil
import json

downloads_dir = r"C:\Users\ferha\Downloads"
repo_dir = r"C:\ProgramData\Py-Projeler\baby_sleep_sounds\baby-sleep-assets"
json_path = os.path.join(repo_dir, "sounds.json")

# New files to add
files_to_add = [
    ("sergequadrado-happy-birthday-to-you-disco-128624.mp3", "happy_birthday.mp3", "Happy Birthday", "Music", "https://img.icons8.com/color/96/birthday-cake.png"),
    ("sergequadrado-hush-little-baby-113104.mp3", "hush_little_baby.mp3", "Hush Little Baby", "Sleep", "https://img.icons8.com/color/96/sleeping-baby.png"),
    ("sergequadrado-twinkle-twinkle-little-star-113108.mp3", "twinkle_star.mp3", "Twinkle Star", "Sleep", "https://img.icons8.com/color/96/star.png")
]

with open(json_path, 'r', encoding='utf-8') as f:
    sounds = json.load(f)

# Translate existing names to English
translation_map = {
    "Beyaz Gürültü (Test)": "White Noise",
    "Yağmur Sesi (Test)": "Rain Sound (Test)",
    "Horoz ve Karga": "Crow & Rooster",
    "Horoz": "Rooster",
    "Karda Ayak Sesleri": "Footsteps in Snow",
    "Sakin Yağmur": "Calming Rain",
    "Su Sesi": "Water Sound",
    "Mağarada Su Damlası": "Cave Water Drip",
    "Su Baloncukları": "Water Bubbles",
    "Sabah Kuşları 1": "Morning Birds 1",
    "Sabah Kuşları 2": "Morning Birds 2",
    "Sabah Kuşları 3": "Morning Birds 3",
    "Sabah Kuşları 4": "Morning Birds 4",
    "Orman Ambiyansı": "Forest Ambience",
    "Doğa ve Su": "Nature Water",
    "Dinlendirici Su": "Sleep Water"
}

for sound in sounds:
    name = sound.get("name", "")
    if name in translation_map:
        sound["name"] = translation_map[name]

# Add new files
max_id = max([int(s['id']) for s in sounds]) if sounds else 0

for orig_name, new_name, display_name, category, icon in files_to_add:
    src = os.path.join(downloads_dir, orig_name)
    dst = os.path.join(repo_dir, new_name)
    
    if os.path.exists(src):
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

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(sounds, f, indent=4, ensure_ascii=False)
