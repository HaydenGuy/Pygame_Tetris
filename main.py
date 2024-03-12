import pygame
import sys
import random

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Piece(pygame.sprite.Sprite):
    def __init__(self, spritesheet, x_sprite, y_sprite, x_pos, y_pos, index):
        super().__init__()
        self.sprite = self.get_sprite(spritesheet, x_sprite, y_sprite, 0, 0, index) # Gets the sprite from the spritesheet,
        self.image = self.sprite # Sets the image attribute to be self.sprite
        self.rect = self.image.get_rect(topleft=(x_pos, y_pos)) # Draws the sprite at x_pos, y_pos

    # Gets the sprite from the spritesheet
    def get_sprite(self, spritesheet, width, height, x_coord, y_coord, index):

        x_coord += width * index
        
        # Sets the surface to equal the width and height
        # Convert alpha to optimize the image and allow transparency
        image = pygame.Surface((width, height)).convert_alpha()

        # Blit copies a portion of the spritesheet onto the image surface
        image.blit(spritesheet, (0, 0), (x_coord, y_coord, width, height))

        # Keys the color from the spritesheet
        image.set_colorkey(WHITE)

        return image

    def move_down(self):
        self.rect.y += 40

# Draws the border for the playable area
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

# Im not sure this is working correctly yet
def random_piece(sprites_tuple, last_num):
    rand_num = random.randint(0, 7)
    if rand_num == last_num or rand_num == 7:
        rand_num = random.randint(0, 7)
        if rand_num == last_num:
            return sprites_tuple(rand_num)
        elif rand_num == 7:
            while rand_num >= 7:
                rand_num = random.randint(0, 7)
            return sprites_tuple(rand_num)
    else:
        return sprites_tuple(rand_num)


def main():
    # Initialize Pygame
    pygame.init()

    # Font
    font = pygame.font.Font(None, 36)

    # Set up display
    width, height = 800, 800
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Tetris")

    # Set up border
    border_x, border_y, border_width, border_height = draw_border(width, height)

    spritesheet = pygame.image.load("/home/linuxlaptop/Python/Pygame_Tetris/sprites/spritesheet.png")

    # Sprite group
    all_sprites = pygame.sprite.Group()

    # Create each piece (spawning values are placeholder)
    long_piece = Piece(spritesheet, 160, 120, border_height // 2.33 , (height - border_height) - 57, 0)
    Z_piece = Piece(spritesheet, 160, 120, border_height // 2.33 , (height - border_height) - 57, 1)
    S_piece = Piece(spritesheet, 160, 120, border_height // 2.33 , (height - border_height) - 57, 2)
    L_piece = Piece(spritesheet, 160, 120, border_height // 2.33 , (height - border_height) - 57, 3)
    T_piece = Piece(spritesheet, 160, 120, border_height // 2.33 , (height - border_height) - 57, 4)
    L_rev_piece = Piece(spritesheet, 160, 120, border_height // 2.33 , (height - border_height) - 57, 5)
    square_piece = Piece(spritesheet, 160, 120, border_height // 2.33 , (height - border_height) - 57, 6)

    # !!Work in progress to randomly choose a piece from this list and have it keep updating
    sprites_tuple = (long_piece, Z_piece, S_piece, L_piece, T_piece, L_rev_piece, square_piece)
    test = random_piece(sprites_tuple, 7)
    print(test)
    # ALSO REMOVED THE ALL_SPRITES GROUP
    
    # Timer variables
    move_timer = 0
    move_interval = 1000

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Exits game if user clicks quit
                pygame.quit()
                sys.exit()
            # if event.type == pygame.KEYUP and event.key == pygame.K_x:
            #     Z_piece.image = pygame.transform.rotate(Z_piece.image, 90)
            #     Z_piece.image.set_colorkey(WHITE)
            #     Z_piece.rect = Z_piece.image.get_rect(center=Z_piece.rect.center)

        # Check if it's time to move a piece down
        current_time = pygame.time.get_ticks()
        if current_time - move_timer > move_interval:
            Z_piece.move_down()
            move_timer = current_time # Reset the timer

        # Background color
        screen.fill(BLACK)

        # Draw the border
        pygame.draw.rect(screen, WHITE, (border_x, border_y, border_width, border_height), 3)

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