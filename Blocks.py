import pygame
import math


WIN_X = 1000
WIN_Y = 500

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


win = pygame.display.set_mode((WIN_X, WIN_Y))
pygame.init()
pygame.display.set_caption("π collider")


def calc_velocities(v1, v2, m1, m2) -> tuple:
    """Returns the final velocities of two blocks after a perfectly elastic
    collision when their respective mass and initial velocities are given."""

    base = (((2 * (m1 * v1)) + v2 * (m2 - m1))/(m1 + m2))
    add = v2 - v1

    return add + base, base


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity, mass, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.velocity = velocity
        self.mass = mass
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()

    def draw(self, window, color):
        pygame.draw.rect(window, color, (self.x, self.y, self.width, self.height))
        pygame.display.update()

    def move(self):
        self.x += self.velocity



def main():
    B1 = Block(x=(WIN_X / 2), y=0, velocity=0, mass=1, width=20, height=20)
    B2 = Block(x=WIN_X-20, y=0, velocity=-1, mass=100, width=20, height=20)
    run = True
    while run:
        pygame.time.delay(10)
        win.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if B2.velocity > B1.velocity >= 0:
            run = False
        else:


            if math.ceil(B1.x + B1.width) == math.ceil(B2.x):
                B1.velocity, B2.velocity = calc_velocities(B1.velocity, B2.velocity, B1.mass, B2.mass)

            elif math.floor(B1.x) < 0:
                B1.velocity = -B1.velocity

            B1.draw(win, GREEN)
            B1.move()

            B2.draw(win, RED)
            B2.move()



    pygame.quit()



if __name__ == '__main__':
    main()
