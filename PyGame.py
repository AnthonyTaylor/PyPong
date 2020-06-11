import pygame

# Vars
WIDTH = 1200
HEIGHT = 600
BORDER = 20
fg_colour = pygame.Color("yellow")
bg_colour = pygame.Color("black")

VELOCITY = 1
FRAMERATE = 400

# Draw scenario
pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT)) # set window size


class Ball:
    radius = 20
    def __init__(self, x,y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def show(self, colour):
        global screen
        pygame.draw.circle(screen, colour, (self.x, self.y), self.radius)

    def update(self):
        global bg_colour, fg_colour

        new_x = self.x + self.vx
        new_y = self.y + self.vy

        if new_x < BORDER + self.radius:
            self.vx = -self.vx
        elif new_y < BORDER + self.radius or new_y > HEIGHT-BORDER-self.radius:
            self.vy = -self.vy
        else:
            self.show(bg_colour)
            self.x += self.vx
            self.y += self.vy
            self.show(fg_colour)


class Paddle:
    WIDTH = 20
    HEIGHT = 100

    def __init__(self, y):
        self.y = y

    def show(self, colour):
        global screen
        paddle_padding = 20

        pygame.draw.rect(screen, colour, pygame.Rect(
            (WIDTH - self.WIDTH, self.y-self.HEIGHT//2),
            (self.WIDTH, self.HEIGHT)))
    
    def update(self):
        self.show(bg_colour)
        self.y = pygame.mouse.get_pos()[1]
        self.show(fg_colour)


# Create objects
ball_play = Ball(WIDTH - Ball.radius, HEIGHT//2, -VELOCITY, VELOCITY)
paddle_play = Paddle(HEIGHT // 2)

# position borders
pygame.draw.rect(screen, fg_colour, pygame.Rect((0,0),(WIDTH,BORDER)))
pygame.draw.rect(screen, fg_colour, pygame.Rect((0,HEIGHT - BORDER),(WIDTH,HEIGHT)))
pygame.draw.rect(screen, fg_colour, pygame.Rect((0,0),(BORDER,HEIGHT)))


ball_play.show(fg_colour)
paddle_play.show(fg_colour)

clock = pygame.time.Clock()

# on close x being pressed break out and close the game
while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break
    clock.tick(FRAMERATE)

    # draw to screen
    pygame.display.flip()

    ball_play.update()
    paddle_play.update()

pygame.quit()