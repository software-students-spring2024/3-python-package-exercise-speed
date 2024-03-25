from .constants import *
from .image_functions import *

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

            return 0
            
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