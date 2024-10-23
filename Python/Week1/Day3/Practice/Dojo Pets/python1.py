# pet.py
class Pet:
    def __init__(self, name, pet_type, tricks):
        self.name = name
        self.type = pet_type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep(self):
        self.energy += 25
        print(f"{self.name} as sliping and his energy is {self.energy}")

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} his heals {self.health} and his energy {self.energy} after eating")

    def play(self):
        self.health += 15
        print(f"{self.name} his health at playing is {self.health}")

    def noise(self):
        print(f"{self.name} Woof!" if self.type == "HabHab!" else f"{self.name} Meow!")