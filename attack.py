# Breaking out of while loops
import random


# CLASS CREATION
class Enemy:
    hp = 200

    def __init__(self, atkl, atkh): # This code runs then the class is instantiated
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):  # The self variable is the entire object
        print("Attack is", self.atkl)  # We use self to access the property

    def getHp(self):
        print("Hp is", self.hp)


enemy1 = Enemy(40, 49)
enemy1.getAtk()
enemy1.getHp()

enemy2 = Enemy(75, 90)
enemy2.getAtk()
enemy2.getHp()
''' 
playerhp = 260 # player hitpoints
enemyatkl = 60 # enemy attack low
enemyatkh = 80 # enemy attack high

while playerhp > 0:
    # damage that the player takes
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30

    print("Enemy strikes for", dmg, "points of damage. Current HP is", playerhp)

    if playerhp > 30:
        # pass  # lets you leave an empty block of code
        continue  # ignores everything after in the loop

    print("You have low health. You've been teleported to the nearest inn")
    break
'''
