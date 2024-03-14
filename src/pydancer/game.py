import pygame
pygame.init()

# Set dimentions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set window title
pygame.display.set_caption("PyDancer")

# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw screen
    screen.fill((0, 0, 0))
    pygame.display.flip()

pygame.quit()
