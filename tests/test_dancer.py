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

    def test_play(self):
        pygame.init()
        try:
            play()
        except Exception as e:
            assert False, f"Error occurred while running the game loop: {e}"
        pygame.quit() 

    def test_initialize_pygame(self):
        initialize_pygame()
        assert (
            pygame.get_init() == True
        ), f"Expected initialize_pygame to return True but returned False."

    # def test_load_music(self):
    #     pygame.init()
    #     load_music("test")
    #     is_playing = pygame.mixer.music.get_busy()
    #     assert (is_playing == True), "Expected test.mp3 to be playing"

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
        dancer, end_area = setup_components("girl")
        assert (isinstance(dancer, Component)), f"Expected 'dancer' to be of instance Component."
        assert (isinstance(end_area, Component)), f"Expected 'end_area' to be of instance Component."

        # Check the image data of the components
        assert (dancer.image == dancer_image_girl), f"Expected dancer.image == dancer_image_girl"
        assert (end_area.image == end_area_image), f"Expected end_area.image == end_area_image"

        # Check the position of the components
        assert(dancer.pos.x == SCREEN_WIDTH * .5), f"Expected dancer.pos.x == SCREEN_WIDTH * .5"
        assert(dancer.pos.y == SCREEN_HEIGHT * .1), f"Expected dancer.pos.y == SCREEN_HEIGHT * .1"
        assert(end_area.pos.x == SCREEN_WIDTH * .5), f"Expected end_area.pos.x == SCREEN_WIDTH * .5"
        assert(end_area.pos.y == SCREEN_HEIGHT * .3), f"Expected end_area.pos.y == SCREEN_HEIGHT * .3"

        dancer, end_area = setup_components("boy")
        assert (isinstance(dancer, Component)), f"Expected 'dancer' to be of instance Component."
        assert (isinstance(end_area, Component)), f"Expected 'end_area' to be of instance Component."

        # Check the image data of the components
        assert (dancer.image == dancer_image_boy), f"Expected dancer.image == dancer_image_boy"
        assert (end_area.image == end_area_image), f"Expected end_area.image == end_area_image"

        # Check the position of the components
        assert(dancer.pos.x == SCREEN_WIDTH * .5), f"Expected dancer.pos.x == SCREEN_WIDTH * .5"
        assert(dancer.pos.y == SCREEN_HEIGHT * .1), f"Expected dancer.pos.y == SCREEN_HEIGHT * .1"
        assert(end_area.pos.x == SCREEN_WIDTH * .5), f"Expected end_area.pos.x == SCREEN_WIDTH * .5"
        assert(end_area.pos.y == SCREEN_HEIGHT * .3), f"Expected end_area.pos.y == SCREEN_HEIGHT * .3"

    def test_check_collision(self):
        pass
        '''
        arrows = []
        end_area = Component(end_area_image, Pos(SCREEN_WIDTH * .5, SCREEN_HEIGHT * .3))

        arrows.append(generate_arrow(Direction.UP, 1))
        arrows.append(generate_arrow(Direction.DOWN, 1))
        arrows.append(generate_arrow(Direction.LEFT, 1))
        arrows.append(generate_arrow(Direction.RIGHT, 1))

        event_keys = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]

        for event in event_keys:
            # Test full collision
            score = 0
            event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_UP})
            new_score = check_collision(arrows, end_area, event, score)
            assert new_score == 10

            # Test partial collision
            arrows[0].pos = Pos(100, 100)  # Move arrow to a position partially inside the end area
            event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_UP})
            new_score = check_collision(arrows, end_area, event, score)
            assert new_score > 0 and new_score < 10  # Partial score should be between 0 and 10
        '''

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
        clock = pygame.time.Clock()
        delta_time = clock.tick(FPS)/1000

        arrows = []
        keys_level = 3 
        speed_level = 1.3
        generate_arrows(arrows, keys_level, speed_level)

        for arrow in arrows:
            init_x = arrow.pos.x
            init_y = arrow.pos.y
            arrow.set_pos(Pos(init_x, init_y - arrow.speed * delta_time))

            assert (arrow.pos.x == init_x), "x position of arrow not in the intended position"
            assert (arrow.pos.y == init_y - arrow.speed * delta_time), "y position of arrow not in the intended position"

    # def test_music_is_playing(self):
    #     is_music_playing = music_is_playing()
    #     should = pygame.mixer.music.get_busy()
    #     assert is_music_playing == should, f"music should be {should}, whereas actual is {is_music_playing}"

    # def test_stop_music(self):
        # pygame.mixer.init()
        # pygame.mixer.music.load("../static/music/test.mp3")
        # pygame.mixer.music.play(1) # Play the music once
        # stop_music()
        # assert not pygame.mixer.music.get_busy(), "music still playing"

    def test_render_screen(self):
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        dancer = Component(dancer_image_girl, Pos(SCREEN_WIDTH * .5 , SCREEN_HEIGHT * .1))
        end_area = Component(end_area_image, Pos(SCREEN_WIDTH * .5, SCREEN_HEIGHT * .3))
        render_screen(screen, end_area, dancer, [generate_arrow(Direction.UP, 4)])

        # Check if the dancer is visible on the screen
        dancer_rect = pygame.Rect(dancer.pos.x, dancer.pos.y, dancer.image.get_width(), dancer.image.get_height())
        assert screen.get_rect().colliderect(dancer_rect), "Dancer is not on the screen"

        # Check if the end area is visible on the screen
        end_area_rect = pygame.Rect(end_area.pos.x, end_area.pos.y, end_area.image.get_width(), end_area.image.get_height())
        assert screen.get_rect().colliderect(end_area_rect), "End area is not on the screen"


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
