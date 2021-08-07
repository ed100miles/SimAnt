import pygame
from PIL import Image
from classes.ant_class import Ant, EnemyAnt, Food

pygame.init()

# Display settings:
game_display_width = 1000
game_display_height = 800
game_title = 'My Game'

# Color definitions:
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grass = (0, 204, 0)

# Game settings:
game_over = False
game_display = pygame.display.set_mode((game_display_width, game_display_height))
pygame.display.set_caption(game_title)
clock = pygame.time.Clock()


# Create object instances:
player_ant = Ant(game_display_height, game_display_width, game_display)
enemy_ant = EnemyAnt(game_display_height, game_display_width, game_display)
food = Food(game_display_height, game_display_width, game_display)

# Game loop:
while not game_over:
    for event in pygame.event.get():
        player_ant.ant_move()
        if event.type == pygame.QUIT:
            game_over = True
        if event:
            player_ant.ant_event(event)
        
        # Draw frame:
        game_display.fill(grass)
        enemy_ant.direction_decision(player_ant)
        # player_ant.orientate()
        food.draw()
        player_ant.draw()
        enemy_ant.draw(player_ant)
        pygame.display.update()

        clock.tick(30)

pygame.quit()
quit()

