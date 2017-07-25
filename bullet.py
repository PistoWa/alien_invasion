import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''creat bullet class'''


    def __init__(self, ai_setting, screen, ship):
        '''creat bullet object'''
        super(Bullet, self).__init__()
        self.screen = screen

        #creat a rect in the (0, 0), and get location right
        self.rect = pygame.Rect(0, 0, ai_setting.bullet_width,
            ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #store y
        self.y = float(self.rect.y)

        #speed and color
        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor

    def update(self):
        '''move the bullet up'''
        #update self.y
        self.y -= self.speed_factor
        #update self.rect.y
        self.rect.y = self.y

    def draw_bullet(self):
        #draw the rect 
        pygame.draw.rect(self.screen, self.color, self.rect)