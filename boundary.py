import pygame
import config

BLACK = config.get_color('BLACK')
GREEN = config.get_color('GREEN')
RED = config.get_color('RED')

landing_speed = config.get('LANDING_ZONE_SPEED', 5)

def check_boundary(rocket_obj, screen, message_to_screen):
    x, y = rocket_obj['pos']
    width, height = config.get('WIDTH'), config.get('HEIGHT')

    if x > width:
        rocket_obj['pos'] = (0, y)
    elif x < 0:
        rocket_obj['pos'] = (width, y)

    if y > height:
        rocket_obj['pos'] = (x, 0)
        if rocket_obj['total_speed'] > landing_speed:
            pygame.draw.rect(screen, RED, (90, 560, 200, 30))
            message_to_screen("You lost!", BLACK, 90, 560, 200, 30, screen)
        else:
            pygame.draw.rect(screen, GREEN, (400, 560, 200, 30))
            message_to_screen("You won!", BLACK, 400, 560, 200, 30, screen)
            rocket_obj['pos'] = (width / 2, 0)
            rocket_obj['vel'] = [0, 0]
            pygame.draw.rect(screen, GREEN, (400, 500, 200, 20))
    elif y < 0:
        rocket_obj['pos'] = (x, height)