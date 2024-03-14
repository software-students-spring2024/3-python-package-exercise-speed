import pygame
pygame.init()

# Set dimentions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set window title
pygame.display.set_caption("PyDancer")

background_color = (250, 250, 250)


# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw screen
    screen.fill(background_color)
    pygame.display.flip()

pygame.quit()
