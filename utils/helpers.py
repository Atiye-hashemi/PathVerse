import pygame

# Initialize
pygame.init()

# Window settings
WIDTH = 600
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Zen Path Finder")

# Colors
WHITE = (255, 255, 255)
GREY = (200, 200, 200)

ROWS = 20
CELL_SIZE = WIDTH // ROWS


def draw_grid():
    for row in range(ROWS):
        for col in range(ROWS):
            pygame.draw.rect(
                WIN,
                WHITE,
                (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )
            pygame.draw.rect(
                WIN,
                GREY,
                (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                1
            )


def main():
    run = True
    while run:
        draw_grid()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == "__main__":
    main()