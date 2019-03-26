
# make interface and battle system first, then make different pokemon and type advantages; if time make animations
import random


# WHY DOES HEALTH INCREASE????
# WHY DOES PROGRAM RANDOMLY STOP????? - main error
# how to make more efficient? - go into definition for everything but type moves.
# rest, loose a turn?
# quick attack always goes first
# change damage depending on speed


Bmoves = {"bulk up": range(1,3), "quick attack": range(10,20), "leaf storm": [range(30,40), range(20,30), range(10,20)], "rest": range(5,10)}
Smoves = {"bulk up": range(1,3), "quick attack": range(10,20), "hydro pump": [range(30,40), range(20,30), range(10,20)], "rest": range(5,10)}
Cmoves = {"bulk up": range(1,3), "quick attack": range(10,20), "flamethrower": [range(30,40), range(20,30), range(10,20)], "rest": range(5,10)}


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
                r = int(random.choice(Cmoves[choice]))
                self.health += r
                print("\nHealth increased by", r)
                break
            if choice == 'bulk up':
                d = int(random.choice(Cmoves[choice]))
                self.defense += d
                print("\nDefense increased by", d)
                break
            if choice == 'quick attack':  # how to ensure that they go first?
                damage = int(random.choice(Cmoves[choice])) - type.defense
                type.health -= damage
                print("\nThe attack hit with", damage, "damage")

                break
            if choice == 'flamethrower':  # keeps health at 100, doesn't go into any conditions syntax below doesn't work either
                if isinstance(type, Bulbasaur):
                    print("\nIt's Super Effective!")
                    damage = int(random.choice(Cmoves["flamethrower"][0])) - type.defense
                    type.health -= damage
                if isinstance(type, Charmander):
                    print("\nIt's neutrally effective")
                    damage = int(random.choice(Cmoves["flamethrower"][1])) - type.defense
                    type.health -= damage
                if isinstance(type, Squirtle):
                    print("\nIt's not very effective...")
                    damage = int(random.choice(Cmoves["flamethrower"][2])) - type.defense
                    type.health -= damage
                print("\nThe attack hit with", damage, "damage")
                break


class Squirtle(Sprite):
    def __init__(self, health=100, defense=5, speed=30):
        super().__init__(health)
        self.speed = speed
        self.defense = defense

    def attack(self, type, choice):
        while True:
            damage = ''
            if choice == 'rest':
                r = int(random.choice(Smoves[choice]))
                self.health += r
                print("\nHealth increased by", r)
                break
            if choice == 'bulk up':
                d = int(random.choice(Smoves[choice]))
                self.defense += d
                print("\nDefense increased by", d)
                break
            if choice == 'quick attack':  # how to ensure that they go first?
                damage = int(random.choice(Smoves[choice]))
                type.health -= damage - type.defense
                print("\nThe attack hit with", damage, "damage")
                break

            if choice == 'hydro pump':
                if isinstance(type, Bulbasaur):
                    print("\nIt's not very effective...")
                    damage = int(random.choice(Smoves["hydro pump"][2])) - type.defense
                    type.health -= damage
                if isinstance(type, Charmander):
                    print("\nIt's Super Effective!")
                    damage = int(random.choice(Smoves["hydro pump"][0])) - type.defense
                    type.health -= damage
                if isinstance(type, Squirtle):
                    print("\nIt's neutrally effective")
                    damage = int(random.choice(Smoves["hydro pump"][1])) - type.defense
                    type.health -= damage
                print("\nThe attack hit with", damage, "damage")
                break


class Bulbasaur(Sprite):
    def __init__(self, health=100, defense=6, speed=10):
        super().__init__(health)
        self.speed = speed
        self.defense = defense

    def attack(self, type, choice):
        while True:
            damage = ''
            if choice == 'rest':
                r = int(random.choice(Bmoves[choice]))
                self.health += r
                print("\nHealth increased by", r)
                break
            if choice == 'bulk up':
                d = int(random.choice(Bmoves[choice]))
                self.defense += d
                print("\nDefense increased by", d)
                break
            if choice == 'quick attack':  # how to ensure that they go first?
                damage = int(random.choice(Bmoves[choice])) - type.defense
                type.health -= damage
                print("\nThe attack hit with", damage, "damage")
                break
            if choice == 'leaf storm':
                if isinstance(type, Bulbasaur):
                    print("\nIt's neutrally effective")
                    damage = int(random.choice(Bmoves["leaf storm"][1])) - type.defense
                    type.health -= damage
                if isinstance(type, Charmander):
                    print("\nIt's not very effective...")
                    damage = int(random.choice(Bmoves["leaf storm"][2])) - type.defense
                    type.health -= damage
                if isinstance(type, Squirtle):
                    print("\nIt's Super Effective!")
                    damage = int(random.choice(Bmoves["leaf storm"][0])) - type.defense
                    type.health -= damage
                print("\nThe attack hit with", damage, "damage")
                break





def pokemonMove(pokemon, enemy):
    # gives me error for code below: UnboundLocalError: local variable 'choice' referenced before assignment
    while True:
        choice = ''
        if isinstance(pokemon, Charmander):
            choice = input("\nPlease select a move (bulk up, quick attack, flamethrower, or rest) ").lower()
        if isinstance(pokemon, Squirtle):
            choice = input("\nPlease select a move (bulk up, quick attack, hydro pump, or rest) ").lower()
        if isinstance(pokemon, Bulbasaur):
            choice = input("\nPlease select a move (bulk up, quick attack, leaf storm, or rest) ").lower()
        if choice == 'bulk up' or choice == 'quick attack' or choice == 'hydro pump' or choice == 'rest' or choice == \
                'leaf storm' or choice == 'flamethrower':
            pokemon.attack(enemy, choice)
            break
        else:
            print("\nYou didn't choose a valid move")


def enemyMove(pokemon, enemy):
    choice = ''
    if isinstance(enemy, Charmander):
        choice = random.choice(list(Cmoves))
    if isinstance(enemy, Squirtle):
        choice = random.choice(list(Smoves))
    if isinstance(enemy, Bulbasaur):
        choice = random.choice(list(Bmoves))
    print("\nYoungster Joey used", choice, "!")
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
    print("\nYoungster Joey challenges you! His pokemon is", enemy)
    pokemon = chooserPokemon(pokemon)
    enemy = chooserEnemy(enemy)
    while pokemon.health > 0 and enemy.health > 0:
        if pokemon.speed >= enemy.speed:
            pokemonMove(pokemon, enemy)
            if enemy.health <= 0:
                break
            print("\nUser:\nHealth:", pokemon.health, "\nDefense:", pokemon.defense)
            print("\nYoungster Joey:\nHealth:", enemy.health, "\nDefense:", enemy.defense)

            while True:
                i = input("\nType 'ok' to continue ").lower()
                if i == 'ok':
                    enemyMove(pokemon, enemy)
                    break

            if pokemon.health <= 0:
                break
            print("\nUser:\nHealth:", pokemon.health, "\nDefense:", pokemon.defense)
            print("\nYoungster Joey\nHealth:", enemy.health, "\nDefense:", enemy.defense)

        else:
            enemyMove(pokemon, enemy)
            if pokemon.health <= 0:
                break
            print("\nUser\nHealth:", pokemon.health, "\nDefense:", pokemon.defense)
            print("\nYoungster Joey\nHealth:", enemy.health, "\nDefense:", enemy.defense)

            pokemonMove(pokemon, enemy)
            if enemy.health <= 0:
                break
            print("\nUser\nHealth:", pokemon.health, "\nDefense:", pokemon.defense)
            print("\nYoungster Joey\nHealth:", enemy.health, "\nDefense:", enemy.defense)

    # outcome
    if pokemon.health > 0:
        print("\nCongrats, you defeated Youngster Joey! You earned 100 gold and 20 exp points.")

    if enemy.health > 0:
        print("\nBooooooo. You lost :(")

    again = input("\nPlay again? (y for yes) ").lower()
    if again != 'y':
        print("\nThank you for playing pokemon!!!")
        exit()

# code begins here


starters = ["Charmander", "Squirtle", "Bulbasaur"]
enemy = random.choice(starters)
x=0
while x == 0:
    pokemon = str(input("\nPlease choose your pokemon (Charmander, Bulbasaur, or Squirtle) ")).title()
    if pokemon == 'Charmander':
        battle(pokemon, enemy)
    elif pokemon == 'Bulbasaur':
        battle(pokemon, enemy)
    elif pokemon == 'Squirtle':
        battle(pokemon, enemy)

    else:
        print("\nNot a valid option")
