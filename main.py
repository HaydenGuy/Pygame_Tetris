import pygame
import sys

class Draw_Square(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move_down(self):
        self.rect.y += 40

def draw_border(width, height):
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

    return border_x, border_y, border_width, border_height

def main():
    # Initialize Pygame
    pygame.init()

    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    # Font
    font = pygame.font.Font(None, 36)

    # Set up display
    width, height = 800, 800
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Tetris")

    # Set up border
    border_x, border_y, border_width, border_height = draw_border(width, height)

    # Sprite group
    all_sprites = pygame.sprite.Group()

    # Placeholder red square, add to sprite group
    red_square = Draw_Square(RED, 50, 50)
    red_square.rect.x = border_height / 2 # Center of border_x
    red_square.rect.y = (height - border_height) / 2 # Top of inside of border_y 
    all_sprites.add(red_square)

    # Timer variables
    move_timer = 0
    move_interval = 1000

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Exits game if user clicks quit
                pygame.quit()
                sys.exit()

        # Check if it's time to move a piece down
        current_time = pygame.time.get_ticks()
        if current_time - move_timer > move_interval:
            red_square.move_down()
            move_timer = current_time # Reset the timer

        # Background color
        screen.fill(WHITE)

        # Draw the border
        pygame.draw.rect(screen, BLACK, (border_x, border_y, border_width, border_height), 3)

        # Update the sprites on screen
        all_sprites.update()

        # Draw sprites
        all_sprites.draw(screen)

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()