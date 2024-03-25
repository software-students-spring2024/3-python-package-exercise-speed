from os import environ
import pygame
from .constants import *
from .image_functions import *
from .arrows import *
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'


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

