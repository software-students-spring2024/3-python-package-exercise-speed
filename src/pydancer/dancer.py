from os import environ
import pygame
from .constants import *
from .functions import *
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Component:
    def __init__(self, image, pos):
        self.image = image
        self.pos = pos

    # returns x position to draw from so that the actual pos.x is centered
    def get_draw_x(self):
        return self.pos.x - (self.image.get_width() / 2)

    # returns y position to draw from so that the actual pos.y is centered
    def get_draw_y(self):
        return self.pos.y - (self.image.get_height() / 2)

def play():
    pygame.init()

    # Pygame setup
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_NAME)
    clock = pygame.time.Clock()
    last_event_time = pygame.time.get_ticks()

    # set up components 
    dancer_image = load_image("../images/dancer.png")
    dancer_image = scale_image(dancer_image, DANCER_WIDTH, DANCER_HEIGHT)
    dancer = Component(dancer_image, Pos(SCREEN_WIDTH * .4 , SCREEN_HEIGHT * .1))

    up_arrow_image = load_image("../images/up_arrow_filled.png")
    up_arrow_image = scale_image(up_arrow_image, ARROW_WIDTH, ARROW_HEIGHT)
    up_arrow = Component(up_arrow_image, Pos(SCREEN_WIDTH * .4, SCREEN_HEIGHT * .9))

    down_arrow_image = load_image("../images/down_arrow_filled.png")
    down_arrow_image = scale_image(down_arrow_image, ARROW_WIDTH, ARROW_HEIGHT)
    down_arrow = Component(down_arrow_image, Pos(SCREEN_WIDTH * .6, SCREEN_HEIGHT * .9))

    left_arrow_image = load_image("../images/left_arrow_filled.png")
    left_arrow_image = scale_image(left_arrow_image, ARROW_WIDTH, ARROW_HEIGHT)
    left_arrow = Component(left_arrow_image, Pos(SCREEN_WIDTH * .2, SCREEN_HEIGHT * .9))

    right_arrow_image = load_image("../images/right_arrow_filled.png")
    right_arrow_image = scale_image(right_arrow_image, ARROW_WIDTH, ARROW_HEIGHT)
    right_arrow = Component(right_arrow_image, Pos(SCREEN_WIDTH * .8, SCREEN_HEIGHT * .9))

    running = True
    while running:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # delta time is needed to make updates independent of the frame rate
        delta_time = clock.tick(FPS)/1000

        up_arrow.pos.y -= 20 * delta_time
        down_arrow.pos.y -= 20 * delta_time
        left_arrow.pos.y -= 20 * delta_time
        right_arrow.pos.y -= 20 * delta_time

        # Draw screen
        screen.fill(BACKGROUND_COLOR)
        display_image(screen, dancer.image, dancer.pos.x, dancer.pos.y)
        display_image(screen, up_arrow.image, up_arrow.get_draw_x(), up_arrow.pos.y)
        display_image(screen, down_arrow.image, down_arrow.get_draw_x(), down_arrow.pos.y)
        display_image(screen, left_arrow.image, left_arrow.get_draw_x(), left_arrow.pos.y)
        display_image(screen, right_arrow.image, right_arrow.get_draw_x(), right_arrow.pos.y)

        pygame.display.flip()

    pygame.quit()

