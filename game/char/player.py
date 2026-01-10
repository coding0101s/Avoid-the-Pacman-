import pygame
from ..config import display
from .funcs.player_func import speed, player_move_input, player_move, player_bounce_on_wall

pygame.init()

orign_size = (50, 60)
orign_width = orign_size[0]
orign_height = orign_size[1]

orign_pos = (display.width // 2 - orign_width // 2, display.height // 2 - orign_height // 2)
orign_x = orign_pos[0]
orign_y = orign_pos[1]

player = pygame.Rect(orign_x, orign_y, orign_width, orign_height)