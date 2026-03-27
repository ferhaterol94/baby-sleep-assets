import os
import json

repo_dir = r"C:\ProgramData\Py-Projeler\baby_sleep_sounds\baby-sleep-assets"
json_path = os.path.join(repo_dir, "sounds.json")

target_files = [
    "binaural_soar.mp3",
    "binaural_drifting.mp3",
    "theta_deep_space.mp3",
    "theta_542hz.mp3",
    "theta_448hz.mp3",
    "beta_20hz.mp3",
    "alpha_12hz_ocean.mp3",
    "spiritual_frequency.mp3",
    "meditation_11hz.mp3"
]

with open(json_path, 'r', encoding='utf-8') as f:
    sounds = json.load(f)

count = 0
for sound in sounds:
    filename = sound.get('url', '').split('/')[-1]
    if filename in target_files:
        sound['category'] = "Frequency"
        count += 1

print(f"Updated {count} sounds to Frequency category.")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(sounds, f, indent=4, ensure_ascii=False)
