import random

class Item:
    def __init__(self, name, price, count, description):
        self.name = self
        self.price = price
        self. count = count
        self.description = description
    def __str__(self):
        return (str(self.name) + ": " + str(self.price) + "-Gold, " + str(self.count) + "-left")

class SuperTonic(Item):
    def __init__(self):
        self.name = "Super Tonic"
        self.count = 5
        self.price = 20*((self.count-6) * (-1))
        self.description = "Brings your charachter back to max health."
    def use(self, user):
        user.health = user.max

class ArmorPlate(Item):
    def __init__(self):
        self.name = "Armor"
        self.count = 5
        self.price = 20*((self.count-6) * (-1))
        self.description = "Adds two armor to your character. (each point of armor negates one damage per attack)"
    def use(self, user):
        user.armor = user.armor + 2

class RegularTonic(Item):
    def __init__(self):
        self.name = "Regular Tonic"
        self.count = "endless"
        self.price = 2
        self.description = "Adds two to your health."
    def use(self, user):
        user.health = user.health +2

class ProtienShake(Item):
    def __init__(self):
        self.name = "Protien shake"
        self.count = 15
        self.price = 20 + ((self.count-15)*5) 
        self.description = "Adds 5 to your max health."
    def use(self, user):
        user.max = user.max + 5

class Axe(Item):
    def __init__(self):
        self.name = "Axe"
        self.count = 1
        self.price = 10
        self.description = "AND MY AXE... for +1 power."
    def use(self, user):
        user.power = user.power + 1
    
class Winchester(Item):
    def __init__(self):
        self.name = "Winchester"
        self.count = 4
        self.price = 25
        self.description = "Good ol' WInchester rifle, for those long shots... and +2 power."
    def use(self, user):
        user.power = user.power + 2

class MagicMissilelauncher(Item):
    def __init__(self):
        self.name = "Magic Missile Launcher"
        self.count = 1
        self.price = 40
        self.description = "All the magic missiles you could ever want! Dont let it get dispelled! (+3 to power)"
    def use(self, user):
        user.power = user.power + 3

class LightSaber(Item):
    def __init__(self):
        self.name = "Light Saber"
        self.count = 1
        self.price = 55
        self.description = "Junior sized for all meticlorian levels... +4 power"
    def use(self, user):
        user.power = user.power + 4

class Hire_DeadPool(Item):
    def __init__(self):
        self.name = "Wade Wilson"
        self.count = 1
        self.price = 100
        self.description = "Otherwise known as Deadpool.. He will fight with you.. for a price. (+10 power)"
    def use(self, user):
        user.power = user.power + 10


class Charachter:
    def __init__(self, name, health, power, level):
        self.name = name
        self.health = health
        self.max = health
        self.power = power
        self.evade = evade
        self.armor = armor
        self.level = 1

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

class Hero(Charachter):
    def __init__(self):
        self.name = "hero"
        self.max = 10
        self.health = 10
        self.power = 5
        self.evade = 1
        self.armor = 0
        self.level = 1
    def attack(self, enemy):
        crit = random.randint(1, 10)
        miss = random.randint(1, 100)
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
                print("The rock golem's hard skin makes your sword bounce back doing half your power as damage top you!")

class Medic(Charachter):
    def __init__(self):
        self.name = "Witch Doctor"
        self.health = 10
        self.max = 10
        self.power = 1
        self.evade = 2
        self.armor = 0
        self.level = 1
    def attack(self, enemy):
        miss = random.randint(1, 100)
        recover = random.randint(1, 10)
        if recover < 3 and self.health < 9:
            self.health = self.health + 2
            print ("THe witch doctor cures his Wounds! (+2 hp)")
        if 1 < miss < (enemy.evade * 5):
            print("You missed!")
        else:
            damage = (self.power - enemy.armor)
            enemy.health = enemy.health - damage
            print ("The Medic does {} damage to the {}. The {} has {} health left.").format(damage, enemy.name, enemy.name, enemy.health)

class Shadow(Charachter):  
    def __init__(self):
        self.name = "shadow"
        self.health = 1
        self.max = 1
        self.power = 1
        self.evade = 18
        self.armor = 0
        self.level = 1

class Goblin(Charachter):
    def __init__(self):
        self.name = 'Goblin'
        self.health = 6
        self.max = 6
        self.power = 2
        self.evade = 3
        self.armor = 0
        self.level = 1

class Zombie(Charachter):
    def __init__(self):
        self.name = 'zombie'
        self.health = 10
        self.max = 10
        self.power = 1
        self.evade = 2
        self.armor = -1
        self.level = 1
    def alive():
        return True

class Slime(Charachter):
    def __init__(self):
        self.name = 'Slime'
        self.health = 10
        self.max = 10
        self.power = 1
        self.evade = 2
        self.armor = -1
        self.level = 1
    def alive(self):
        split = random.randint(1,2)
        if (self.health > 0 and split == 1):
            return True
        elif (self.health < 0 and split == 2):
            self.health = 1
            print("The slime didnt die, but split into two!")
            return True
        else:
            return False
    
class FireEmp(Charachter):
    def __init__(self):
        self.name = "Fire Emp"
        self.health = 6
        self.max = 6
        self.power = 3
        self.evade = 5
        self.armor = 0
        self.level = 1
    def attack(self, enemy):
        miss = random.randint(1, 100)
        if 1 < miss < (enemy.evade * 5):
            print("You missed!")
        else:
            preburn = self.power - enemy.armor
            damage = self.power + 1 - enemy.armor   
            enemy.health = enemy.health - damage
            print ("The Fire Emp does {} dammage to the {}. And the {} takes one burn damage. The {} has {} health left.".format(preburn, enemy.name, ememy.name, enemy.name, enemy.health))
    
class RockGolem(Charachter):
    def __init__(self):
        self.name = "Rock Golem"
        self.health = 10
        self.max = 10 
        self.power = 2
        self.evade = 1
        self.armor = 4
        self.level = 1

class DarkWizzard(Charachter):
    def __init__(self):
        self.name = "Dark Wizzard"
        self.health = 250
        self.max = 250
        self.power = 15
        self.evade = 8
        self.armor = 10
        self.level = 1

###################################
###################################
###################################

def fight_sequence(flenemy, hero):
    while flenemy.alive() and hero.alive():
        print()
        hero.print_status()
        flenemy.print_status()
        print()
        print("What do you want to do?")
        print("1. fight {}").format(flenemy.name)
        print("2. do nothing")
        print("3. flee")
        print("> ")
        raw_input = int(input())
        print()
        if raw_input == 1:
            hero.attack(flenemy)
            if flenemy.alive() == False:
                print("The {} is dead.").format(flenemy.name)
        elif raw_input == 2:
            pass
        elif raw_input == 3:
            print("Goodbye.")
            break

        else:
            print("Invalid input {}".format(raw_input))

        if flenemy.alive():
            # Enemy attacks hero
            flenemy.attack(hero)
            if hero.alive() == False:
                print("You are dead.")

def generate_items():
    

def store(a, b, c, d, e, f, g, h, i):
    print()
    print("Welcome to the shop:")
    print("Select a number for an item in the shop to see what it does or to purchase it. Of course\nthis is a buisness so the items arent free.\nIf you dont have enough cash, go kill a monster or two. I'll have a portal open between each floor.")
    print()
    print ("1. " + str(a) + "\n2. " + str(b) + "\n3. " + str(c) + "\n4. " + str(d) + "\n5. " + str(e) + "\n6. " + str(f) + "\n7. " + str(g) + "\n8. " + str(h) + "\n9. " + str(i) + "\n10. ")

def main():
    print("Welcome to python Dungeon Crawler! Reach the Dark Wizzard in the deepest floor of the Maze!")
    print("Each floor will have a new, stronger combatant, and a small fairy store will have aportal open to")
    print("sell you items you might need between each floor. Can you make it all of the way to the bottom?")
    floor_count = 1
    thishero = Hero()
    #items
    super_tonic = SuperTonic()
    armor_plate = ArmorPlate()
    regular_tonic = RegularTonic()
    protien_shake = ProtienShake()
    axe = Axe()
    winchester = Winchester()
    magic_missile_launcher = MagicMissilelauncher()
    lightsaber = LightSaber()
    hire_deadpool = Hire_DeadPool()
    #


#loop
    flenemy = Medic()
    fight_sequence(flenemy, thishero)
    store(super_tonic, armor_plate, regular_tonic, protien_shake, axe, winchester, magic_missile_launcher, lightsaber, hire_deadpool)


main()
