import pygame

def play():
    pygame.init()

    # Set dimentions
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

    # Create screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set window title
    pygame.display.set_caption("PyDancer")

    background_color = (250, 250, 250)

    timeout_duration = 30000 #30 seconds

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
        if elapsed_time >= timeout_duration:
            running = False

        # Draw screen
        screen.fill(background_color)
        pygame.display.flip()

    pygame.quit()
