from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

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

    up_arrow_image = load_image("../images/up_arrow_filled.png")
    up_arrow_image = scale_image(up_arrow_image, 64, 64)

    down_arrow_image = load_image("../images/down_arrow_filled.png")
    down_arrow_image = scale_image(down_arrow_image, 64, 64)

    left_arrow_image = load_image("../images/left_arrow_filled.png")
    left_arrow_image = scale_image(left_arrow_image, 64, 64)

    right_arrow_image = load_image("../images/right_arrow_filled.png")
    right_arrow_image = scale_image(right_arrow_image, 64, 64)
    
    # Game loop
    running = True
    last_event_time = pygame.time.get_ticks()
    while running:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw screen
        screen.fill(BACKGROUND_COLOR)
        display_image(screen, dancer_image, SCREEN_WIDTH * .4 , SCREEN_HEIGHT * .1)
        display_image(screen, up_arrow_image, 0, 0)
        display_image(screen, down_arrow_image, 50, 10)
        display_image(screen, left_arrow_image, 90, 20)
        display_image(screen, right_arrow_image, 200, 30)

        pygame.display.flip()

    pygame.quit()

