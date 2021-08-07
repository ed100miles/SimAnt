import pygame
import random
pygame.init()

# Ant 
class Ant:
    def __init__(self, display_height, display_width, game_display):
        self.ant_img = pygame.image.load('imgs/small_ant.png')
        self.ant_x = display_height * 0.5
        self.ant_y = display_width * 0.5
        self.rect = (self.ant_x, self.ant_y, 10, 10)
        self.ant_up = False
        self.ant_down = False
        self.ant_left = False
        self.ant_right = False
        self.with_food = False
        self.game_display = game_display
        
        self.health = 50
        print(f'ant health: {self.health}')

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
            self.ant_y -= 2
        if self.ant_down:
            self.ant_y += 2
        if self.ant_left:
            self.ant_x -= 2
        if self.ant_right:
            self.ant_x += 2
        return
    
    def orientate(self):
        if not self.with_food:
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
        else:
            self.ant_img = pygame.image.load('imgs/sugar_small.png')

    def feeding(self, food=None):
        if food is not None:
            ant_x_coord = (self.ant_x, self.ant_x + self.rect[2]) # e.g (210, 220) if 'x' 210 and width 10
            ant_y_coord = (self.ant_y, self.ant_y + self.rect[3])
            food_x_coord = (food[0], food[0] + food[2])
            food_y_coord = (food[1], food[1] + food[3])
            if ant_x_coord[1] >= food_x_coord[0] and ant_x_coord[0] <= food_x_coord[1]:
                if ant_y_coord[1] >= food_y_coord[0] and ant_y_coord[0] <= food_y_coord[1]:
                    if self.health < 100:
                        self.health = 100
                    print(f'ant health: {self.health}')
                    if self.health == 100 and self.with_food == False:
                        self.with_food = True
                        # food.capacity -= 1   # !!!!!!!!!!!! complete this

    def draw(self, food_rect):
        self.feeding(food_rect)
        self.orientate()
        self.game_display.blit(self.ant_img,(self.ant_x, self.ant_y))


class EnemyAnt:
    def __init__(self, display_height, display_width, game_display):
        self.ant_img = pygame.image.load('imgs/small_ant.png')
        self.ant_x = (display_height * random.randint(15, 85) / 100)
        self.ant_y = (display_width * random.randint(15, 85) / 100)
        self.ant_up = False
        self.ant_down = False
        self.ant_left = False
        self.ant_right = False
        self.game_display = game_display
        self.health = 100

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

    def direction_decision(self, player_ant):
        # if good health, go fight:
        if self.health > 90:
            if player_ant is not None:
                if player_ant.ant_x > self.ant_x:
                    self.ant_right = True
                    self.ant_left = False
                elif player_ant.ant_x < self.ant_x:
                    self.ant_left = True
                    self.ant_right = False
                else:             # if ==
                    self.ant_right = self.ant_left = False

                if player_ant.ant_y < self.ant_y:
                    self.ant_up = True
                    self.ant_down = False
                elif player_ant.ant_y > self.ant_y:
                    self.ant_up = False
                    self.ant_down = True
                else:
                    self.ant_up = self.ant_down = False

    def draw(self, player_ant):
        self.direction_decision(player_ant)
        self.ant_move()
        self.orientate()
        self.game_display.blit(self.ant_img,(self.ant_x, self.ant_y))


class Food:
    def __init__(self, display_height, display_width, game_display):
        self.food_img = pygame.image.load('imgs/food_small.png')
        self.game_display = game_display
        self.food_x = display_height * (random.randint(25, 75) / 100)
        self.food_y = display_width * (random.randint(25, 75) / 100)
        self.capacity = 10
        self.rect = (self.food_x, self.food_y, 20, 20)

    def draw(self):
        self.game_display.blit(self.food_img,(self.food_x, self.food_y))


class Nest:
    def __init__(self, display_height, display_width, game_display):
        self.nest_img = pygame.image.load('imgs/nest.png')
        self.game_display = game_display
        self.food_x = display_height * (random.randint(25, 75) / 100)
        self.food_y = display_width * (random.randint(25, 75) / 100)