from python1 import Pet
# ninja.py
class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        print(f"{self.first_name} is walking {self.pet.name}.")
        self.pet.play()

    def feed(self):
        print(f"{self.first_name} is feeding {self.pet.name}.")
        self.pet.eat()

    def bathe(self):
        print(f"{self.first_name} is bathing {self.pet.name}.")
        self.pet.noise()


my_pet = Pet("OPS", "kalb", ["roll over", "fetch"])
my_ninja = Ninja("Itachi", "Utchihha", "treats", "dog food", my_pet)

my_ninja.feed()
my_ninja.walk()
my_ninja.bathe()


    