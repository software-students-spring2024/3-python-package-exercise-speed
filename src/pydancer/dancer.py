import pygame
from .constants import * 
from .functions import * 

def play():
    pygame.init()

    # Create screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set window title
    pygame.display.set_caption(GAME_NAME)
    # set up images
    dancer_image = load_image("../images/dancer.png")
    dancer_image = scale_image(dancer_image, 128, 128)

    # Game loop
    running = True
    last_event_time = pygame.time.get_ticks()
    while running:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # end loop if no events in 30 seconds
        elapsed_time = pygame.time.get_ticks() - last_event_time

        if elapsed_time >= TIMEOUT_DURATION:
            running = False

        # Draw screen
        screen.fill(BACKGROUND_COLOR)
        display_image(screen, dancer_image, SCREEN_WIDTH * .4 , SCREEN_HEIGHT * .1)

        pygame.display.flip()

    pygame.quit()

