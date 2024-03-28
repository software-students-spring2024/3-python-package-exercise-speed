from .constants import *
from .image_functions import *
from .component import *
from .images import *
import random
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame


def play(difficulty="easy", character="girl", song="test"):
    initialize_pygame()
    # TODO: add theme
    font = pygame.font.SysFont(None, 36)

    # variable to keep track of player's score
    score = 0

    # Pygame setup
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_NAME)
    clock = pygame.time.Clock()

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
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    score = check_collision(arrows, end_area, event, score)

            if event.type == ADD_ARROW:
                generate_arrows(arrows, keys_level, speed_level)

        # running = music_status()
        if not music_is_playing():
            stop_music()
            display_final_score(score, font, screen, character)
            pygame.quit()
            break

        # delta time is needed to make updates independent of the frame rate to arrows
        delta_time = clock.tick(FPS)/1000
        update_arrows(arrows, delta_time)

        render_screen(screen, end_area, dancer, arrows)
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
    # TO-DO: possibly load song from a database/JSON file that has milliseconds info etc
    pygame.mixer.music.load("../static/music/" + song + ".mp3")
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

def check_collision(arrows, end_area, event, score):
    '''
    Function to check if an arrow was pressed in the collision zone (partially or fully)
    Score is rewarded based off partial or full collision
    If collision occurs, the arrow glows
    '''
    new_score = score
    for arrow in arrows:
        if arrow.percent_inside_of(end_area) == 100: # full collision
            if ((arrow.direction == Direction.LEFT and event.key == pygame.K_LEFT)
                or (arrow.direction == Direction.RIGHT and event.key == pygame.K_RIGHT)
                or (arrow.direction == Direction.UP and event.key == pygame.K_UP)
                or (arrow.direction == Direction.DOWN and event.key == pygame.K_DOWN)):
                if arrow.status != Status.GLOWING:
                    arrow.set_arrow_status(Status.GLOWING)
                    # 10 points if the arrow is inside the collision area
                    new_score += 10
        elif arrow.percent_inside_of(end_area) > 0 and arrow.percent_inside_of(end_area) < 100: # partial collision
            if ((arrow.direction == Direction.LEFT and event.key == pygame.K_LEFT)
                or (arrow.direction == Direction.RIGHT and event.key == pygame.K_RIGHT)
                or (arrow.direction == Direction.UP and event.key == pygame.K_UP)
                or (arrow.direction == Direction.DOWN and event.key == pygame.K_DOWN)):
                if arrow.status != Status.GLOWING:
                    arrow.set_arrow_status(Status.GLOWING)
                    # Calculate partial score for partial collision
                    new_score += round(arrow.percent_inside_of(end_area) / 10)
    return new_score

def generate_arrows(arrows, keys_level, speed_level):
    '''
    Randomly generate arrows generate based on difficulty level
    '''
    num_arrows = random.randint(1, keys_level)
    for _ in range(num_arrows):
        # Randomly select the direction for each arrow
        direction = random.choice([Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT])
        arrows.append(generate_arrow(direction, speed_level))

def update_arrows(arrows, delta_time):
    '''
    Function to update arrow positions with time delta_time
    '''
    for arrow in arrows:
        arrow.set_pos(Pos(arrow.pos.x, arrow.pos.y - arrow.speed * delta_time))

def music_is_playing():
    '''
    Function to check if music finished playing
    '''
    if not pygame.mixer.music.get_busy():
        return False
    return True

def stop_music():
    '''
    Function to stop background music when quitting the game
    '''
    pygame.mixer.music.stop()

def render_screen(screen, end_area, dancer, arrows):
    '''
    Function to display the screen and all elements
    '''
    screen.fill(BACKGROUND_COLOR) # Draw screen

    # display components
    end_area.display(screen)
    dancer.display(screen)

    # display arrows
    for arrow in arrows:
        arrow.display(screen)

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
