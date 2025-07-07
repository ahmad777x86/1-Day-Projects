
class Player:
    def __init__(self,name,damage):
        self.health = 100
        self.name = name
        self.damage = damage
        self.state = "alive"        

    def attack(self,other):
        other.health -= self.damage
        if(other.health < 0):
            other.health = 0
            other.state = "dead"

    def stats(self):
        print(f"Name:{self.name} \nHealth:{self.health} \nState:{self.state}\n")

class Enemy:
    def __init__(self,name,damage):
        self.health = 100
        self.name = name
        self.damage = damage
        self.state = "alive"

    def attack(self,other):
        other.health -= self.damage
        if(other.health < 0):
            other.health = 0
            other.state = "dead"

    def stats(self):
        print(f"Name:{self.name} \nHealth:{self.health} \nState:{self.state}\n")
