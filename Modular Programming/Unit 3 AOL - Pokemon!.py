import random
import pygame
'''
#######################################################
####################---Classes---######################
#######################################################
'''
'''
this is the main class that all the other classes inherit. It includes all the moves that each pokemon has except for 
the type moves.
'''
class Sprite:
    '''
    this initializing only includes attributes that remain the same throughout the other classes
    '''
    def __init__(self, health, isEnemy):
        self.health = health
        self.isEnemy = isEnemy
    '''
    this method increases the defense of either the enemy or the user.
    '''
    def bulkUp(self):
        d = int(random.randint(1,3))
        self.defense += d
        print("\nDefense increased by", d)

    '''
    only increases health if total health will be less 100. otherwise, it will just max health.
    '''
    def rest(self):
        r = random.randint(3,7)
        if self.health + r < 100:
            self.health += r
            print("\nHealth increased by", r)
        else:
            self.health = 100
            print("\nHealth is maxed")
    '''
    health of the type(either enemy or user) is deducted by damage, less whatever defense value that pokemon has
    '''
    def tackle(self, type):
        damage = random.randint(20,25)
        type.health -= damage - type.defense
        net = damage - type.defense
        print("\nThe attack hit with", damage, "damage, but defended by", type.defense, "points, netting", net,
              "damage")  # gives a detailed description of the move
    '''
    this method is what forms the animation in the game. first, the background is formed and a caption is set.
    then, depending on if it is an enemy or the user, health and health bars are made. after that, everything is
    drawn onto the board. in the sub classes, the pokemon images are formed and scaled depending on if it is an
    enemy or user.
    '''
    def draw_health(self, type):
        background = pygame.image.load('background2.png')
        background = pygame.transform.scale(background, (900, 400))
        # load and scale background ^^
        screen = pygame.display.set_mode((900, 400))
        pygame.display.set_caption("Pokemon!")
        pygame.font.init()
        h = pygame.font.SysFont('Comic Sans MS', 30)

        maxhp = 100  # this is needed for forming in the health bars

        if type.isEnemy:
            playerHealth = h.render("Health: " + str(type.health), False, (0, 0, 0))  # how to display health?
            enemyHealth = h.render("Health: " + str(self.health), False, (0, 0, 0))
            # when is the enemy,

            width = int(self.health)  # width of health bar is relative to that of how much health there is
            health_bar = pygame.Rect(150, 60, width, 7)
            border = pygame.Rect(140, 56, 120, 17)
            # the numbers set the size and position

            width2 = int(type.health)
            health_bar2 = pygame.Rect(700, 300, width2, 7)
            border2 = pygame.Rect(690, 296, 120, 17)

            # the code above had to be duplicated for when the user comes into this method because the health
            # bar positions and the actual health values need to be in the same spot every time.

        else:
            # does the same thing as code above, just flipped for the user.
            playerHealth = h.render("Health: " + str(self.health), False, (0, 0, 0))
            enemyHealth = h.render("Health: " + str(type.health), False, (0, 0, 0))

            width = int(100 * type.health / maxhp)
            health_bar = pygame.Rect(150, 60, width, 7)
            border = pygame.Rect(140, 56, 120, 17)
            # enemy health located in the same spot ^

            width2 = int(100 * self.health / maxhp)
            health_bar2 = pygame.Rect(700, 300, width2, 7)
            border2 = pygame.Rect(690, 296, 120, 17)
            # user health located in the same spot

        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # when the window is exited, pygame successfully closes
                    done = True

            black = (0,0,0)  # used for health bar border
            green = (50,205,50)
            # I decided to just use green as the health bar colour because in order to implement changing colours, I
            # would have to be super repetitive.

            pygame.draw.rect(background, black, border)
            pygame.draw.rect(background, green, health_bar)
            pygame.draw.rect(background, black, border2)
            pygame.draw.rect(background, green, health_bar2)
            # code above actually draws it on the board.
            pygame.display.update()

            screen.blit(background, (0, 0))  # want the background to be centered

            if type.isEnemy:  # the code below puts the pokemon onto the screen. this needs to be done in a different
                # condition because the background needs to be put on first.
                screen.blit(self.picture, (100, 100))
                screen.blit(type.picture, (600, 60))
            else:
                screen.blit(type.picture, (100, 100))
                screen.blit(self.picture, (600, 60))

            screen.blit(playerHealth, (600, 350))
            screen.blit(enemyHealth, (50, 20))
            #  finally, the healths are put on the board with the appropriate dimentions

            pygame.display.flip()  # Make the most recently drawn screen visible.
        pygame.quit()  # needed syntax for a smooth shut down
'''
this class inherits the Sprite class, so it receives all of the methods above. the only thing unique about all
the rest of the classes are the type moves (flamethrower, leaf storm, and hydro pump). note that I won't be
giving block or line comments for the rest of the classes because they are virtually the same, just with different
moves.
'''
class Charizard(Sprite):
    def __init__(self, health=100, defense=5, speed=20, isEnemy=True):  # efficient programming to gives these
        # attributes values here. isEnemy = True is default, but it is false if the user enters the class
        super().__init__(health, isEnemy)  # inherited
        self.defense = defense
        self.speed = speed
        self.picture = pygame.image.load('charizard.bmp.png')  # loads image
        self.description = "\nCharizard is the second fastest and the second bulkiest pokemon" \
                           "\nFlamethrower does the second most damage of all the type-moves"
        # description above displays after the user chooses pokemon.

        # conditional statement below scales picture depending on if it an enemy or user
        if self.isEnemy:
            self.picture = pygame.transform.scale(self.picture, (200, 200))
        else:
            self.picture = pygame.transform.scale(self.picture, (300, 300))

    '''
    this method is the same in all the rest of the classes. the only things that change are the effectiveness
    of the move depending on which pokemon it is attacking. damage if different for each pokemon to balance
    the playing field. the damage system here works the same as it does in the tackle method.
    '''
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
        # nice statement outlining gross damage, defense and net damage

'''
same function as above, just with a differnt move and pokemon.
'''
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

'''
again, virtually the same as before. 
'''
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

'''
#######################################################
####################---Functions---####################
#######################################################
'''
'''
this function asks the user to choose a move depending on what pokemon they have, then goes into that specific class
and performs the move.
'''
def pokemonMove(pokemon, enemy):
    while True:
        choice = ''  # eliminates the unbound local variable error
        if isinstance(pokemon, Charizard):
            choice = input("\nPlease select a move (bulk up, tackle, flamethrower, or rest) ").lower()
        if isinstance(pokemon, Blastoise):
            choice = input("\nPlease select a move (bulk up, tackle, hydro pump, or rest) ").lower()
        if isinstance(pokemon, Venusaur):
            choice = input("\nPlease select a move (bulk up, tackle, leaf storm, or rest) ").lower()

        # all the conditional statements below just go into the respective methods depending on what move the user
        # chooses
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
            continue  # prevents the loop from breaking
        if enemy.health > 0:  # only shows the animation if the enemy is still 'alive'
            pokemon.draw_health(enemy)
        break


'''
this function chooses the enemy's move, and also incorporates intelligent computer guessing
'''
def enemyMove(pokemon, enemy):
    choice = ''
    C = ["bulk up", "rest", "flamethrower", "tackle"]
    S = ["bulk up", "rest", "hydro pump", "tackle"]
    B = ["bulk up", "rest", "leaf storm", "tackle"]
    # above are the default move sets.

    if enemy.health < 30:  # if the enemy is less than 30 hp, rest will be added once more to the list of moves
        for i in range(0,1):
            C.append("rest")
            S.append("rest")
            B.append("rest")

    # for the following conditions, if the enemy has a type advantage, they use use their type move more often,
    # and if they have a type disadvantage, they will use tackle more often
    if isinstance(enemy, Charizard):
        if isinstance(pokemon, Venusaur):
            C = ["bulk up", "rest", "flamethrower","flamethrower", "tackle"]
        if isinstance(pokemon, Blastoise):
            C = ["bulk up", "rest","flamethrower", "tackle", "tackle"]

        choice = random.choice(C)

    if isinstance(enemy, Blastoise):
        if isinstance(pokemon, Charizard):
            S = ["bulk up", "rest", "hydro pump","hydro pump", "tackle"]
        if isinstance(pokemon, Venusaur):
            S = ["bulk up", "rest", "hydro pump", "tackle", "tackle"]

        choice = random.choice(S)

    if isinstance(enemy, Venusaur):
        if isinstance(pokemon, Blastoise):
            B = ["bulk up", "rest", "leaf storm","leaf storm", "tackle"]
        if isinstance(pokemon, Charizard):
            B = ["bulk up", "rest","leaf storm", "tackle", "tackle"]

        choice = random.choice(B)

    print("\nYoungster Joey used {0}!".format(choice))

    # this is the same as when the user goes in, only it is the enemy attacking the user.
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

'''
the following two functions turn the strings of pokemon and enemy into iterable class names. the last
attribute inside the pokemon def is false because that indicates they are not an enemy. vise versa for enemy
'''
def chooserPokemon(pokemon):
    if pokemon == "Charizard":
        return Charizard(100, 4, 20, False)
    if pokemon == "Blastoise":
        return Blastoise(100, 5, 30, False)
    if pokemon == "Venusaur":
        return Venusaur(100, 6, 10, False)


def chooserEnemy(enemy): # may not be needed
    if enemy == "Charizard":
        return Charizard(100, 4, 20, True)
    if enemy == "Blastoise":
        return Blastoise(100, 5, 30, True)
    if enemy == "Venusaur":
        return Venusaur(100, 6, 10, True)

'''
I decided to make a definition to display the health and defense because I do it every time after the user/enemy
goes, so this is more efficient than just repeating it several times
'''
def displayScores(pokemon, enemy):
    print("\nUSER\nHealth:", pokemon.health, "\nDefense:", pokemon.defense)
    print("\nYOUNGSTER JOEY\nHealth:", enemy.health, "\nDefense:", enemy.defense)

'''
the main function that call on every other function. this function runs while both the enemy and user have health
greater than 0. depending on which pokemon is faster, it allows then to go first. after the loop is broken, it
shows who won and offers the user to play again.
'''
def battle(pokemon, enemy):
    # the code below changes the strings of the pokemon and user into objects and then prints the description of both
    pokemon = chooserPokemon(pokemon)
    des = pokemon.description
    print(des)
    print("\nYoungster Joey challenges you! His pokemon is", enemy)
    enemy = chooserEnemy(enemy)
    des2 = enemy.description
    print(des2)

    while pokemon.health > 0 and enemy.health > 0:

        if pokemon.speed >= enemy.speed:  # pokemon will go first
            pokemonMove(pokemon, enemy)
            if enemy.health <= 0:  # if this move kills the enemy, the loop will break
                break
            displayScores(pokemon, enemy)
            enemyMove(pokemon, enemy)
            if pokemon.health <= 0:  # if this move kills the player, the loop will break
                break
            displayScores(pokemon, enemy)
            # scores display after every move

        else:  # same as above, just the enemy goes first
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
        exit()  # exits the program
    # otherwise, the loop below will continue running

'''
#######################################################
####################---Main Code---####################
#######################################################
'''

starters = ["Charizard", "Blastoise", "Venusaur"] # charizard () here? how to print out?
enemy = random.choice(starters)  # enemy pokemon is random

while True:
    pokemon = str(input("\nPlease choose your pokemon (Charizard, Venusaur, or Blastoise) ")).title()
    if pokemon == 'Charizard' or pokemon == 'Venusaur'or pokemon == 'Blastoise':
        battle(pokemon, enemy)  # enter the main def
    else:  # defensive coding
        print("\nThis is 1st Generation pokemon. C'mon Mr. Stubbs you should know this...")
