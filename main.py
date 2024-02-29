import pygame
import sys


def main():
    # Initialize Pygame
    pygame.init()

    # Set up display
    width, height = 800, 800
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Tetris")

    # Background color
    bg_color = (0, 0, 0)

    # Font
    font = pygame.font.Font(None, 36)

    # Load sprites
    # sprite = pygame.image.load("")


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Exits game if user clicks quit
                pygame.quit()
                sys.exit()

        # Fill the background color
        screen.fill(bg_color)

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()