import pygame
import config

config_items = [
    {'name': 'Gravity', 'config_key': 'GRAVITY', 'min': 0, 'max': 2},
    {'name': 'Acceleration', 'config_key': 'ACC', 'min': 0, 'max': 5},
    {'name': 'Friction', 'config_key': 'FRICTION', 'min': -1, 'max': 0},
    {'name': 'Propulsion', 'config_key': 'PROPULSION', 'min': 0, 'max': 1},
    {'name': 'Landing Zone Speed', 'config_key': 'LANDING_ZONE_SPEED', 'min': 1, 'max': 20},
    {'name': 'Propulsion Time', 'config_key': 'PROPULSION_TIME', 'min': 0, 'max': 5},
    {'name': 'Propulsion Max', 'config_key': 'PROPULSION_MAX', 'min': 0, 'max': 1},
    {'name': 'Air Resistance', 'config_key': 'AIR_RESISTANCE', 'min': 0, 'max': 1},
]

def draw_config_menu(screen):
    menu_font = pygame.font.Font(None, config.get('FONT_SIZE'))
    menu_color = config.get_color('WHITE')

    for i, item in enumerate(config_items):
        config_value = config.get(item['config_key'])
        menu_text = f"{item['name']}: {config_value:.2f}"
        menu_surface = menu_font.render(menu_text, True, menu_color)
        screen.blit(menu_surface, (10, 100 + i * 30))

def handle_config_events(event):
    for item in config_items:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                new_value = config.get(item['config_key']) + 0.1
                if new_value <= item['max']:
                    config.update(item['config_key'], new_value)
            elif event.key == pygame.K_DOWN:
                new_value = config.get(item['config_key']) - 0.1
                if new_value >= item['min']:
                    config.update(item['config_key'], new_value)
