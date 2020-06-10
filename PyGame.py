import pygame


# Vars
WIDTH = 1200
HEIGHT = 600
BORDER = 20
fg_colour = pygame.Color("white")

# Draw scenario
pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT)) # set window size

# position borders
pygame.draw.rect(screen, fg_colour, pygame.Rect((0,0),(WIDTH,BORDER)))
pygame.draw.rect(screen, fg_colour, pygame.Rect((0,HEIGHT - BORDER),(WIDTH,HEIGHT)))
pygame.draw.rect(screen, fg_colour, pygame.Rect((0,0),(BORDER,HEIGHT)))

# draw to screen
pygame.display.flip()

# on close x being pressed break out and close the game
while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break

pygame.quit()