import random

print("🎲 Комп'ютерний кубик готовий! Натискай Enter, щоб кинути.")

while True:
    input()
    number = random.randint(1, 6)
    print(f"Тобі випало: {number} 🎲")