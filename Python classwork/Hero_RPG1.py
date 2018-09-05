#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. goblin
class Charachter:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    
    def attack(self, enemy):
        enemy.health = enemy.health - self.power
        print ("The {} does {} dammage to the {}. The {} has {} health left.").format(self.name, self.power, enemy.name, enemy.name, enemy.health)

    def print_status(self):
        print ("The {} has {} health and {} power.".format(self.name, self.health, self.power))

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

class Hero(Charachter):
    def fillspace(self):
        print("This is top fill space")

class Goblin(Charachter):
    def fillspace(self):
        print("This is top fill space")

class Zombie(Charachter):
    def alive(self):
        return True
    

def main():
    hero = Hero("hero", 10, 5)
    goblin = Goblin("goblin", 6, 2)
    zombie = Zombie("zombie", 0, 1)
    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        zombie.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("4. fight zombie (at your own risk)")
        print("> ")
        raw_input = int(input())
        if raw_input == 1:
            hero.attack(goblin)
            if goblin.alive() == False:
                print("The goblin is dead.")
        elif raw_input == 2:
            pass
        elif raw_input == 3:
            print("Goodbye.")
            break
        if raw_input == 4:
            hero.attack(zombie)

        else:
            print("Invalid input {}".format(raw_input))

        if goblin.alive() and raw_input != 4:
            # Goblin attacks hero
            goblin.attack(hero)
            if hero.alive() == False:
                print("You are dead.")
        elif zombie.alive() and raw_input == 4:
            # Zombie attacks hero
            zombie.attack(hero)
            if hero.alive() == False:
                print("You are dead.")

main()
