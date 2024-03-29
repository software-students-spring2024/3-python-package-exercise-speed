import os
os.chdir("./src")
from src.pydancer.dancer import *
import pygame
from unittest.mock import patch

class Tests:
    def test_sanity_check(self):
        expected = True  # the value we expect to be present
        actual = True  # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"

    def test_play(self):
        pass
    #     pygame.init()
    #     try:
    #         play(run_game=False)
    #     except Exception as e:
    #         assert False, f"Error occurred while running the game loop: {e}"
    #     pygame.quit() 

    def test_initialize_pygame(self):
        initialize_pygame()
        assert (pygame.get_init() == True), f"Expected initialize_pygame to return True but returned False."

    def test_load_music(self):
        pass
        # with patch('pygame.mixer.music') as mixer:
        #     #mixer.get_busy.return_value = True  # Simulate music playing
        #     load_music("test")
        #     mixer.load.assert_called_once_with("../static/music/test.mp3")
        #     mixer.play.assert_called_once()
        #     assert (mixer.get_busy() == True)

    def test_set_difficulty(self):
        keys_level, speed_level = set_difficulty("easy")
        assert (keys_level == 2 and speed_level == 1), f"Expected set_difficulty('easy') to return keys_level = 2 and speed_level = 1. Instead, it returned keys_level = '{keys_level}' and speed_level = '{speed_level}'."
        keys_level, speed_level = set_difficulty("medium")

        assert (keys_level == 3 and speed_level == 1.3), f"Expected set_difficulty('medium') to return keys_level = 3 and speed_level = 1.3. Instead, it returned keys_level = '{keys_level}' and speed_level = '{speed_level}'."

        keys_level, speed_level = set_difficulty("hard")
        assert (keys_level == 4 and speed_level == 1.6), f"Expected set_difficulty('hard') to return keys_level = 4 and speed_level = 1.6. Instead, it returned keys_level = '{keys_level}' and speed_level = '{speed_level}'."

    def test_set_character_image(self):
        image = set_character_image("girl")
        assert (image == dancer_image_girl), f"Expected image to be dancer_image_girl. Instead, it returned '{image}'."
        image = set_character_image("boy")
        assert (image == dancer_image_boy), f"Expected image to be dancer_image_boy. Instead, it returned '{image}'."

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

        arrows = []
        arrow1 = generate_arrow(Direction.UP, 1)
        arrow1.set_pos(Pos(100, 200))

        arrow2 = generate_arrow(Direction.UP, 1)
        arrow2.set_pos(Pos(0, 0))

        arrows.append(arrow1)
        arrows.append(arrow2)

        end_area = Component(end_area_image, Pos(SCREEN_WIDTH * .5, SCREEN_HEIGHT * .3))
        event = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_UP})
        score = 0

        new_score = check_collision(arrows, end_area, event, score)
        assert (new_score > 0 and new_score < 10), f"Expected score > 0 and score < 10. Instead, returned score = '{new_score}'."

    def test_generate_arrows(self):
        arrows = []
        keys_level = 3 
        speed_level = 1.3
        generate_arrows(arrows, keys_level, speed_level)
        
        assert (len(arrows) <= keys_level), f"Expected len(arrows) <= keys_level. Instead, len(arrows) > keys_level."
        assert (len(arrows) >= 1), f"Expected len(arrows) >= 1. Instead, len(arrows) < 1."

        # Check if each arrow in the list has a valid direction and speed
        for arrow in arrows:
            assert (arrow.direction in [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]), f"Invalid direction detected: {arrow.direction}."
            
    def test_update_arrows_positions(self):
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

    def test_music_is_playing(self):
        with patch('pygame.mixer.music') as mixer:
            mixer.get_busy.return_value = True  # Simulate music playing
            assert (music_is_playing() == True), "Expected music_is_playing() == True, but returned False"

        with patch('pygame.mixer.music') as mixer:
            mixer.get_busy.return_value = False # Simulate music not playing
            assert music_is_playing() == False, "Expected music_is_playing() == False, but returned True"

    def test_stop_music(self):
        pass
        # with patch('pygame.mixer.music') as mixer:
        #     mixer.get_busy.return_value = True  # Simulate music playing
        #     stop_music()
        #     actual = mixer.get_busy()
        #     #mixer.stop.assert_called_once()
        #     assert (actual == False)

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

    def test_update_arrows(self):
        # Create arrows
        normal_arrow = []
        generate_arrows(normal_arrow, 1, 1)
        normal_arrow[0].set_pos(Pos(100,SCREEN_HEIGHT))

        grey_arrow = []
        generate_arrows(grey_arrow, 1, 1)
        grey_arrow[0].set_pos(Pos(200, 100))

        out_of_screen_arrow = []
        generate_arrows(out_of_screen_arrow, 1, 1)
        out_of_screen_arrow[0].set_pos(Pos(300,-100))
        
        # Set arrow statuses
        normal_arrow[0].set_arrow_status(Status.DEFAULT)
        grey_arrow[0].set_arrow_status(Status.DEFAULT)
        out_of_screen_arrow[0].set_arrow_status(Status.DEFAULT)
        
        # Create end area
        end_area = Component(end_area_image, Pos(SCREEN_WIDTH * .5, SCREEN_HEIGHT * .3))

        # List of arrows
        arrows = []
        arrows.append(normal_arrow[0])
        arrows.append(grey_arrow[0])
        arrows.append(out_of_screen_arrow[0])

        # Update arrows
        updated_arrows = update_arrows(arrows, 0.1, end_area)

        # Check statuses
        assert updated_arrows[0].status == Status.DEFAULT, "Normal arrow status changed"
        assert updated_arrows[1].status == Status.OUTLINE, "Grey arrow status not updated"
        assert out_of_screen_arrow[0] not in updated_arrows, "Out-of-screen arrow not removed"

        # Assertions
        assert len(updated_arrows) == 2, "Expected number of arrows to be 2 after update. Instead, returned 3"

    def test_setup_pygame(self):
        screen, clock, font = setup_pygame()

        assert isinstance(screen, pygame.Surface), "Screen is not an instance of pygame.Surface"
        assert isinstance(clock, pygame.time.Clock), "Clock is not an instance of pygame.time.Clock"
        assert isinstance(font, pygame.font.Font), "Font is not an instance of pygame.font.Font"
        assert screen.get_width() == SCREEN_WIDTH, f"Screen width is {screen.get_width()}, expected {SCREEN_WIDTH}."
        assert screen.get_height() == SCREEN_HEIGHT, f"Screen height is {screen.get_height()}, expected {SCREEN_HEIGHT}."
        assert pygame.display.get_caption()[0] == GAME_NAME, f"Game name is {pygame.display.get_caption()[0]}, expected {GAME_NAME}."
    
    def test_handle_keydown(self):
        arrows = []
        generate_arrows(arrows, 1, 1)
        arrows[0].set_pos(Pos(100,SCREEN_HEIGHT * .3))

        # Create mock event with a valid key
        # only one event should cause a collision (w score 10)
        # all others should have score 0
        mock_event1 = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_LEFT})
        mock_event2 = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_RIGHT})
        mock_event3 = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_UP})
        mock_event4 = pygame.event.Event(pygame.KEYDOWN, {'key': pygame.K_DOWN})

        end_area = Component(end_area_image, Pos(SCREEN_WIDTH * .5, SCREEN_HEIGHT * .3))

        score = 0

        score1 = handle_keydown(arrows, end_area, mock_event1, score)
        score2 = handle_keydown(arrows, end_area, mock_event2, score)
        score3 = handle_keydown(arrows, end_area, mock_event3, score)
        score4 = handle_keydown(arrows, end_area, mock_event4, score)

        score = score1 + score2 + score3 + score4

        assert (score == 10), f"Expected updated score to be 10 when a valid key is pressed. Instead, returned '{score}'."

    def test_game_loop(self):
        pass