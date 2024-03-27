import os
os.chdir("./src")
from src.pydancer.dancer import *
import pygame

class Tests:
    def test_sanity_check(self):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes
        From the main project directory, run the `python3 -m pytest` command to run all tests.
        """
        expected = True  # the value we expect to be present
        actual = True  # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"

    # def test_play(self):
    #     pygame.init()
    #     try:
    #         play()
    #     except Exception as e:
    #         assert False, f"Error occurred while running the game loop: {e}"
    #     pygame.quit() 

    def test_initialize_pygame(self):
        initialize_pygame()
        assert pygame.get_init() == True

    def test_load_music(self):
        load_music("test")
        assert pygame.mixer.music.get_busy() == True

    def test_set_difficulty(self):
        keys_level, speed_level = set_difficulty("easy")
        assert keys_level == 2 and speed_level == 1
        keys_level, speed_level = set_difficulty("medium")
        assert keys_level == 3 and speed_level == 1.3
        keys_level, speed_level = set_difficulty("hard")
        assert keys_level == 4 and speed_level == 1.6

    def test_set_character_image(self):
        image = set_character_image("girl")
        assert image == dancer_image_girl
        image = set_character_image("boy")
        assert image == dancer_image_boy

    def test_setup_components(self):
        pass

    def test_check_collision(self):
        pass

    def test_generate_arrows(self):
        pass

    def test_update_arrows(self):
        pass

    def test_music_status(self):
        pass

    def test_stop_music(self):
        pass

    def test_render_screen(self):
        pass

    def test_display_score(self):
        pass

    def test_display_final_score(self):
        pass