import pygame

pygame.init()

speed = 5

def player_bounce_on_wall(player, dire: list, screen_width: int, screen_height: int):
    if player.left <= 0:
        dire[0] = 'right'
        return 0
    if player.right >= screen_width:
        dire[0] = 'left'
        return 0
    if player.top <= 0:
        dire[0] = 'down'
        return 0
    if player.bottom >= screen_height:
        dire[0] = 'up'
        return 0
    
    return 1

def player_move_input(keys, dire: list, player, screen_width: int, screen_height: int):
    if player_bounce_on_wall(player, dire, screen_width, screen_height) == 0:
        return

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        dire[0] = 'up'
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        dire[0] = 'down'
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        dire[0] = 'left'
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        dire[0] = 'right'

def player_move(player, dire: list):
    if dire[0] == 'up':
        player.y -= speed
    if dire[0] == 'down':
        player.y += speed
    if dire[0] == 'left':
        player.x -= speed
    if dire[0] == 'right':
        player.x += speed

