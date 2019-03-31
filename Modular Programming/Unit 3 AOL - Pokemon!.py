
# make interface and battle system first, then make different pokemon and type advantages; if time make animations
import random
import pygame

# intelligent computer guessing

# damage of 'type' moves is dependent on speed (lower speed, more damage)

class Sprite:
    def __init__(self, health, isEnemy):
        self.health = health
        self.isEnemy = isEnemy

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
        screen = pygame.display.set_mode((900, 400))
        pygame.display.set_caption("Pokemon!")
        pygame.font.init()
        h = pygame.font.SysFont('Comic Sans MS', 30)

        maxhp = 100

        if type.isEnemy:
            playerHealth = h.render("Health: " + str(type.health), False, (0, 0, 0))  # how to display health?
            enemyHealth = h.render("Health: " + str(self.health), False, (0, 0, 0))

            width = int(100 * self.health / maxhp)
            health_bar = pygame.Rect(150, 60, width, 7)
            border = pygame.Rect(140, 56, 120, 17)

            width2 = int(100 * type.health / maxhp)
            health_bar2 = pygame.Rect(700, 300, width2, 7)
            border2 = pygame.Rect(690, 296, 120, 17)

        else:
            playerHealth = h.render("Health: " + str(self.health), False, (0, 0, 0))
            enemyHealth = h.render("Health: " + str(type.health), False, (0, 0, 0))

            width = int(100 * type.health / maxhp)
            health_bar = pygame.Rect(150, 60, width, 7)
            border = pygame.Rect(140, 56, 120, 17)

            width2 = int(100 * self.health / maxhp)
            health_bar2 = pygame.Rect(700, 300, width2, 7)
            border2 = pygame.Rect(690, 296, 120, 17)

        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
            black = (0,0,0)
            green = (50,205,50)  # didn't want to get super reptitive with changing colours
            if self.health <= maxhp:
                pygame.draw.rect(background, black, border)
                pygame.draw.rect(background, green, health_bar)
                pygame.display.update()

            if type.health <= maxhp:
                pygame.draw.rect(background, black, border2)
                pygame.draw.rect(background, green, health_bar2)
                pygame.display.update()

            screen.blit(background, (0, 0))

            if type.isEnemy:
                screen.blit(self.picture, (100, 100))
                screen.blit(type.picture, (600, 60))

            else:
                screen.blit(type.picture, (100, 100)) # position
                screen.blit(self.picture, (600, 60))

            screen.blit(playerHealth, (600, 350))
            screen.blit(enemyHealth, (50, 20))

            pygame.display.flip()
                # Make the most recently drawn screen visible.
        pygame.quit()


class Charizard(Sprite):
    def __init__(self, health=100, defense=5, speed=20, isEnemy=True):
        super().__init__(health, isEnemy)
        self.defense = defense
        self.speed = speed
        self.picture = pygame.image.load('charizard.bmp.png')
        self.description = "\nCharizard is the second and the second bulkiest pokemon" \
                           "\nFlamethrower does the second most damage of all the type-moves"

        if self.isEnemy:
            self.picture = pygame.transform.scale(self.picture, (200, 200))
        else:
            self.picture = pygame.transform.scale(self.picture, (300, 300))

    def flamethrower(self, type):
        damage = ''
        if isinstance(type, Venusaur):
            print("\nIt's Super Effective!")
            damage = random.randint(30,40)
            type.health -= damage - type.defense
            net = damage - type.defense
        if isinstance(type, Charizard):
            print("\nIt's neutrally effective")
            damage = random.randint(25,30)
            type.health -= damage - type.defense
            net = damage - type.defense
        if isinstance(type, Blastoise):
            print("\nIt's not very effective...")
            damage = random.randint(10,20)
            type.health -= damage - type.defense
            net = damage - type.defense
        print("\nThe attack hit with", damage, "damage, but defended by", type.defense, "points, netting", net, "damage")


class Blastoise(Sprite):
    def __init__(self, health=100, defense=4, speed=30, isEnemy=True):
        super().__init__(health, isEnemy)
        self.speed = speed
        self.defense = defense
        self.picture = pygame.image.load('blastoise.png')
        self.description = "\nBlastoise is the fastest pokemon, but the least bulky." \
                           "\nHydro Pump does the least damage of all the type-moves"

        if self.isEnemy:
            self.picture = pygame.transform.scale(self.picture, (200, 200))
        else:
            self.picture = pygame.transform.scale(self.picture, (300, 300))


    def hydroPump(self, type):
        damage = ''
        if isinstance(type, Venusaur):
            print("\nIt's not very effective...")
            damage = random.randint(10,15)
            type.health -= damage - type.defense
            net = damage - type.defense
        if isinstance(type, Charizard):
            print("\nIt's Super Effective!")
            damage = random.randint(30,35)
            type.health -= damage - type.defense
            net = damage - type.defense
        if isinstance(type, Blastoise):
            print("\nIt's neutrally effective")
            damage = random.randint(20,25)
            type.health -= damage - type.defense
            net = damage - type.defense
        print("\nThe attack hit with", damage, "damage, but defended by", type.defense, "points, netting", net, "damage")


class Venusaur(Sprite):
    def __init__(self, health=100, defense=6, speed=10, isEnemy=True):
        super().__init__(health, isEnemy)
        self.speed = speed
        self.defense = defense
        self.picture = pygame.image.load('venusaur.png')
        self.description = "\nVenusaur is the slowest pokemon, but the most bulky." \
                           "\nLeaf Storm does the most damage of all the type-moves"

        if self.isEnemy:
            self.picture = pygame.transform.scale(self.picture, (200, 200))
        else:
            self.picture = pygame.transform.scale(self.picture, (300, 300))


    def leafStorm(self, type):
        damage = ''
        if isinstance(type, Venusaur):
            print("\nIt's neutrally effective")
            damage = random.randint(25,30)
            type.health -= damage - type.defense
            net = damage - type.defense
        if isinstance(type, Charizard):
            print("\nIt's not very effective...")
            damage = random.randint(15,20)
            type.health -= damage - type.defense
            net = damage - type.defense
        if isinstance(type, Blastoise):
            print("\nIt's Super Effective!")
            damage = random.randint(35,40)
            type.health -= damage - type.defense
            net = damage - type.defense
        print("\nThe attack hit with", damage, "damage, but defended by", type.defense, "points, netting", net, "damage")


def pokemonMove(pokemon, enemy):

    while True:

        choice = ''
        if isinstance(pokemon, Charizard):
            choice = input("\nPlease select a move (bulk up, tackle, flamethrower, or rest) ").lower()
        if isinstance(pokemon, Blastoise):
            choice = input("\nPlease select a move (bulk up, tackle, hydro pump, or rest) ").lower()
        if isinstance(pokemon, Venusaur):
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
        if enemy.health > 0:
            pokemon.draw_health(enemy)
        break


def enemyMove(pokemon, enemy):
    choice = ''
    if isinstance(enemy, Charizard):
        if enemy.health < 30:
            C = ["bulk up", "rest", "rest", "rest", "rest", "flamethrower", "tackle"]
        elif isinstance(pokemon, Venusaur):
            C = ["bulk up", "rest", "flamethrower","flamethrower","flamethrower", "tackle"]
        else:
            C = ["bulk up", "rest", "flamethrower", "tackle"]
        choice = random.choice(C)
    if isinstance(enemy, Blastoise):
        if enemy.health < 30:
            S = ["bulk up", "rest", "rest", "rest", "rest", "flamethrower", "tackle"]
        elif isinstance(pokemon, Charizard):
            S = ["bulk up", "rest", "hydro pump","hydro pump","hydro pump", "tackle"]
        else:
            S = ["bulk up", "rest", "hydro pump", "tackle"]
        choice = random.choice(S)
    if isinstance(enemy, Venusaur):
        if enemy.health < 30:
            B = ["bulk up", "rest", "rest", "rest", "rest", "leaf storm", "tackle"]
        elif isinstance(pokemon, Blastoise):
            B = ["bulk up", "rest", "leaf storm","leaf storm","leaf storm", "tackle"]
        else:
            B = ["bulk up", "rest", "leaf storm", "tackle"]

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
    if pokemon.health > 0:
        enemy.draw_health(pokemon)


def chooserPokemon(pokemon):
    if pokemon == "Charizard":
        return Charizard(100, 4, 20, False)
    if pokemon == "Blastoise":
        return Blastoise(100, 5, 30, False)
    if pokemon == "Venusaur":
        return Venusaur(100, 6, 10, False)


def chooserEnemy(enemy):
    if enemy == "Charizard":
        return Charizard(100, 4, 20, True)
    if enemy == "Blastoise":
        return Blastoise(100, 5, 30, True)
    if enemy == "Venusaur":
        return Venusaur(100, 6, 10, True)


def displayScores(pokemon, enemy):  #how to display normal names?
    print("\nUSER\nHealth:", pokemon.health, "\nDefense:", pokemon.defense)
    print("\nYOUNGSTER JOEY\nHealth:", enemy.health, "\nDefense:", enemy.defense)


def battle(pokemon, enemy):
    print("\nYoungster Joey challenges you! His pokemon is", enemy)
    pokemon = chooserPokemon(pokemon)
    des = pokemon.description
    print(des)
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
starters = ["Charizard", "Blastoise", "Venusaur"]
enemy = random.choice(starters)

while True:
    pokemon = str(input("\nPlease choose your pokemon (Charizard, Venusaur, or Blastoise) ")).title()
    if pokemon == 'Charizard' or pokemon == 'Venusaur'or pokemon == 'Blastoise':
        battle(pokemon, enemy)
    else:
        print("\nThis is 1st Generation pokemon. C'mon Mr. Stubbs you should know this...")
