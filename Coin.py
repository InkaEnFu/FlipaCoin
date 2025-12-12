from User import User
import random
import time
class Coin:
    def __init__(self,user):
        self.user = user

    def flip_a_coin(self):
        while True:
            wait_for_enter = input("Click any key for start")
            time.sleep(1)
            dropped = random.randint(1,100)
            if dropped <= 10 * self.user.chance:
                print("You won!")
                user1.add_money(0.01)
            else:
                print("You lost")

if __name__ == "__main__":
    user1 = User(0,1)
    coin1 = Coin(user1)
    coin1.flip_a_coin()