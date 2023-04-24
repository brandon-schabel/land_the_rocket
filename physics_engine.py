import pygame
import config
import math
from boundary import check_boundary

BLACK = config.get_color('BLACK')
WHITE = config.get_color('WHITE')
GREEN = config.get_color('GREEN')
RED = config.get_color('RED')


def update_pos(rocket_obj, dt):
    rocket_obj['pos'] = (rocket_obj['pos'][0] + rocket_obj['vel']
                         [0] * dt, rocket_obj['pos'][1] + rocket_obj['vel'][1] * dt)


def update_vel(keys, rocket_obj, dt):
    max_propulsion = config.get('PROPULSION_MAX', 0.5)
    landing_speed = config.get('LANDING_ZONE_SPEED', 5)

    # Update propulsion and velocity based on user input
    if keys[pygame.K_UP]:
        rocket_obj['propulsion'] = min(rocket_obj['propulsion'] + config.get('PROPULSION_INC', 0), max_propulsion)
        rocket_obj['vel'][1] -= config.get('ACC') * rocket_obj['propulsion']
    else:
        rocket_obj['propulsion'] = max(rocket_obj['propulsion'] - config.get('PROPULSION_DEC'), 0.1) # Add minimum propulsion value

    # Limit rocket's horizontal speed
    if keys[pygame.K_RIGHT] and rocket_obj['vel'][0] < landing_speed:
        rocket_obj['vel'][0] += config.get('ACC') * dt
    if keys[pygame.K_LEFT] and rocket_obj['vel'][0] > -landing_speed:
        rocket_obj['vel'][0] -= config.get('ACC') * dt

    # Update velocity due to friction, gravity, and air resistance
    rocket_obj['vel'][0] += rocket_obj['vel'][0] * config.get('FRICTION')
    rocket_obj['vel'][1] += config.get('GRAVITY') * dt - \
        config.get('AIR_RESISTANCE') * rocket_obj['vel'][1] ** 2 * dt
    rocket_obj['total_speed'] = math.sqrt(
        rocket_obj['vel'][0] ** 2 + rocket_obj['vel'][1] ** 2)

    # Cap maximum upward velocity
    if rocket_obj['vel'][1] > 30:
        rocket_obj['vel'][1] = 30

    # Set minimum altitude to ground level
    if rocket_obj['pos'][1] < 0:
        rocket_obj['pos'][1] = 0
        rocket_obj['vel'][1] = 0
        
    
def sim(keys, rocket_obj, dt, screen, message_to_screen):
    update_vel(keys, rocket_obj, dt)
    update_pos(rocket_obj, dt)

    y = rocket_obj['pos'][1] + 20
    x1, x2 = config.get('LANDING_PAD_X'), config.get(
        'LANDING_PAD_X') + config.get('LANDING_PAD_WIDTH')
    within_landing_pad = x1 <= rocket_obj['pos'][0] <= x2
    landing_speed = config.get('LANDING_ZONE_SPEED')
    best_score = config.get('BEST_SCORE')

    if y >= config.get('LANDING_PAD_Y') and within_landing_pad and rocket_obj['vel'][0] < landing_speed:
        # Player wins
        pygame.draw.rect(screen, GREEN, (400, 560, 200, 30))
        message_to_screen("You won!", config.get_color(
            'BLACK'), 400, 560, 200, 30, screen)
        if rocket_obj['vel'][0] > best_score:
            config.update('BEST_SCORE', rocket_obj['vel'][0])
        message_to_screen("Best Score: " + str(config.get('BEST_SCORE')),
                          config.get_color('BLACK'), 400, 600, 200, 30, screen)
    else:
        # Player loses
        pygame.draw.rect(screen, RED, (90, 560, 200, 30))
        message_to_screen("You lost!", config.get_color(
            'BLACK'), 90, 560, 200, 30, screen)

    check_boundary(rocket_obj, screen, message_to_screen)
