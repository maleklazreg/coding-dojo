class user:
    def __init__(self, first_name, last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(f"name: {self.first_name} {self.last_name}")
        print(f"email: {self.email}")
        print(f"age : {self.age}")
        print(f"reward member : {self.is_rewards_member}")
        print(f"gold card points : {self.gold_card_points}")
    
    def enroll(self):
        if self.is_rewards_member:
            print(f"{self.first_name}user is alrady an the members")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print(f"{self.first_name} has been enrolled in the rewards program")
            return True
    
    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
            print(f"{self.first_name} spent {amount} poitns")
        else:
            print(f"{self.first_name} does not have enough points")


user1 = user("John","Doe", "johndoe@efel.com",20)
user2 = user("Zayn", "Jorden", "zayn@efel.com", 40)
user3 = user("Liam", "Paine", "liam@nefel.com", 31)

user1.display_info()

user1.enroll()
user2.enroll()

user1.spend_points(50)
user2.spend_points(80)

user1.display_info()
user2.display_info()
user3.display_info()

user1.enroll()

user3.spend_points(40)


