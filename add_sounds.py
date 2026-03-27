import os
import shutil
import json

downloads_dir = r"C:\Users\ferha\Downloads"
repo_dir = r"C:\ProgramData\Py-Projeler\baby_sleep_sounds\baby-sleep-assets"
json_path = os.path.join(repo_dir, "sounds.json")

files_to_add = [
    ("mehmetfaal1991-turkish-crow-and-rooster-sound-effect-136858.mp3", "crow_rooster.mp3", "Horoz ve Karga", "Animal", "https://img.icons8.com/color/96/rooster.png"),
    ("freesound_community-cock-rooster-cockerel-scream-sound-100787.mp3", "rooster.mp3", "Horoz", "Animal", "https://img.icons8.com/color/96/rooster.png"),
    ("dragon-studio-footsteps-in-the-snow-499652.mp3", "snow_footsteps.mp3", "Karda Ayak Sesleri", "Nature", "https://img.icons8.com/color/96/snow.png"),
    ("liecio-calming-rain-257596.mp3", "calming_rain_2.mp3", "Sakin Yağmur", "Nature", "https://img.icons8.com/color/96/rain.png"),
    ("40727898-touching-the-water-176713.mp3", "water_touch.mp3", "Su Sesi", "Nature", "https://img.icons8.com/color/96/water.png"),
    ("solarmusic-dripping-water-in-cave-114694.mp3", "cave_water_drip.mp3", "Mağarada Su Damlası", "Nature", "https://img.icons8.com/color/96/cave.png"),
    ("liecio-water-bubbles-257594.mp3", "water_bubbles.mp3", "Su Baloncukları", "Nature", "https://img.icons8.com/color/96/bubbles.png"),
    ("freesound_community-morning-birdsong-60158.mp3", "morning_birds_1.mp3", "Sabah Kuşları 1", "Nature", "https://img.icons8.com/color/96/bird.png"),
    ("fahimexpo32-bird-morning-sound-178978.mp3", "morning_birds_2.mp3", "Sabah Kuşları 2", "Nature", "https://img.icons8.com/color/96/bird.png"),
    ("freesound_community-birds-in-the-morning-24147.mp3", "morning_birds_3.mp3", "Sabah Kuşları 3", "Nature", "https://img.icons8.com/color/96/bird.png"),
    ("freesound_community-morning-birds-30911.mp3", "morning_birds_4.mp3", "Sabah Kuşları 4", "Nature", "https://img.icons8.com/color/96/bird.png"),
    ("audiopapkin-forest-ambience-296528.mp3", "forest_ambience.mp3", "Orman Ambiyansı", "Nature", "https://img.icons8.com/color/96/forest.png"),
    ("slrathna-sleep-water-nature-317559.mp3", "sleep_water_nature.mp3", "Doğa ve Su", "Nature", "https://img.icons8.com/color/96/water.png"),
    ("slrathna-sleep-water-316041.mp3", "sleep_water.mp3", "Dinlendirici Su", "Nature", "https://img.icons8.com/color/96/water.png")
]

with open(json_path, 'r', encoding='utf-8') as f:
    sounds = json.load(f)

# find max id
max_id = max([int(s['id']) for s in sounds])

for orig_name, new_name, display_name, category, icon in files_to_add:
    src = os.path.join(downloads_dir, orig_name)
    dst = os.path.join(repo_dir, new_name)
    
    if os.path.exists(src):
        shutil.copy2(src, dst)
        max_id += 1
        new_entry = {
            "id": str(max_id),
            "name": display_name,
            "category": category,
            "icon": icon,
            "url": f"https://raw.githubusercontent.com/ferhaterol94/baby-sleep-assets/main/{new_name}"
        }
        sounds.append(new_entry)
        print(f"Added {new_name}")
    else:
        print(f"Missing: {orig_name}")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(sounds, f, indent=4, ensure_ascii=False)
