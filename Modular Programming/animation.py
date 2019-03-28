
import pygame

background = pygame.image.load('background2.png')
background = pygame.transform.scale(background, (900, 400))

charizard = pygame.image.load('charizard.bmp.png')
charizard = pygame.transform.scale(charizard, (300, 300))

blastoise = pygame.image.load('blastoise.png')
blastoise = pygame.transform.scale(blastoise, (200, 200))

venusaur = pygame.image.load('venusaur.png')
venusaur = pygame.transform.scale(venusaur, (200, 200))


xx=0
health_bar_width = 100
maxHP = 100
currentHP = 50
value = 10
per = (int(max(min(currentHP / float(maxHP) * health_bar_width, health_bar_width), 0)))

white = (255,255,255)


def run_game():
    screen = pygame.display.set_mode((900, 400))
    screen.fill(white)
    pygame.display.update()
    pygame.display.set_caption("Pokemon!")

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        for i in range(10):
            pygame.draw.rect(background, white, per, 0)

        screen.blit(background,(10,10))
        screen.blit(charizard,(100,100))
        screen.blit(blastoise,(600,60))
        screen.blit(venusaur,(600,60))


        pygame.display.flip()
        # Make the most recently drawn screen visible.
    pygame.quit()
run_game()
