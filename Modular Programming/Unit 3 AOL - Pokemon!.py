
# make interface and battle system first, then make different pokemon and type advantages; if time make animations
import random
import pygame


# why pokemon changing?
# to make more efficient?
# how to ensure health bar works?
# moving spots?

# damage of 'type' moves is dependent on speed (lower speed, more damage)

class Sprite:
    def __init__(self, health):
        self.health = health

    def bulkUp(self):
        d = int(random.randint(1,3))
        self.defense += d
        print("\nDefense increased by", d)

    def rest(self):
        r = random.randint(3,7)
        if self.health + r < 100:
            self.health += r
            print("\nHealth increased by", r)
        else:
            self.health = 100
            print("\nHealth is maxed")

    def tackle(self, type):
        damage = random.randint(20,25)
        type.health -= damage - type.defense
        net = damage - type.defense
        print("\nThe attack hit with", damage, "damage, but defended by", type.defense, "points, netting", net,
              "damage")


    def draw_health(self, type):
        background = pygame.image.load('background2.png')
        background = pygame.transform.scale(background, (900, 400))
        MAX_HEALTH = 100
        #p= pygame.Surface
        #e = pygame.Surface

        if isinstance(type, Bulbasaur):
            e = pygame.image.load('venusaur.png')
            e = pygame.transform.scale(e, (200, 200))
        if isinstance(type, Charmander):
            e = pygame.image.load('charizard.bmp.png')
            e = pygame.transform.scale(e, (200, 200))
        if isinstance(type, Squirtle):
            e = pygame.image.load('blastoise.png')
            e = pygame.transform.scale(e, (200, 200))

        if isinstance(self, Bulbasaur):
            p = pygame.image.load('venusaur.png')
            p = pygame.transform.scale(p, (300, 300))
        if isinstance(self, Charmander):
            p = pygame.image.load('charizard.bmp.png')
            p = pygame.transform.scale(p, (300, 300))
        if isinstance(self, Squirtle):
            p = pygame.image.load('blastoise.png')
            p = pygame.transform.scale(p, (300, 300))


        screen = pygame.display.set_mode((900, 400))
        pygame.display.set_caption("Pokemon!")

        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            if self.health > 66:
                color = (0, 255, 0)
            elif self.health > 33:
                color = (255,255,0)  # yellow???
            else:
                color = (255, 0, 0)

            if type.health > 66:
                color2 = (0, 255, 0)
            elif type.health > 33:
                color2 = (255,255,0)  # yellow???
            else:
                color2 = (255, 0, 0)

            black = (0,0,0)

            width = int(100 * self.health / MAX_HEALTH)
            health_bar = pygame.Rect(150, 60, width, 7)
            border = pygame.Rect(140, 56, 120, 17)

            width2 = int(100 * type.health / MAX_HEALTH)
            health_bar2 = pygame.Rect(700, 300, width2, 7)
            border2 = pygame.Rect(690, 296, 120, 17)


            if self.health <= MAX_HEALTH:
                pygame.draw.rect(background, black, border)
                pygame.draw.rect(background, color, health_bar)
                pygame.display.update()

            if type.health <= MAX_HEALTH:
                pygame.draw.rect(background, black, border2)
                pygame.draw.rect(background, color, health_bar2)
                pygame.display.update()


            screen.blit(background, (10, 10))
            screen.blit(p, (100, 100))
            screen.blit(e, (600, 60))
            #screen.blit(venusaur, (600, 60))

            #100,100; 600, 60

            pygame.display.flip()
            # Make the most recently drawn screen visible.
        pygame.quit()




class Charmander(Sprite):
    def __init__(self, health=100, defense=4, speed=20):
        super().__init__(health)
        self.defense = defense
        self.speed = speed

    def flamethrower(self, type):
        damage = ''
        if isinstance(type, Bulbasaur):
            print("\nIt's Super Effective!")
            damage = random.randint(30,40)
            type.health -= damage - type.defense
            net = damage - type.defense
        if isinstance(type, Charmander):
            print("\nIt's neutrally effective")
            damage = random.randint(25,30)
            type.health -= damage - type.defense
            net = damage - type.defense
        if isinstance(type, Squirtle):
            print("\nIt's not very effective...")
            damage = random.randint(10,20)
            type.health -= damage - type.defense
            net = damage - type.defense
        print("\nThe attack hit with", damage, "damage, but defended by", type.defense, "points, netting", net, "damage")


class Squirtle(Sprite):
    def __init__(self, health=100, defense=5, speed=30):
        super().__init__(health)
        self.speed = speed
        self.defense = defense

    def hydroPump(self, type):
        damage = ''
        if isinstance(type, Bulbasaur):
            print("\nIt's not very effective...")
            damage = random.randint(10,15)
            type.health -= damage - type.defense
            net = damage - type.defense
        if isinstance(type, Charmander):
            print("\nIt's Super Effective!")
            damage = random.randint(30,35)
            type.health -= damage - type.defense
            net = damage - type.defense
        if isinstance(type, Squirtle):
            print("\nIt's neutrally effective")
            damage = random.randint(20,25)
            type.health -= damage - type.defense
            net = damage - type.defense
        print("\nThe attack hit with", damage, "damage, but defended by", type.defense, "points, netting", net, "damage")


class Bulbasaur(Sprite):
    def __init__(self, health=100, defense=6, speed=10):
        super().__init__(health)
        self.speed = speed
        self.defense = defense

    def leafStorm(self, type):
        damage = ''
        if isinstance(type, Bulbasaur):
            print("\nIt's neutrally effective")
            damage = random.randint(25,30)
            type.health -= damage - type.defense
            net = damage - type.defense
        if isinstance(type, Charmander):
            print("\nIt's not very effective...")
            damage = random.randint(15,20)
            type.health -= damage - type.defense
            net = damage - type.defense
        if isinstance(type, Squirtle):
            print("\nIt's Super Effective!")
            damage = random.randint(35,40)
            type.health -= damage - type.defense
            net = damage - type.defense
        print("\nThe attack hit with", damage, "damage, but defended by", type.defense, "points, netting", net, "damage")


def pokemonMove(pokemon, enemy):

    while True:

        choice = ''
        if isinstance(pokemon, Charmander):
            choice = input("\nPlease select a move (bulk up, tackle, flamethrower, or rest) ").lower()
        if isinstance(pokemon, Squirtle):
            choice = input("\nPlease select a move (bulk up, tackle, hydro pump, or rest) ").lower()
        if isinstance(pokemon, Bulbasaur):
            choice = input("\nPlease select a move (bulk up, tackle, leaf storm, or rest) ").lower()

        if choice == 'bulk up':
            pokemon.bulkUp()
        elif choice == 'rest':
            pokemon.rest()
        elif choice == 'tackle':
            pokemon.tackle(enemy)
        elif choice == 'flamethrower':
            pokemon.flamethrower(enemy)
        elif choice == 'hydro pump':
            pokemon.hydroPump(enemy)
        elif choice == 'leaf storm':
            pokemon.leafStorm(enemy)
        else:
            print("That's not a move...")
            continue
        pokemon.draw_health(enemy)
        break


def enemyMove(pokemon, enemy):
    choice = ''
    C = ["bulk up", "rest", "flamethrower", "tackle"]
    S = ["bulk up", "rest", "hydro pump", "tackle"]
    B = ["bulk up", "rest", "leaf storm", "tackle"]
    if isinstance(enemy, Charmander):
        choice = random.choice(C)
    if isinstance(enemy, Squirtle):
        choice = random.choice(S)
    if isinstance(enemy, Bulbasaur):
        choice = random.choice(B)
    print("\nYoungster Joey used {0}!".format(choice))

    if choice == 'bulk up':
        enemy.bulkUp()
    if choice == 'rest':
        enemy.rest()
    if choice == 'tackle':
        enemy.tackle(pokemon)
    if choice == 'flamethrower':
        enemy.flamethrower(pokemon)
    if choice == 'hydro pump':
        enemy.hydroPump(pokemon)
    if choice == 'leaf storm':
        enemy.leafStorm(pokemon)
    pokemon.draw_health(pokemon)


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


def displayScores(pokemon, enemy):  #how to display normal names?
    print("\nUSER\nHealth:", pokemon.health, "\nDefense:", pokemon.defense)
    print("\nYOUNGSTER JOEY\nHealth:", enemy.health, "\nDefense:", enemy.defense)


def battle(pokemon, enemy):
    print("\nYoungster Joey challenges you! His pokemon is", enemy)
    pokemon = chooserPokemon(pokemon)
    enemy = chooserEnemy(enemy)
    while pokemon.health > 0 and enemy.health > 0:

        if pokemon.speed >= enemy.speed:
            pokemonMove(pokemon, enemy)
            if enemy.health <= 0:
                break
            displayScores(pokemon, enemy)
            enemyMove(pokemon, enemy)
            if pokemon.health <= 0:
                break
            displayScores(pokemon, enemy)

        else:
            enemyMove(pokemon, enemy)
            if pokemon.health <= 0:
                break
            displayScores(pokemon, enemy)

            pokemonMove(pokemon, enemy)
            if enemy.health <= 0:
                break
            displayScores(pokemon, enemy)

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

while True:
    pokemon = str(input("\nPlease choose your pokemon (Charmander, Bulbasaur, or Squirtle) ")).title()
    if pokemon == 'Charmander' or pokemon == 'Bulbasaur'or pokemon == 'Squirtle':
        battle(pokemon, enemy)
    else:
        print("\nThis is 1st Generation pokemon. C'mon Mr. Stubbs you should know this...")
