
# make interface and battle system first, then make different pokemon and type advantages; if time make animations
import random


# WHY DOES HEALTH INCREASE????
# WHY DOES PROGRAM RANDOMLY STOP????? - main error
# how to make more efficient? - go into definition for everything but type moves.
# rest, loose a turn?
# quick attack always goes first

Bmoves = {"bulk up": range(15,30), "quick attack": range(10,20), "leaf storm": [range(30,40), range(20,30), range(10,20)], "rest": range(10,25)}
Smoves = {"bulk up": range(15,30), "quick attack": range(10,20), "hydro pump": [range(30,40), range(20,30), range(10,20)], "rest": range(10,25)}
Cmoves = {"bulk up": range(15,30), "quick attack": range(10,20), "flamethrower": [range(30,40), range(20,30), range(10,20)], "rest": range(10,25)}

class Sprite:
    def __init__(self, health):
        self.health = health

    def attack(self, type, choice):
        raise NotImplementedError
    # pass?


class Charmander(Sprite):
    def __init__(self, health=100, defense=4, speed=20):
        super().__init__(health)
        self.defense = defense
        self.speed = speed

    def attack(self, type, choice):
        while True:
            if choice == 'rest':
                self.health += int(random.choice(Cmoves[choice]))
                print("\nYour health is now", self.health)
                break
            if choice == 'bulk up':
                self.defense += int(random.choice(0,4))
                print("\nYour defense is now", self.defense)
                break
            if choice == 'quick attack':  # how to ensure that they go first?
                damage = int(random.choice(Cmoves[choice])) - type.defense
                type.health -= damage
                print("hi")
                break
            if choice == 'flamethrower':  # keeps health at 100, doesn't go into any conditions
                print(type)
                if type == Bulbasaur():
                    damage = int(random.choice(Cmoves["flamethrower"][0])) - type.defense
                    type.health -= damage
                if type == Charmander():
                    damage = int(random.choice(Cmoves["flamethrower"][1])) - type.defense
                    type.health -= damage
                if type == Squirtle():
                    damage = int(random.choice(Cmoves["flamethrower"][2])) - type.defense
                    type.health -= damage
            #print("\nThe attack hit with", damage, "damage")
                break


class Squirtle(Sprite):
    def __init__(self, health=100, defense=5, speed=30):
        super().__init__(health)
        self.speed = speed
        self.defense = defense

    def attack(self, type, choice):
        while True:
            if choice == 'rest':
                self.health += int(random.choice(Cmoves[choice]))
                print("\nYour health is now", self.health)
                break
            if choice == 'bulk up':
                self.defense += int(random.choice(0,4))
                print("\nYour defense is now", self.defense)
                break
            if choice == 'quick attack':  # how to ensure that they go first?
                damage = int(random.choice(Cmoves[choice]))
                type.health -= damage - type.defense
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
                #print("\nThe attack hit with", damage, "damage")
                break

class Bulbasaur(Sprite):
    def __init__(self, health=100, defense=6, speed=10):
        super().__init__(health)
        self.speed = speed
        self.defense = defense

    def attack(self, type, choice):
        while True:
            if choice == 'rest':
                self.health += int(random.choice(Cmoves[choice]))
                print("\nYour health is now", self.health)
                break
            if choice == 'bulk up':
                self.defense += int(random.choice(0,4))  #  TypeError: choice() takes 2 positional arguments but 3 were given

                print("\nYour defense is now", self.defense)
                break
            if choice == 'quick attack':  # how to ensure that they go first?
                damage = int(random.choice(Cmoves[choice])) - type.defense
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
                break

                # print("\nThe attack hit with", damage, "damage") # unbound local variable error


def pokemonMove(pokemon, enemy):
    # gives me error for code below: UnboundLocalError: local variable 'choice' referenced before assignment
    '''
    if pokemon == "Charmander":
        choice = input("\nPlease select a move (bulk up, quick attack, flamethrower, or rest) ").lower()
    if pokemon == 'Squirtle':
        choice = input("\nPlease select a move (bulk up, quick attack, hydro pump, or rest) ").lower()
    if pokemon == "Bulbasaur":
        choice = input("\nPlease select a move (bulk up, quick attack, leaf storm, or rest) ").lower()
    '''

    choice = input("\nPlease select a move (bulk up, quick attack, flamethrower, or rest) ").lower()
    pokemon.attack(enemy, choice)


def enemyMove(pokemon, enemy):
    choice = random.choice(list(Cmoves))
    enemy.attack(pokemon, choice)


def chooserPokemon(pokemon):
    if pokemon == "Charmander":
        return Charmander()
    if pokemon == "Squirtle":
        return Squirtle()
    if pokemon == "Bulbasaur":
        return Bulbasaur()

def chooserEnemy(enemy):
    if enemy == "Charmander":
        return Charmander()
    if enemy == "Squirtle":
        return Squirtle()
    if enemy == "Bulbasaur":
        return Bulbasaur()


def battle(pokemon, enemy):
    print("\nYounger Joey challenges you! His pokemon is", enemy)
    pokemon = chooserPokemon(pokemon)
    enemy = chooserEnemy(enemy)
    while pokemon.health > 0 and enemy.health > 0:
        if pokemon.speed >= enemy.speed:
            pokemonMove(pokemon, enemy)
            if enemy.health <= 0:
                break
            print("\nThe health of Youngster Joey is now", enemy.health)

            enemyMove(pokemon, enemy)
            if pokemon.health <= 0:
                break
            print("\nYour health is now", pokemon.health)

        else:
            enemyMove(pokemon, enemy)
            if pokemon.health <= 0:
                break
            print("\nYour health is now", pokemon.health)

            pokemonMove(pokemon, enemy)
            if enemy.health <= 0:
                break
            print("\nThe health of Youngster Joey is now", enemy.health)

    # outcome
    if pokemon.health > 0:
        print("\nCongrats, you defeated Youngster Joey! You earned 100 gold and 20 exp points.")
    if enemy.health > 0:
        print("\nBooooooo. You lost :(")


# code begins here
starters = ["Charmander", "Squirtle", "Bulbasaur"]
enemy = random.choice(starters)
while True:
    pokemon = str(input("\nPlease choose your pokemon (Charmander, Bulbasaur, or Squirtle) ")).title()
    if pokemon == 'Charmander':
        battle(pokemon, enemy)
    elif pokemon == 'Bulbasaur':
        battle(pokemon, enemy)
    elif pokemon == 'Squirtle':
        battle(pokemon, enemy)

    else:
        print("\nNot a valid option")
