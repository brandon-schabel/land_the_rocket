from rocket import create_rocket, update_rocket_position, handle_rocket_landing
import display_objects
import physics_engine
import config_menu
import config
from pygame.math import Vector2
import pygame
from random import randint

# global reset
def reset_game():
    global rocket_obj
    rocket_obj = create_rocket(randint(100, config.get('WIDTH') - 100), 50, 0, 0)


rocket_obj = None
reset_game()  # initialize rocket_obj


BLACK = config.get_color('BLACK')
WHITE = config.get_color('WHITE')
GREEN = config.get_color('GREEN')
RED = config.get_color('RED')
TITLE = '2D Rocket Simulator'

pygame.init()
pygame.font.init()
pygame.display.set_caption(TITLE)
SIZE = (config.get('WIDTH'), config.get('HEIGHT'))
screen = pygame.display.set_mode(SIZE)

config.update('BEST_SCORE', 0)

done = False
dt = 0.1
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        config_menu.handle_config_events(event)

    keys = pygame.key.get_pressed()
    physics_engine.sim(keys, rocket_obj, dt, screen,
                       display_objects.message_to_screen)


    rocket_obj = update_rocket_position(rocket_obj, dt)
    handle_rocket_landing(rocket_obj, screen,
                          display_objects.message_to_screen)

    # Clear screen
    screen.fill(config.get_color('BLACK'))

    # Draw landing pad
    display_objects.draw_rect(config.get_color('WHITE'), config.get(
        'LANDING_PAD_X'), config.get('LANDING_PAD_Y'), config.get('LANDING_PAD_WIDTH'), config.get('LANDING_PAD_HEIGHT'), screen)

    # Draw rocket
    pygame.draw.circle(screen, config.get_color('WHITE'),
                       (int(rocket_obj['pos'][0]), int(rocket_obj['pos'][1])), 10)

    # Draw current speed and target speed
    display_objects.display_current_speed(
        rocket_obj['total_speed'], 10, 10, screen)
    display_objects.display_target_speed(
        config.get('LANDING_ZONE_SPEED'), 10, 40, screen)

    # Draw reset button
    display_objects.reset_button(
        config.get('WIDTH') - 100, config.get('HEIGHT') - 50, screen, reset_game)

    # Update screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()