import random

print("🎲 Комп'ютерний кубик готовий! Натискай Enter, щоб кинути.")

while True:
    input()
    number = random.randint(1, 6)
    print(f"Тобі випало: {number} 🎲")


    class hero:

        def __init__(self, name, health):
            self.name = name
            self.health = health
    hero1 = hero("Odin", 80)
    hero2 = hero("Jezzear", 100)

    print(hero1.name, hero1.health)
    print(hero2.name, hero2.health)


    class Cat:

        def __init__(self, name, color, age):
            self.name = name
            self.color = color
            self.age = age

    cat1 = Cat("Odin", "black", 3)
    cat2 = Cat("Jezzear", "white", 5)

    print(cat1.name, cat1.color, cat1.age)
    print(cat2.name, cat2.color, cat2.age)

