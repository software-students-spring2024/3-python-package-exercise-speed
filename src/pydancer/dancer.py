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
    pos = Pos(0, 0)
    left = 0
    right = 0
    up = 0
    bottom = 0
    speed = 0

    def __init__(self, image, pos):
        self.image = image
        self.set_pos(pos)

    def set_pos(self, pos):
        self.pos = pos
        self.left = self.pos.x - (self.image.get_width() / 2)
        self.right = self.pos.x + (self.image.get_height() / 2)
        self.top = self.pos.y - (self.image.get_height() / 2)
        self.bottom = self.pos.y + (self.image.get_height() / 2)

    # display the component on the screen
    def display(self, screen):
        # render from top left of the image so that (pos.x, pos.y) is centered
        display_image(screen, self.image, self.left, self.top)

    def percent_inside_of(self, other) -> int:
        # it's outside 
        if (self.top > other.bottom 
            or self.bottom < other.top
            or self.left > other.right 
            or self.right < other.left):

            return 0;
            
        height = 0
        if (self.bottom > other.bottom):
            height = min((other.bottom - self.top), self.image.get_height(), other.image.get_height())
        elif (self.top > other.top):
            height = min((self.bottom - other.top), self.image.get_height(), other.image.get_height())

        width = 0
        if (self.right > other.right):
            width = min((other.right - self.left), self.image.get_width(), other.image.get_width())
        elif (self.left > other.left):
            width = min((self.right - other.left), self.image.get_width(), other.image.get_width())

        area_self = self.image.get_width() * self.image.get_height()
        area_inside = height * width

        return (area_inside / area_self) * 100 
        

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
                # TODO: check key events for other arrows
                if event.key == pygame.K_LEFT:
                    # TODO: Check if there is a left arrow in the target area, 
                    # if so replace it's image with glowing one, if not
                    # play fail sound and make the animation glitch

                    # NOTE: You can check if an arrow is in the target area with
                    # arrow.percent_inside_of(end_area)
                    # it's fully inside if 100, it's out if 0, can be anywhere in between
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
            arrow.set_pos(Pos(arrow.pos.x, arrow.pos.y - arrow.speed * delta_time))
            
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
                # NOTE: This is terrible in terms big-O however the number 
                # of arrows on screen will never be too big to cause trouble
                arrows.remove(arrow)

        pygame.display.flip()

    pygame.quit()

