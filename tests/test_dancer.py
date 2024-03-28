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
    #         play(run_game=False)
    #     except Exception as e:
    #         assert False, f"Error occurred while running the game loop: {e}"
    #     pygame.quit() 

    def test_initialize_pygame(self):
        initialize_pygame()
        assert (
            pygame.get_init() == True
        ), f"Expected initialize_pygame to return True but returned False."

    # def test_load_music(self):
    #     load_music("test")
    #     assert pygame.mixer.music.get_busy() == True

    def test_set_difficulty(self):
        keys_level, speed_level = set_difficulty("easy")
        assert (
            keys_level == 2 and speed_level == 1
        ), f"Expected set_difficulty('easy') to return keys_level = 2 and speed_level = 1. Instead, it returned keys_level = '{keys_level}' and speed_level = '{speed_level}'."
        keys_level, speed_level = set_difficulty("medium")

        assert (
            keys_level == 3 and speed_level == 1.3
        ), f"Expected set_difficulty('medium') to return keys_level = 3 and speed_level = 1.3. Instead, it returned keys_level = '{keys_level}' and speed_level = '{speed_level}'."

        keys_level, speed_level = set_difficulty("hard")
        assert (
            keys_level == 4 and speed_level == 1.6
        ), f"Expected set_difficulty('hard') to return keys_level = 4 and speed_level = 1.6. Instead, it returned keys_level = '{keys_level}' and speed_level = '{speed_level}'."


    def test_set_character_image(self):
        image = set_character_image("girl")
        assert (
            image == dancer_image_girl
        ), f"Expected image to be dancer_image_girl. Instead, it returned '{image}'."
        image = set_character_image("boy")
        assert (
            image == dancer_image_boy
        ), f"Expected image to be dancer_image_boy. Instead, it returned '{image}'."

    def test_setup_components(self):
        pass

    def test_check_collision(self):
        pass

    def test_generate_arrows(self):
        arrows = []
        keys_level = 3 
        speed_level = 1.3
        generate_arrows(arrows, keys_level, speed_level)
        
        assert (
            len(arrows) <= keys_level
        ), f"Expected len(arrows) <= keys_level. Instead, len(arrows) > keys_level."
        assert (
            len(arrows) >= 1
        ), f"Expected len(arrows) >= 1. Instead, len(arrows) < 1."

        # Check if each arrow in the list has a valid direction and speed
        for arrow in arrows:
            assert (
                arrow.direction in [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]
            ), f"Invalid direction detected: {arrow.direction}."
            '''
            assert (
                arrow.speed == speed_level
            ), f"Expected speed level: {speed_level}. Instead, speed level detected detected {arrow.speed}."
            '''
            
    def test_update_arrows(self):
        pass

    def test_music_is_playing(self):
        pass

    def test_stop_music(self):
        pass

    def test_render_screen(self):
        pass

    def test_display_score(self):
        font = pygame.font.SysFont(None, 36)
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        display_score(782, font, screen)
        final_score_text = font.render("Final Score: 782", True, (0, 0, 0))
        # put on screen
        screen.blit(final_score_text, ((SCREEN_WIDTH - final_score_text.get_width()) // 2, (SCREEN_HEIGHT - final_score_text.get_height()) // 2))
        pygame.display.flip()
        # check if text is on screen
        screen_surface = pygame.display.get_surface()
        text_rect = final_score_text.get_rect(center=screen_surface.get_rect().center)
        assert screen_surface.get_rect().colliderect(text_rect), "Final score text not on screen"

    def test_display_final_score(self):
        font = pygame.font.SysFont(None, 36)
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        display_final_score(782, font, screen, "girl")
        final_score_text = font.render("Final Score: 782", True, (0, 0, 0))
        # put on screen
        screen.blit(final_score_text, ((SCREEN_WIDTH - final_score_text.get_width()) // 2, (SCREEN_HEIGHT - final_score_text.get_height()) // 2))
        pygame.display.flip()
        # check if text is on screen
        screen_surface = pygame.display.get_surface()
        text_rect = final_score_text.get_rect(center=screen_surface.get_rect().center)
        assert screen_surface.get_rect().colliderect(text_rect), "Final score text not on screen"
