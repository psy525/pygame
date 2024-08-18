import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Character Change on Item Collect")

# Load character images
character_files = ['../image/J.png', '../image/R.png', '../image/L.png', '../image/S.png', '../image/sky.png',
                   '../image/O.png', '../image/P.png']
characters = [pygame.image.load(file).convert_alpha() for file in character_files]

# Define rainbow colors
rainbow_colors = [
    (255, 0, 0),  # Red
    (255, 127, 0),  # Orange
    (255, 255, 0),  # Yellow
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (75, 0, 130),  # Indigo
    (148, 0, 211)  # Violet
]

# Map colors to characters
color_to_character = {
    (255, 0, 0): characters[1],  # Red
    (255, 127, 0): characters[5],  # Orange
    (255, 255, 0): characters[4],  # Yellow
    (0, 255, 0): characters[2],  # Green
    (0, 0, 255): characters[3],  # Blue
    (75, 0, 130): characters[6],  # Indigo
    (148, 0, 211): characters[0]  # Violet
}

# Initial character
current_character = characters[0]  # Start with J.png

# Load item image (base image)
item_image = pygame.image.load("../image/구슬.png").convert_alpha()
item_width, item_height = item_image.get_width(), item_image.get_height()


# Function to colorize the bead image
def colorize_image(image, color):
    colored_image = pygame.Surface((item_width, item_height), pygame.SRCALPHA)
    colored_image.blit(image, (0, 0))

    # Create a surface for color overlay
    overlay = pygame.Surface((item_width, item_height), pygame.SRCALPHA)
    overlay.fill(color)

    # Apply color using blend mode
    colored_image.blit(overlay, (0, 0), special_flags=pygame.BLEND_MULT)

    return colored_image


# Define bead properties
bead_x = SCREEN_WIDTH
bead_y = random.randint(0, SCREEN_HEIGHT - item_height)
bead_color = random.choice(rainbow_colors)
colored_bead_image = colorize_image(item_image, bead_color)

bead_speed = 5
color_change_interval = 3000  # 3 seconds for color change
last_color_change_time = pygame.time.get_ticks()

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move bead
    bead_x -= bead_speed
    if bead_x < -item_width:
        bead_x = SCREEN_WIDTH
        bead_y = random.randint(0, SCREEN_HEIGHT - item_height)
        bead_color = random.choice(rainbow_colors)
        colored_bead_image = colorize_image(item_image, bead_color)

    # Check for color change
    current_time = pygame.time.get_ticks()
    if current_time - last_color_change_time > color_change_interval:
        bead_color = random.choice(rainbow_colors)
        colored_bead_image = colorize_image(item_image, bead_color)
        last_color_change_time = current_time

    # Check collision
    character_rect = pygame.Rect(SCREEN_WIDTH // 2 - current_character.get_width() // 2,
                                 SCREEN_HEIGHT // 2 - current_character.get_height() // 2,
                                 current_character.get_width(), current_character.get_height())
    bead_rect = pygame.Rect(bead_x, bead_y, item_width, item_height)

    if character_rect.colliderect(bead_rect):
        current_character = color_to_character[bead_color]
        bead_x = SCREEN_WIDTH  # Reset bead position

    # Clear screen
    screen.fill((255, 255, 255))

    # Draw the current character
    screen.blit(current_character, (
    SCREEN_WIDTH // 2 - current_character.get_width() // 2, SCREEN_HEIGHT // 2 - current_character.get_height() // 2))

    # Draw the colored bead
    screen.blit(colored_bead_image, (bead_x, bead_y))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()