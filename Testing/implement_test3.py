import test3_oop

player1 = test3_oop.Player("Hazel",30)
enemy1 = test3_oop.Enemy("Sans",40)
player2 = test3_oop.Player("Armin",60)

player1.attack(enemy1)
player2.attack(enemy1)

enemy1.attack(player1)
enemy1.attack(player1)
enemy1.attack(player1)

player1.stats()
player2.stats()
enemy1.stats()
