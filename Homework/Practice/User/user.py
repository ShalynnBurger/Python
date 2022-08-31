# print("sanity check")


class User:
    def __init__(self, first_name, last_name, email, age, is_rewards_member = False, gold_card_points = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_meber = is_rewards_member
        self.gold_card_points = gold_card_points

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_meber)
        print(self.gold_card_points)
        return self

    def enroll(self):
        self.is_rewards_meber = True
        self.gold_card_points += 200
        return self

    def spend_points(self, amount):
        self.gold_card_points -= amount
        return self

shay = User("Shay", "Burger", "snburger@gmail.com", 27, False, 0)

shay.enroll().display_info()

print("----")

maverick = User("Maverick", "James", "mavjames@gmail.com", 4, False, 0)

kyva = User("Kyva", "Ray", "kray@gmail.com", 3, True, 200)

maverick.spend_points(50).display_info()

print("----")

kyva.enroll().spend_points(80).display_info()


