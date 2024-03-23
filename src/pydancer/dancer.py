import pygame
# from .constants import * 
# from .functions import * 

# Constants bc I can't fix import errors
GAME_NAME = "PyDancer"
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BACKGROUND_COLOR = (250, 250, 250)
TIMEOUT_DURATION = 30000  # 30 seconds

# image functions because I can't fix import errors
def load_image(image_path):
    return pygame.image.load(image_path)

def display_image(screen, image, x, y):
    screen.blit(image, (x, y))

def scale_image(image, x, y):
    return pygame.transform.scale(image, (x, y))



def play():
    pygame.init()

    # Create screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set window title
    pygame.display.set_caption(GAME_NAME)
    # set up images
    dancer_image = load_image("images/dancer.png")
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

