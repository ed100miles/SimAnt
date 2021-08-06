import pygame
import random
pygame.init()

# Ant 
class Ant:
    def __init__(self, display_height, display_width, game_display):
        self.ant_img = pygame.image.load('imgs/small_ant.png')
        self.ant_x = display_height * 0.5
        self.ant_y = display_width * 0.5
        self.ant_up = False
        self.ant_down = False
        self.ant_left = False
        self.ant_right = False
        self.game_display = game_display

    def ant_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.ant_up = True
                self.ant_down = False
            if event.key == pygame.K_s:
                self.ant_down = True
                self.ant_up = False
            if event.key == pygame.K_a:
                self.ant_left = True
                self.ant_right = False
            if event.key == pygame.K_d:
                self.ant_right = True
                self.ant_left = False
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                self.ant_up = False
            if event.key == pygame.K_s:
                self.ant_down = False
            if event.key == pygame.K_a:
                self.ant_left = False
            if event.key == pygame.K_d:
                self.ant_right = False
        return

    def ant_move(self):
        if self.ant_up:
            self.ant_y -= 1
        if self.ant_down:
            self.ant_y += 1
        if self.ant_left:
            self.ant_x -= 1
        if self.ant_right:
            self.ant_x += 1
        return
    
    def orientate(self):
        if self.ant_up: #and not (self.ant_left or self.ant_right):
            self.ant_img = pygame.image.load('imgs/small_ant.png')
        if self.ant_right:
            self.ant_img = pygame.image.load('imgs/small_ant90.png')
        if self.ant_down:
            self.ant_img = pygame.image.load('imgs/small_ant180.png')
        if self.ant_left:
            self.ant_img = pygame.image.load('imgs/small_ant270.png')

        if self.ant_up and self.ant_right:
            self.ant_img = pygame.image.load('imgs/small_ant45.png')
        if self.ant_up and self.ant_left:
            self.ant_img = pygame.image.load('imgs/small_ant315.png')

        if self.ant_down and self.ant_left:
            self.ant_img = pygame.image.load('imgs/small_ant225.png')
        if self.ant_down and self.ant_right:
            self.ant_img = pygame.image.load('imgs/small_ant135.png')

    def draw(self):
        self.game_display.blit(self.ant_img,(self.ant_x, self.ant_y))

class Food:
    def __init__(self, display_height, display_width, game_display):
        self.food_img = pygame.image.load('imgs/food_small.png')
        self.game_display = game_display
        self.food_x = display_height * (random.randint(5, 95) / 100)
        self.food_y = display_width * (random.randint(5, 95) / 100)

    def draw(self):
        self.game_display.blit(self.food_img,(self.food_x, self.food_y))


