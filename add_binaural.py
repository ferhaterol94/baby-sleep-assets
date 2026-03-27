import os
import shutil
import json

downloads_dir = r"C:\Users\ferha\Downloads"
repo_dir = r"C:\ProgramData\Py-Projeler\baby_sleep_sounds\baby-sleep-assets"
json_path = os.path.join(repo_dir, "sounds.json")

files_to_add = [
    ("kaazoom-soar-full-version-binaural-beats-409369.mp3", "binaural_soar.mp3", "Binaural Soar", "Sleep", "https://img.icons8.com/color/96/brain.png"),
    ("kaazoom-drifting-away-full-version-binaural-beats-409329.mp3", "binaural_drifting.mp3", "Binaural Drifting", "Sleep", "https://img.icons8.com/color/96/brain.png"),
    ("michael-x_studio-michael-x_studio-thetha-deep-space-336hz-original-mix-486472.mp3", "theta_deep_space.mp3", "Theta Deep Space", "Sleep", "https://img.icons8.com/color/96/galaxy.png"),
    ("michael-x_studio-thetha-waves-542-hz-311040.mp3", "theta_542hz.mp3", "Theta 542 Hz", "Sleep", "https://img.icons8.com/color/96/sound-wave.png"),
    ("michael-x_studio-thetha-waves-448-hz-286578.mp3", "theta_448hz.mp3", "Theta 448 Hz", "Sleep", "https://img.icons8.com/color/96/sound-wave.png"),
    ("purebinaural-purebinaural-20-hz-beta-isochronic-tones-pure-tone-496540.mp3", "beta_20hz.mp3", "Beta 20 Hz", "Music", "https://img.icons8.com/color/96/brain.png"),
    ("purebinaural-purebinaural-12-hz-alpha-binaural-beat-with-ocean-waves-484847.mp3", "alpha_12hz_ocean.mp3", "Alpha 12 Hz Ocean", "Nature", "https://img.icons8.com/color/96/sea-waves.png"),
    ("beetpro-asmr-power-brain-connect-spiritual-frequency-11946.mp3", "spiritual_frequency.mp3", "Spiritual Frequency", "Sleep", "https://img.icons8.com/color/96/meditation-guru.png"),
    ("natureseye-simply-meditation-series-11hz-alpha-binaural-waves-for-relaxed-focus-8028.mp3", "meditation_11hz.mp3", "Meditation 11 Hz", "Sleep", "https://img.icons8.com/color/96/meditation-guru.png")
]

with open(json_path, 'r', encoding='utf-8') as f:
    sounds = json.load(f)

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
