import pygame

def calc_velocities(v1, v2, m1, m2) -> tuple:
    """Returns the final velocities of two blocks after a perfectly elastic
    collision when their respective mass and initial velocities are given."""

    base = (((2 * (m1 * v1)) + v2 * (m2 - m1))/(m1 + m2))
    add = v2 - v1

    return add + base, base


class Block:
    def __init__(self, x, y, velocity, mass, width, height):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.mass = mass
        self.width = width
        self.height = height

def run_collisions(m1, m2):
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


    B1 = Block(x=250, y=0, velocity=0, mass=m1, width=20, height=20)
    B2 = Block(x=500, y=0, velocity=-1, mass=m2, width=20, height=20)

    run = True
    collision_count = 0

    while run:

        if B2.velocity > B1.velocity >= 0:
            run = False
        else:
            pygame.time.delay(0)
            win.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.draw.rect(win, GREEN, (B1.x, B1.y, B1.width, B1.height))
            pygame.draw.rect(win, RED, (B2.x, B2.y, B2.width, B2.height))

            if B1.x + (B1.width / 2) >= B2.x - (B2.width / 2):
                B1.velocity, B2.velocity = calc_velocities(B1.velocity, B2.velocity, B1.mass, B2.mass)
                collision_count += 1

            elif B1.x < 0:
                B1.velocity = -B1.velocity
                collision_count += 1

            B1.x += B1.velocity
            B2.x += B2.velocity

            pygame.display.update()
            print(collision_count)

    pygame.quit()
    print(collision_count)

if __name__ == '__main__':
    run_collisions(1, 100000000)
