from pygame.math import Vector2
import config
import pygame
from boundary import check_boundary

GREEN = config.get_color('GREEN')
RED = config.get_color('RED')
BLACK = config.get_color('BLACK')


def create_rocket(pos_x, pos_y, vel_x, vel_y):
    rocket_obj = {
        'pos': Vector2(pos_x, pos_y),
        'vel': Vector2(vel_x, vel_y),
        'propulsion': 0,
    }
    return rocket_obj

def update_rocket_position(rocket_obj, dt):
    rocket_obj['pos'] += rocket_obj['vel'] * dt
    rocket_obj['total_speed'] = rocket_obj['vel'].length()
    return rocket_obj


def handle_rocket_landing(rocket_obj, screen, message_to_screen):
    best_score = config.get('BEST_SCORE')
    y = rocket_obj['pos'][1] + 20
    x1, x2 = config.get('LANDING_PAD_X'), config.get(
        'LANDING_PAD_X') + config.get('LANDING_PAD_WIDTH')
    within_landing_pad = x1 <= rocket_obj['pos'][0] <= x2
    landing_speed = config.get('LANDING_ZONE_SPEED')

    if y >= config.get('LANDING_PAD_Y') and within_landing_pad and rocket_obj['vel'][0] < landing_speed:
        # Player wins
        pygame.draw.rect(screen, GREEN, (400, 560, 200, 30))
        message_to_screen("You won!", config.get_color(
            'BLACK'), 400, 560, 200, 30, screen)
        if rocket_obj['vel'][0] > best_score:
            config.update('BEST_SCORE', rocket_obj['vel'][0])
        message_to_screen("Best Score: " + str(config.get('BEST_SCORE')),
                          BLACK, 400, 600, 200, 30, screen)
    else:
        # Player loses
        pygame.draw.rect(screen, RED, (90, 560, 200, 30))
        message_to_screen("You lost!", BLACK, 90, 560, 200, 30, screen)

    check_boundary(rocket_obj, screen, message_to_screen)