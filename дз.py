class Toy:
    def __init__(self, name):
        self.name = name


class Cat:
    def __init__(self, name):
        self.name = name

    def play(self, toy):
        print(f"Кіт {self.name} грається з іграшкою: {toy.name}")


my_toy = Toy("Мишка")
my_cat = Cat("Мур")

my_cat.play(my_toy)
