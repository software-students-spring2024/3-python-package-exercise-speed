from os import environ
import pygame
from .constants import *
from .functions import *
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Holds an element that we want to display on the screen and potentially move around
class Component:
    speed = 0

    def __init__(self, image, pos):
        self.image = image
        self.pos = pos

    # returns x position to draw from so that the actual pos.x is centered
    def get_draw_x(self):
        return self.pos.x - (self.image.get_width() / 2)

    # returns y position to draw from so that the actual pos.y is centered
    def get_draw_y(self):
        return self.pos.y - (self.image.get_height() / 2)

    # display the component on the screen
    def display(self, screen):
        display_image(screen, self.image, self.get_draw_x(), self.get_draw_y())

def generate_arrow(direction) -> Component:
    # generate path
    path = "../images/" + direction + "_arrow_filled.png"

    # load and scale image
    arrow_image = load_image(path)
    arrow_image = scale_image(arrow_image, ARROW_WIDTH, ARROW_HEIGHT)

    # set the x position based on direction
    pos_x = 0
    if direction == "up":
        pos_x = SCREEN_WIDTH * .6
    elif direction == "down":
        pos_x = SCREEN_WIDTH * .4
    elif direction == "left":
        pos_x = SCREEN_WIDTH * .2
    elif direction == "right":
        pos_x = SCREEN_WIDTH * .8

    # create the component and set speed
    arrow = Component(arrow_image, Pos(pos_x, SCREEN_HEIGHT * 1.1))
    arrow.speed = 70 

    return arrow

def play():
    pygame.init()

    # Pygame setup
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_NAME)
    clock = pygame.time.Clock()
    # last_event_time = pygame.time.get_ticks()

    # set up components 
    dancer_image = load_image("../images/dancer.png")
    dancer_image = scale_image(dancer_image, DANCER_WIDTH, DANCER_HEIGHT)
    dancer = Component(dancer_image, Pos(SCREEN_WIDTH * .5 , SCREEN_HEIGHT * .1))

    end_area_image = load_image("../images/end_area.png")
    end_area_image = scale_image(end_area_image, SCREEN_WIDTH, SCREEN_HEIGHT * .2)
    end_area = Component(end_area_image, Pos(SCREEN_WIDTH * .5, SCREEN_HEIGHT * .3))

    arrows = [generate_arrow("up"), generate_arrow("down"), generate_arrow("left"), generate_arrow("right")]

    # Set a timer to add an arrow to the screen every x milliseconds
    ADD_ARROW = pygame.USEREVENT 
    milliseconds = 2000
    pygame.time.set_timer(ADD_ARROW, milliseconds)

    # Game Loop
    running = True
    while running:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

            if event.type == pygame.KEYDOWN:
                # checking if key "A" was pressed
                if event.key == pygame.K_LEFT:
                    pass

            if event.type == ADD_ARROW:
                arrows.append(generate_arrow("up"))
                arrows.append(generate_arrow("down"))
                arrows.append(generate_arrow("left"))
                arrows.append(generate_arrow("right"))

        # delta time is needed to make updates independent of the frame rate
        delta_time = clock.tick(FPS)/1000

        # update arrow positions
        for arrow in arrows:
            arrow.pos.y -= arrow.speed * delta_time

        # Draw screen
        screen.fill(BACKGROUND_COLOR)

        # display components
        end_area.display(screen)
        dancer.display(screen)
        for arrow in arrows:
            arrow.display(screen)
            
        # remove arrows that go out of the screen
        for arrow in arrows:
            if arrow.pos.y < -arrow.image.get_height():
                # This is terrible in terms big O however
                # number of arrows on screen will never be 
                # too big to cause trouble
                arrows.remove(arrow)

        pygame.display.flip()

    pygame.quit()

