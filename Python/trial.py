import random
class Charachter:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.max = health
        self.power = power
        self.evade = evade
        self.armor = armor

    def __str__(self):
        print self.name + ": " + self.health + "hp, " + self.power + "pw, " + self.evade + "ev, " + self.armor + "ar"

    def print_status(self):
        print ("The {} has {} health and {} power.".format(self.name, self.health, self.power))
 
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    
    def attack(self, enemy):
        miss = random.randint(1, 100)
        if 1 < miss < (enemy.evade * 5):
            print("You missed!")
        else:
            damage = (self.power - enemy.armor)
            enemy.health = enemy.health - damage
            print ("The {} does {} dammage to the {}. The {} has {} health left.").format(self.name, damage, enemy.name, enemy.name, enemy.health)

class Item:
    def __init__(self, name, price, count, description):
        self.name = self
        self.price = price
        self. count = count
        self.description = description

class SuperTonic(Item):
    def __ini__(self):
        self.name = "Super Tonic"
        self.count = 5
        self.price = 20*((self.count-6) * (-1))
        self.description = "Brings your charachter back to max health."
    def use(self, user):
        user.health = user.max

class ArmorPlate(Item):
    def __ini__(self):
        self.name = "Armor"
        self.count = 5
        self.price = 20*((self.count-6) * (-1))
        self.description = "Adds two armor to your character. (each point of armor negates one damage per attack)"
    def use(self, user):
        user.armor = user.armor + 2

class RegularTonic(Item):
    def __ini__(self):
        self.name = "Regular Tonic"
        self.count = "endless"
        self.price = 2
        self.description = "Adds two to your health."
    def use(self, user):
        user.health = user.health +2

class ProtienShake(Item):
    def __ini__(self):
        self.name = "Protien shake"
        self. count = 15
        self.sprice = 20 + ((count-15)*5) 
        self.description = "Adds 5 to your max health."
    def use(self, user):
        user.max = user.max + 5

class Axe(Item):
    def __ini__(self):
        self.name = "Axe"
        self.count = 1
        self.price = 10
        self.description = "AND MY AXE... for +1 power."
    def use(self, user):
        user.power = user.power + 1
    
class Winchester(Item):
    def __ini__(self):
        self.name = "Winchester"
        self.count = 4
        self.price = 25
        self.description = "Good ol' WInchester rifle, for those long shots... and +2 power."
    def use(self, user):
        user.power = user.power + 2

class MagicMissilelauncher(Item):
    def __ini__(self):
        self.name = "Magic Missile Launcher"
        self.count = 1
        self.price = 40
        self.description = "All the magic missiles you could ever want! Dont let it get dispelled! (+3 to power)"
    def use(self, user):
        user.power = user.power + 3

class LightSaber(Item):
    def __ini__(self):
        self.name = "Light Saber"
        self.count = 1
        self.price = 55
        self.description = "Junior sized for all meticlorian levels... +4 power"
    def use(self, user):
        user.power = user.power + 4

class Hire_DeadPool(Item):
    def __ini__(self):
        self.name = "Wade Wilson"
        self.count = 1
        self.price = 100
        self.description = "Otherwise known as Deadpool.. He will fight with you.. for a price. (+10 power)"
    def use(self, user):
        user.power = user.power + 10


class Hero(Charachter):
    def __ini__(self):
        self.name = hero
        self.max = 10
        self.health = 10
        self.power = 5
        self.evade = 1
        self.armor = 0
    def attack(self, enemy):
        crit = random.randomint(1, 10)
        miss = random.randomint(1, 100)
        reflect = random.randint(1,4)
        if 1 < miss < (enemy.evade * 5):
            print("You missed!")
        else:
            if crit < 3:
                damage = (self.power*2 -enemy.armor)
                print ("Critical Strike!")
            else:
                damage = (self.power- enemy.armor)
            enemy.health = enemy.health - damage
            print ("The hero does {} dammage to the {}. The {} has {} health left.").format(damage, enemy.name, enemy.name, enemy.health)
            if isinstance(enemy, FireEmp):
                self.health = self.health - 1
                print ("The hero is hurt by the flames. He takes one damage.")
            if isinstance(enemy, RockGolem) and reflect == 1:
                self.health = self.health - (self.power/2)
                print("The rock golem's hard skin makes your sword bounce back!")
class Medic(Charachter):
    def __ini__(self):
        self.name = dark_medic
        self.health = 10
        self.max = 10
        self.power = 1
        self.evade = 2
        self.armor = 0
    def attack(self, enemy):
        miss = random.randint(1, 100)
        recover = random.randomint(1, 10)
        if recover < 3 and self.health < 9:
            self.health = self.health + 2
            print ("Cure Wounds!")
        if 1 < miss < (enemy.evade * 5):
            print("You missed!")
        else:
            damage = (self.power - enemy.armor)
            enemy.health = enemy.health - damage
            print ("The Medic does {} damage to the {}. The {} has {} health left.").format(damage, enemy.name, enemy.name, enemy.health)

class Shadow (Charachter):  
    def __ini__(self):
        self.name = hero
        self.health = 1
        self.max = 1
        self.power = 1
        self.evade = 18
        self.armor = 0

class Goblin(Charachter):
    def __ini__(self):
        self.name = hero
        self.health = 6
        self.max = 6
        self.power = 2
        self.evade = 3
        self.armor = 0

class Zombie(Charachter):
    def __ini__(self):
        self.name = hero
        self.health = 10
        self.max = 10
        self.power = 1
        self.evade = 2
        self.armor = -1
    def alive():
        return True

class FireEmp(Charachter):
    def __ini__(self):
        self.name = hero
        self.health = 6
        self.max = 6
        self.power = 3
        self.evade = 5
        self.armor = 0
    def attack(self, enemy):
        miss = random.randint(1, 100)
        if 1 < miss < (enemy.evade * 5):
            print("You missed!")
        else:
            preburn = self.power - enemy.armor
            damage = self.power + 1 - enemy.armor   
            enemy.health = enemy.health - damage
            print ("The Fire Emp does {} dammage to the {}. And the {} takes one burn damage. The {} has {} health left.").format(preburn, enemy.name, ememy.name, enemy.name, enemy.health)
    
class RockGolem(Charachter):
    def __ini__(self):
        self.name = "Rock Golem"
        self.health = 10
        self.max = 10
        self.power = 2
        self.evade = 1
        self.armor = 4
    
def main():
    print("Welcome to python Dungeon Crawler! Reach the Dark Wizzard in the deepest floor of the Maze!")
    print("Each floor will have a new, stronger combatant, and a small fairy store will have aportal open to")
    print("sell you items you might need between each floor. Can you make it all of the way to the bottom?")
    floor_count = 1
    hero = Hero()
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
