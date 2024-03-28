from src.pydancer.images import *
from src.pydancer.constants import *
import pygame

class Tests:
    def test_load_image(self):
        # Test loading dancer images
        assert (
            isinstance(dancer_image_girl, pygame.Surface)
        ), f"dancer_image_girl is not an instance of pygame.Surface"
        assert (
            isinstance(dancer_image_boy, pygame.Surface)
        ), f"dancer_image_boy is not an instance of pygame.Surface"

        # Test loading end area image
        assert (
            isinstance(end_area_image, pygame.Surface)
        ), f"end_area_image is not an instance of pygame.Surface"

    def test_scale_image(self):
        # Test scaling of dancer images
        girl_width = dancer_image_girl.get_width()
        assert (
            girl_width == DANCER_WIDTH
        ), f"Expected width of dancer_image_girl to be '{DANCER_WIDTH}'. Instead, width is '{girl_width}'."
        girl_height = dancer_image_girl.get_height()
        assert (
            girl_height == DANCER_HEIGHT
        ), f"Expected height of dancer_image_girl to be '{DANCER_HEIGHT}'. Instead, height is '{girl_height}'."

        boy_width = dancer_image_boy.get_width()
        assert (
            boy_width == DANCER_WIDTH
        ), f"Expected width of dancer_image_boy to be '{DANCER_WIDTH}'. Instead, width is '{boy_width}'."
        boy_height = dancer_image_boy.get_height()
        assert (
            boy_height == DANCER_HEIGHT
        ), f"Expected height of dancer_image_boy to be '{DANCER_HEIGHT}'. Instead, height is '{boy_height}'."

        # Test scaling of end area image
        end_area_width = end_area_image.get_width()
        assert (
            end_area_width == SCREEN_WIDTH
        ), f"Expected width of end_area_image to be '{SCREEN_WIDTH}'. Instead, width is '{end_area_width}'."
        end_area_height = end_area_image.get_height()
        assert (
            end_area_height == SCREEN_HEIGHT * 0.15
        ), f"Expected height of end_area_image to be '{SCREEN_HEIGHT * 0.15}'. Instead, height is '{end_area_height}'."
