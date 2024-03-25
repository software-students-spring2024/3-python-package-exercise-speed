from os import environ
import pygame
from .constants import *
from .image_functions import *
from .component import *
from .images import *
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'


def play():
    pygame.init()

    # Pygame setup
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_NAME)
    clock = pygame.time.Clock()
    # last_event_time = pygame.time.get_ticks()

    # set up components 
    dancer = Component(dancer_image, Pos(SCREEN_WIDTH * .5 , SCREEN_HEIGHT * .1))
    end_area = Component(end_area_image, Pos(SCREEN_WIDTH * .5, SCREEN_HEIGHT * .3))

    arrows = [generate_arrow(Direction.UP), generate_arrow(Direction.DOWN), generate_arrow(Direction.LEFT), generate_arrow(Direction.RIGHT)]

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
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    # NOTE: You can check if an arrow is in the target area with
                    # arrow.percent_inside_of(end_area)
                    # it's fully inside if 100, it's out if 0, can be anywhere in between
                    for arrow in arrows:
                        # if the corresponding arrow is fully inside the target area, replace image with glowing
                        # TODO: if not, play fail sound and make the animation glitch
                        if arrow.percent_inside_of(end_area) == 100:
                            if arrow.direction == Direction.LEFT and event.key == pygame.K_LEFT:
                                arrow.image = left_glow_arrow_image
                            elif arrow.direction == Direction.RIGHT and event.key == pygame.K_RIGHT:
                                arrow.image = right_glow_arrow_image
                            elif arrow.direction == Direction.UP and event.key == pygame.K_UP:
                                arrow.image = up_glow_arrow_image
                            elif arrow.direction == Direction.DOWN and event.key == pygame.K_DOWN:
                                arrow.image = down_glow_arrow_image


            if event.type == ADD_ARROW:
                arrows.append(generate_arrow(Direction.UP))
                arrows.append(generate_arrow(Direction.DOWN))
                arrows.append(generate_arrow(Direction.LEFT))
                arrows.append(generate_arrow(Direction.RIGHT))

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

