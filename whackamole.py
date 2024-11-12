import pygame
import random

WIDTH = 640
HEIGHT = 512
SQUARE_SIZE = 32
BOARD_ROWS = 16
BOARD_COLS = 20
LINE_WIDTH = 2
#color?
LINE_COLOR = (0, 0, 0)


def main():
    pygame.init()

    mole_image = pygame.image.load("mole.png")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    mole_x = 0
    mole_y = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                mole_grid_x = mole_x // SQUARE_SIZE
                mole_grid_y = mole_y // SQUARE_SIZE

                clicked_grid_x = mouse_x // SQUARE_SIZE
                clicked_grid_y = mouse_y // SQUARE_SIZE

                # if inside, do random
                if clicked_grid_x == mole_grid_x and clicked_grid_y == mole_grid_y:
                    mole_x = random.randrange(0, BOARD_COLS) * SQUARE_SIZE
                    mole_y = random.randrange(0, BOARD_ROWS) * SQUARE_SIZE

        screen.fill("light green")

        # draw grid
        for i in range(1, BOARD_ROWS):
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (0, i * SQUARE_SIZE),
                (WIDTH, i * SQUARE_SIZE),
                LINE_WIDTH
            )

        for i in range(1, BOARD_COLS):
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (i * SQUARE_SIZE, 0),
                (i * SQUARE_SIZE, HEIGHT),
                LINE_WIDTH
            )

        screen.blit(mole_image, (mole_x, mole_y)) # not top left = ?
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()