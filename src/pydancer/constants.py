from enum import Enum

GAME_NAME = "PyDancer"
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
DANCER_WIDTH, DANCER_HEIGHT = 128, 128
ARROW_WIDTH, ARROW_HEIGHT = 64, 64
BACKGROUND_COLOR = (250, 250, 250)
FPS = 60 # frames per second

class Direction(Enum):
    RIGHT = "right"
    LEFT = "left"
    UP = "up"
    DOWN = "down"
    NONE = "none"
