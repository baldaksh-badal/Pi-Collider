import pygame


#   DIMENSIONS
WIDTH, HEIGHT = 900, 500

#   CONSTANTS
WHITE = (255, 255, 255)
FPS = 60

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

#   TITLE
pygame.display.set_caption("π Collider")


def draw_window():
    WINDOW.fill(WHITE)
    pygame.display.update()


#   GAME LOOP
def main():
    running = True

    while running:
        pygame.time.Clock().tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_window()
        pygame.display.flip()

    pygame.quit()


#   SO THIS DOESN'T RUN IF THIS MODULE IS IMPORTED
if __name__ == "__main__":
    main()

