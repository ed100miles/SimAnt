import pygame
from PIL import Image
from classes.ant_class import Ant

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

# Imgs: 
ant_size = 0.01
ant_img = Image.open('imgs/ant.png')
orig_ant_height, orig_ant_width = ant_img.size
ant_img = ant_img.resize((round(orig_ant_width*ant_size), 
                round(orig_ant_width*ant_size)))
ant_img.save('imgs/small_ant.png')

# Game settings:
game_over = False
game_display = pygame.display.set_mode((game_display_width, game_display_height))
pygame.display.set_caption(game_title)
clock = pygame.time.Clock()


# Ant 
# class Ant:
#     def __init__(self):
#         self.ant_img = pygame.image.load('imgs/small_ant.png')
#         self.ant_x = game_display_height * 0.5
#         self.ant_y = game_display_width * 0.5
#         self.ant_up = False
#         self.ant_down = False
#         self.ant_left = False
#         self.ant_right = False

#     def ant_event(self, event):
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_w:
#                 self.ant_up = True
#                 self.ant_down = False
#             if event.key == pygame.K_s:
#                 self.ant_down = True
#                 self.ant_up = False
#             if event.key == pygame.K_a:
#                 self.ant_left = True
#                 self.ant_right = False
#             if event.key == pygame.K_d:
#                 self.ant_right = True
#                 self.ant_left = False
        
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_w:
#                 self.ant_up = False
#             if event.key == pygame.K_s:
#                 self.ant_down = False
#             if event.key == pygame.K_a:
#                 self.ant_left = False
#             if event.key == pygame.K_d:
#                 self.ant_right = False
#         return

#     def ant_move(self):
#         if self.ant_up:
#             self.ant_y -= 1
#         if self.ant_down:
#             self.ant_y += 1
#         if self.ant_left:
#             self.ant_x -= 1
#         if self.ant_right:
#             self.ant_x += 1
#         return
    
#     def ant_draw(self):
#         game_display.blit(self.ant_img,(self.ant_x, self.ant_y))


player_ant = Ant()

# Game loop:
while not game_over:

    for event in pygame.event.get():

        player_ant.ant_move()
        
        if event.type == pygame.QUIT:
            game_over = True
        # print(event)

        if event:
            player_ant.ant_event(event)

        game_display.fill(grass)
        player_ant.ant_draw()

        pygame.display.update()

        clock.tick(60)

pygame.quit()
quit()



