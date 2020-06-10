import pygame

# Vars
WIDTH = 1200
HEIGHT = 600
BORDER = 20
fg_colour = pygame.Color("yellow")
paddle_height = 50
paddle_width = 10
paddle_padding = 20


# Draw scenario
pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT)) # set window size

# position borders
pygame.draw.rect(screen, fg_colour, pygame.Rect((0,0),(WIDTH,BORDER)))
pygame.draw.rect(screen, fg_colour, pygame.Rect((0,HEIGHT - BORDER),(WIDTH,HEIGHT)))
pygame.draw.rect(screen, fg_colour, pygame.Rect((0,0),(BORDER,HEIGHT)))

# position paddle
pygame.draw.rect(screen, fg_colour, pygame.Rect(
    (WIDTH - paddle_width - paddle_padding, (HEIGHT / 2) - (paddle_height / 2)),
    (paddle_width - paddle_padding, paddle_height)))


# draw to screen
pygame.display.flip()

# on close x being pressed break out and close the game
while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break

pygame.quit()