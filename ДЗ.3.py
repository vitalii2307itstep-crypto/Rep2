import random
class Pet:
    def __init__(self, name, hunger=50, happiness=50):
        self.name = name
        self.hunger = hunger
        self.happiness = happiness
    def eat(self):
        self.hunger += 20
        self.happiness += 5
        if self.hunger > 1000:
            self.hunger = 1000
        print(self.name, "eats")
    def play(self):
        self.happiness += 20
        self.hunger -= 15
        if self.happiness > 1000:
            self.happiness = 1000
        print(self.name, "is playing")
    def status(self):
        print("Pet:", self.name)
        print("Hunger:", self.hunger)
        print("Happiness:", self.happiness)
    def live(self):
        self.hunger -= c
        self.happiness -= x
class Student:
    def __init__(self, name, pet):
        self.name = name
        self.pet = pet
    def feed_pet(self):
        print(self.name, "feeds", self.pet.name)
        self.pet.eat()
    def play_with_pet(self):
        print(self.name, "plays with", self.pet.name)
        self.pet.play()
pet = Pet("Rex")
student = Student("Ren", pet)
for month in range(1, 13):
    student.feed_pet()
    student.play_with_pet()
    c = random.randint(1, 10)
    x = random.randint(1, 10)
    pet.live()
    print()
    pet.status()