# fortune.py (v1.1)
import random

name = "Avishi Saxena"
admission_no = "21JE0200"

print(f"🔮 Welcome to {name}'s Fortune Teller ({admission_no}) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

fortunes = {
    "happy": [
        f"Great things await you, {name.split()[0]}! Keep smiling.",
        "You are radiating positivity. Something great is near."
    ],
    "sad": [
        "Storms don’t last forever. You’re stronger than you think.",
        "Even rain helps the flowers grow. Better days ahead."
    ],
    "neutral": [
        "Still waters run deep. Embrace the calm.",
        "It’s okay to just exist. Balance is beautiful."
    ],
    "stressed": [
        f"Take a breath, {name.split()[0]}. The universe has your back.",
        "Tension is temporary. Keep moving forward."
    ]
}

if mood in fortunes:
    print(f"✨ Your fortune: {random.choice(fortunes[mood])} ✨")
else:
    print("✨ Unknown mood, but stay hopeful! ✨")
