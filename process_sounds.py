import os
import shutil
import json

downloads_dir = r"C:\Users\ferha\Downloads"
repo_dir = r"C:\ProgramData\Py-Projeler\baby_sleep_sounds\baby-sleep-assets"
json_path = os.path.join(repo_dir, "sounds.json")

sound_mapping = {
    "changewire-moonlit_serenity_womb_healing_ambient_v2-339967.mp3": {
        "name": "Womb Healing", "category": "Uyku", "icon": "https://img.icons8.com/color/96/maternity.png", "new_file": "womb_healing.mp3"
    },
    "changewire-divine-feminine-healing-ethereal-ambient-soundscape-for-peace-339969.mp3": {
        "name": "Ethereal Ambient", "category": "Uyku", "icon": "https://img.icons8.com/color/96/night.png", "new_file": "ethereal_ambient.mp3"
    },
    "voicebosch-hair-dryer-225441.mp3": {
        "name": "Hair Dryer", "category": "Ev", "icon": "https://img.icons8.com/color/96/hair-dryer.png", "new_file": "hair_dryer.mp3"
    },
    "backgroundmusicforvideos-lullaby-baby-sleep-music-388567.mp3": {
        "name": "Lullaby 1", "category": "Uyku", "icon": "https://img.icons8.com/color/96/music-record.png", "new_file": "lullaby_1.mp3"
    },
    "bredorantes-shushing-150148.mp3": {
        "name": "Shushing", "category": "Uyku", "icon": "https://img.icons8.com/color/96/lips.png", "new_file": "shushing.mp3"
    },
    "tunetank-lullaby-baby-sleep-music-349977.mp3": {
        "name": "Lullaby 2", "category": "Uyku", "icon": "https://img.icons8.com/color/96/music-record.png", "new_file": "lullaby_2.mp3"
    },
    "dragon-studio-winter-wind-402331.mp3": {
        "name": "Winter Wind", "category": "Doğa", "icon": "https://img.icons8.com/color/96/wind.png", "new_file": "winter_wind.mp3"
    },
    "dragon-studio-gentle-rain-07-437321.mp3": {
        "name": "Gentle Rain", "category": "Doğa", "icon": "https://img.icons8.com/color/96/rain.png", "new_file": "gentle_rain.mp3"
    },
    "freemusicforvideo-lullaby-baby-sleep-music-456277.mp3": {
        "name": "Lullaby 3", "category": "Uyku", "icon": "https://img.icons8.com/color/96/music-record.png", "new_file": "lullaby_3.mp3"
    },
    "freesound_community-sea-wave-34088.mp3": {
        "name": "Sea Waves", "category": "Doğa", "icon": "https://img.icons8.com/color/96/sea.png", "new_file": "sea_waves.mp3"
    },
    "freesound_community-kitchen-fan-71401.mp3": {
        "name": "Kitchen Fan", "category": "Ev", "icon": "https://img.icons8.com/color/96/fan.png", "new_file": "kitchen_fan.mp3"
    },
    "freesound_community-c5_mother-singing-80947.mp3": {
        "name": "Mother Singing", "category": "Uyku", "icon": "https://img.icons8.com/color/96/mother.png", "new_file": "mother_singing.mp3"
    },
    "mariacorgo-embalar-13513.mp3": {
        "name": "Embalar Lullaby", "category": "Uyku", "icon": "https://img.icons8.com/color/96/music-record.png", "new_file": "embalar_lullaby.mp3"
    },
    "lilliben-cosmic-serenity-celestial-soundscapes-365183.mp3": {
        "name": "Cosmic Serenity", "category": "Uyku", "icon": "https://img.icons8.com/color/96/galaxy.png", "new_file": "cosmic_serenity.mp3"
    },
    "schorsch1964-night-atmosphere-with-crickets-374652.mp3": {
        "name": "Night Crickets", "category": "Doğa", "icon": "https://img.icons8.com/color/96/cricket-insect.png", "new_file": "night_crickets.mp3"
    },
    "soundreality-fire-sound-334130.mp3": {
        "name": "Fireplace", "category": "Doğa", "icon": "https://img.icons8.com/color/96/fire-element.png", "new_file": "fireplace.mp3"
    }
}

# 1. Read existing json to find highest ID
with open(json_path, 'r', encoding='utf-8') as f:
    sounds = json.load(f)

max_id = 0
for s in sounds:
    try:
        current_id = int(s['id'])
        if current_id > max_id:
            max_id = current_id
    except ValueError:
        pass

# 2. Process and Copy
base_url = "https://raw.githubusercontent.com/ferhaterol94/baby-sleep-assets/main/"

for old_name, details in sound_mapping.items():
    source = os.path.join(downloads_dir, old_name)
    if os.path.exists(source):
        print(f"Copying {old_name}...")
        dest = os.path.join(repo_dir, details['new_file'])
        shutil.copy2(source, dest)
        
        max_id += 1
        new_entry = {
            "id": str(max_id),
            "name": details['name'],
            "category": details['category'],
            "icon": details['icon'],
            "url": f"{base_url}{details['new_file']}"
        }
        sounds.append(new_entry)
    else:
        print(f"Warning: {old_name} not found in Downloads!")

# 3. Write back json
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(sounds, f, indent=4, ensure_ascii=False)

print("Finished processing.")
