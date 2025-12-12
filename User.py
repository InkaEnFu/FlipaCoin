class User:
    def __init__(self,money,chance):
        self.money = money
        self.chance = chance

    def add_money(self,x):
        self.money += x
        