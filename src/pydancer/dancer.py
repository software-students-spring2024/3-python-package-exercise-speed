from os import environ
import pygame
from .constants import *
from .image_functions import *
from .component import *
from .images import *
import random
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

def play(difficulty="easy", character="girl", song="test"):
    # TO DO: add theme
    initialize_pygame()
    font = pygame.font.SysFont(None, 36)

    # variable to keep track of player's score
    score = 0

    # Pygame setup
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_NAME)
    clock = pygame.time.Clock()
    # last_event_time = pygame.time.get_ticks()

    load_music(song)
    keys_level, speed_level = set_difficulty(difficulty)
    dancer, end_area = setup_components(character)

    arrows = []

    # Set a timer to add an arrow to the screen every x milliseconds
    ADD_ARROW = pygame.USEREVENT 
    milliseconds = 1406
    pygame.time.set_timer(ADD_ARROW, milliseconds)

    # Game Loop
    running = True
    while running:
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    # NOTE: You can check if an arrow is in the target area with
                    # arrow.percent_inside_of(end_area)
                    # it's fully inside if 100, it's out if 0, can be anywhere in between
                    for arrow in arrows:
                        # if the corresponding arrow is fully inside the target area, replace image with glowing
                        # TODO: if not, play fail sound and make the animation glitch
                        if arrow.percent_inside_of(end_area) == 100:
                            if ((arrow.direction == Direction.LEFT and event.key == pygame.K_LEFT)
                                or (arrow.direction == Direction.RIGHT and event.key == pygame.K_RIGHT)
                                or (arrow.direction == Direction.UP and event.key == pygame.K_UP)
                                or (arrow.direction == Direction.DOWN and event.key == pygame.K_DOWN)):
                                arrow.set_arrow_status(Status.GLOWING)
                                # 10 points if the arrow is inside the collision area
                                score += 10
                        elif arrow.percent_inside_of(end_area) > 0 and arrow.percent_inside_of(end_area) < 100:
                            if ((arrow.direction == Direction.LEFT and event.key == pygame.K_LEFT)
                                or (arrow.direction == Direction.RIGHT and event.key == pygame.K_RIGHT)
                                or (arrow.direction == Direction.UP and event.key == pygame.K_UP)
                                or (arrow.direction == Direction.DOWN and event.key == pygame.K_DOWN)):
                                arrow.set_arrow_status(Status.GLOWING)
                                # Calculate partial score for partial collision
                                score += round(arrow.percent_inside_of(end_area) / 10)

            if event.type == ADD_ARROW:
                # Randomly select the number of arrows to generate based on difficulty level
                num_arrows = random.randint(1, keys_level)
                for _ in range(num_arrows):
                    # Randomly select the direction for each arrow
                    direction = random.choice([Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT])
                    arrows.append(generate_arrow(direction, speed_level))

        # check if music finished playing
        if not pygame.mixer.music.get_busy():
            running = False

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

        display_score(score, font, screen)

        for arrow in arrows:
            # grey_out arrows that are above the end area
            if arrow.is_above(end_area) and arrow.status != Status.GLOWING:
                arrow.set_arrow_status(Status.OUTLINE)
            # remove arrows that go out of the screen
            if arrow.pos.y < -arrow.image.get_height():
                # NOTE: This is terrible in terms big-O however the number 
                # of arrows on screen will never be too big to cause trouble
                arrows.remove(arrow)

        pygame.display.flip()

    stop_music()
    display_final_score(score, font, screen, character)
    pygame.quit()


def initialize_pygame():
    '''
    Function to initialize pygame
    '''
    pygame.init()
    pygame.font.init()

def load_music(song):
    '''
    Function to load background music
    '''
    # TO-DO: add more songs
    # TO-DO: Change milliseconds variable based on song to sync with the beat
    # TO-DO: possibly load song from a database/JSON file that has millseconds info etc
    if song == "animals":
        pygame.mixer.music.load("../static/song_data/Animals.mp3")
    else:
        pygame.mixer.music.load("../static/song_data/test.mp3")
    pygame.mixer.music.play(1) # Play the music once

def set_difficulty(difficulty):
    '''
    Function to select number of max keys that can be pressed at once
    and speed of keys based on difficulty level
    '''
    if difficulty == "easy":
        keys_level = 2
        speed_level = 1
    elif difficulty == "medium":
        keys_level = 3
        speed_level = 1.3
    elif difficulty == "hard":
        keys_level = 4
        speed_level = 1.6
    return keys_level, speed_level

def set_character_image(character):
    '''
    Function to output image for dancer based on the selected character
    '''
    if character == "girl":
        dancer_image = dancer_image_girl
    else:
        dancer_image = dancer_image_boy
    return dancer_image

def setup_components(character):
    '''
    Function to set up dancer and collision area components
    '''
    dancer_image = set_character_image(character)
    dancer = Component(dancer_image, Pos(SCREEN_WIDTH * .5 , SCREEN_HEIGHT * .1))
    end_area = Component(end_area_image, Pos(SCREEN_WIDTH * .5, SCREEN_HEIGHT * .3))
    return dancer, end_area

def stop_music():
    '''
    Function to stop background music when quitting the game
    '''
    pygame.mixer.music.stop()

def display_score(score, font, screen):
    '''
    Function to display current score
    Score is displayed in the top right corner of the screen
    '''
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - 10, 10))

def display_final_score(score, font, screen, character):
    '''
    Function to display final score when game ends
    '''
    screen.fill(BACKGROUND_COLOR)
    # display dancer
    dancer_image = set_character_image(character)
    dancer = Component(dancer_image, Pos(SCREEN_WIDTH * .5 , SCREEN_HEIGHT * .3))
    dancer.display(screen)
    # display score
    final_score_text = font.render("Final Score: " + str(score), True, (0, 0, 0))
    screen.blit(final_score_text, ((SCREEN_WIDTH - final_score_text.get_width()) // 2, (SCREEN_HEIGHT - final_score_text.get_height()) // 2))
    pygame.display.flip()
    pygame.time.wait(5000)
