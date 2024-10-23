class User:
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
        return self


    
    def enroll(self):
        if  self.is_rewards_member == True:
            # self.is_rewards_member == True
            self.gold_card_points == 200
            print(f"{self.first_name} has been enrolled as a rewards member.")
        else:
            print(f"{self.first_name} is already a rewards member.")
        return self


    
    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
            print(f"{self.first_name} spent {amount} poitns")
        else:
            print(f"{self.first_name} does not have enough points")
        return self


user1 = User("John","Doe", "johndoe@efel.com",20)
user2 = User("Zayn", "Jorden", "zayn@efel.com", 40)
user3 = User("Liam", "Paine", "liam@nefel.com", 31)


# user1.display_info().enroll().spend_points(50).dispaly_info()     ===== commenter there is issue hear
user1.display_info().enroll().spend_points(50).display_info()




user2.display_info().enroll().spend_points(50).display_info()