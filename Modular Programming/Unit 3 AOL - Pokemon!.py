
# make interface and battle system first, then make different pokemon and type advantages; if time make animations
import random

# how to make more efficient? - go into definition for everything but type moves.
# rest, loose a turn?
# quick attack always goes first
# add speed?

Bmoves = {"bulk up": range(15,30), "quick attack": range(10,20), "leaf storm": [range(30,40), range(20,30), range(10,20)], "rest": range(10,25)}
Smoves = {"bulk up": range(15,30), "quick attack": range(10,20), "hydro pump": [range(30,40), range(20,30), range(10,20)], "rest": range(10,25)}
Cmoves = {"bulk up": range(15,30), "quick attack": range(10,20), "flamethrower": [range(30,40), range(20,30), range(10,20)], "rest": range(10,25)}


class Sprite:
    def __init__(self, health):
        self.health = health

    def attack(self, type):
        raise NotImplementedError
    # pass?


class Charmander(Sprite):
    def __init__(self, health=100, defense=4, speed=20):
        super().__init__(health)
        self.defense = defense
        self.speed = speed

    def attack(self, type):
        while True:
            choice = input("\nPlease select a move (bulk up, quick attack, flamethrower, or rest) ").lower()

            if choice == 'heal':
                self.health += int(random.choice(Cmoves[choice]))
                print("\nYour health is now", self.health)
                break
            if choice == 'bulk up':
                self.defense += int(random.choice(1, 4))
                print("\nYour defense is now", self.defense)
                break
            if choice == 'quick attack':  # how to ensure that they go first?
                damage = int(random.choice(Cmoves[choice]))
                type.health -= damage
                break
            if choice == 'flamethrower':
                if type == 'Bulbasaur':
                    damage = int(random.choice(Cmoves["flamethrower"][0])) - type.defense
                    type.health -= damage
                if type == 'Charmander':
                    damage = int(random.choice(Cmoves["flamethrower"][1])) - type.defense
                    type.health -= damage
                if type == 'Squirtle':
                    damage = int(random.choice(Cmoves["flamethrower"][2])) - type.defense
                    type.health -= damage
                print("\nYour attack hit with", damage, "damage")


class Squirtle(Sprite):
    def __init__(self, health=100, defense=5, speed=30):
        super().__init__(health)
        self.speed = speed
        self.defense = defense

    def attack(self, type):
        while True:
            choice = input("\nPlease select a move (bulk up, quick attack, flamethrower, or rest) ").lower()

            if choice == 'heal':
                self.health += int(random.choice(Cmoves[choice]))
                print("\nYour health is now", self.health)
                break
            if choice == 'bulk up':
                self.defense += int(random.choice(1, 4))
                print("\nYour defense is now", self.defense)
                break
            if choice == 'quick attack':  # how to ensure that they go first?
                damage = int(random.choice(Cmoves[choice]))
                type.health -= damage
                break

            if choice == 'hydro pump':
                if type == 'Bulbasaur':
                    damage = int(random.choice(Cmoves["flamethrower"][2])) - type.defense
                    type.health -= damage
                if type == 'Charmander':
                    damage = int(random.choice(Cmoves["flamethrower"][0])) - type.defense
                    type.health -= damage
                if type == 'Squirtle':
                    damage = int(random.choice(Cmoves["flamethrower"][1])) - type.defense
                    type.health -= damage
                print("\nYour attack hit with", damage, "damage")


class Bulbasaur(Sprite):
    def __init__(self, health=100, defense=6, speed=10):
        super().__init__(health)
        self.speed = speed
        self.defense = defense

    def attack(self, type):
        while True:
            choice = input("\nPlease select a move (bulk up, quick attack, flamethrower, or rest) ").lower()

            if choice == 'heal':
                self.health += int(random.choice(Cmoves[choice]))
                print("\nYour health is now", self.health)
                break
            if choice == 'bulk up':
                self.defense += int(random.choice(1, 4))
                print("\nYour defense is now", self.defense)
                break
            if choice == 'quick attack':  # how to ensure that they go first?
                damage = int(random.choice(Cmoves[choice]))
                type.health -= damage
                break
            if choice == 'leaf storm':
                if type == 'Bulbasaur':
                    damage = int(random.choice(Cmoves["flamethrower"][1])) - type.defense
                    type.health -= damage
                if type == 'Charmander':
                    damage = int(random.choice(Cmoves["flamethrower"][2])) - type.defense
                    type.health -= damage
                if type == 'Squirtle':
                    damage = int(random.choice(Cmoves["flamethrower"][0])) - type.defense
                    type.health -= damage
                print("\nYour attack hit with", damage, "damage")


def battle(pokemon, enemy):
    pokemon = eval(pokemon)  # makes iterable for classes
    print("\nYounger Joey challenges you! His pokemon is", enemy)
    enemy = eval(enemy)  # need here because of line above
    while pokemon.health > 0 and enemy.health > 0:

        if pokemon.speed > enemy.speed:  # and pokemon.attack == False:
            pokemon.attack(enemy)
            if enemy.health <= 0:
                break
            print("\nThe health of Youngster Joey is now", enemy.health)

        if enemy.speed > pokemon.speed:  # and enemy.speed == False:
            enemy.attack(pokemon)
            if pokemon.health <= 0:
                break
            print("\nYour health is now", pokemon.health)

    # outcome
    if pokemon.health > 0:
        print("\nCongrats, you defeated Youngster Joey! You earned 100 gold and 20 exp points.")
    if enemy.health > 0:
        print("\nBooooooo. You lost :(")


starters = ["Charmander", "Squirtle", "Bulbasaur"]
enemy = random.choice(starters)

while True:
    pokemon = str(input("\nPlease choose your pokemon (Charmander, Bulbasaur, or Squirtle) ")).title()
    if pokemon == 'Charmander':
        # enemy has the type advantage
        battle(pokemon, enemy)
    elif pokemon == 'Bulbasaur':
        battle(pokemon, enemy)
    elif pokemon == 'Squirtle':
        battle(pokemon, enemy)

    else:
        print("\nNot a valid option")
