import pygame
import sys


def main():
    # Initialize Pygame
    pygame.init()

    # Set up display
    width, height = 800, 800
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Tetris")
    
    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Calculate 95% of the screen width and height
    border_width = int(0.95 * width)
    border_height = int(0.95 * height)

    border_scale = (10, 20)

    # Width and height to fit the scale
    border_width = min(border_width, border_height * border_scale[0] // border_scale[1])
    border_height = min(border_height, border_width * border_scale[1] // border_scale[0])

    # Position to center the border
    border_x = (width - border_width) / 2
    border_y = (height - border_height) / 2

    # Font
    font = pygame.font.Font(None, 36)

    # Load sprites
    # sprite = pygame.image.load("")


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Exits game if user clicks quit
                pygame.quit()
                sys.exit()

        # Background color
        screen.fill(WHITE)

        # Draw the border
        pygame.draw.rect(screen, BLACK, (border_x, border_y, border_width, border_height), 3)

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()