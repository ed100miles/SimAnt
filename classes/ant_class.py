import pygame
pygame.init()

# Ant 
class Ant:
    def __init__(self):
        self.ant_img = pygame.image.load('imgs/small_ant.png')
        self.ant_x = game_display_height * 0.5
        self.ant_y = game_display_width * 0.5
        self.ant_up = False
        self.ant_down = False
        self.ant_left = False
        self.ant_right = False

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
    
    def ant_draw(self):
        game_display.blit(self.ant_img,(self.ant_x, self.ant_y))