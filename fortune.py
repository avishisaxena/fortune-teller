# fortune.py (v1.0)

print("🔮 Welcome to Avishi Saxena's Fortune Teller (21JE0200) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

if mood == "happy":
    print("✨ Your fortune: Great things await you, Avishi! Keep smiling. ✨")
elif mood == "sad":
    print("✨ Your fortune: Storms don’t last forever. Better days are coming. ✨")
elif mood == "neutral":
    print("✨ Your fortune: Still waters run deep. Patience is key. ✨")
else:
    print("✨ Unknown mood, but stay hopeful! ✨")
