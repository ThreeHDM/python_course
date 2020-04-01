# Breaking out of while loops
import random

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

