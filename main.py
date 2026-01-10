import pygame
import game.config as config
import game.char as char

pygame.init()

screen = pygame.display.set_mode(config.display.size)
pygame.display.set_caption('avoid the pacman')
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    char.player.player_move(char.player.player, keys)

    clock.tick(config.display.fps)

    screen.fill(config.color.BLACK)
    pygame.draw.rect(screen, config.color.WHITE, char.player.player)

    pygame.display.flip()

pygame.quit()