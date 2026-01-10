import pygame
import game.config as config
import game.char as char

pygame.init()

screen = pygame.display.set_mode(config.display.size)
pygame.display.set_caption('Avoid the Pacman')
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()

    char.player.player_move_input(keys, config.player.dire, char.player.player, config.display.width, config.display.height)
    char.player.player_move(char.player.player, config.player.dire)
    

    clock.tick(config.display.fps)

    screen.fill(config.color.BLACK)
    pygame.draw.rect(screen, config.color.WHITE, char.player.player)

    pygame.display.flip()

pygame.quit()