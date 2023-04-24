import pygame
import config

def message_to_screen(msg, color, x, y, width, height, screen):
    font = pygame.font.Font(None, config.get('FONT_SIZE'))
    text_surface = font.render(msg, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = ((x) + (width / 2), (y) + (height / 2))
    screen.blit(text_surface, text_rect)

def draw_rect(color, x, y, width, height, screen):
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, rect)

def reset_button(x, y, screen, reset_func):
    draw_rect(config.get_color('WHITE'), x, y, 80, 30, screen)
    message_to_screen("Reset", config.get_color(
        'BLACK'), x, y, 80, 30, screen)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x < mouse[0] < x + 80 and y < mouse[1] < y + 30:
        if click[0] == 1:
            reset_func()

def display_current_speed(velocity, x, y, screen):
    message_to_screen("Current speed: {:.2f}".format(
        velocity), config.get_color('WHITE'), x, y, 150, 30, screen)

def display_target_speed(target_speed, x, y, screen):
    message_to_screen("Target speed: {:.2f}".format(
        target_speed), config.get_color('WHITE'), x, y, 150, 30, screen)