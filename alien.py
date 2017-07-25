import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_setting, screen):
        #inition
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_setting = ai_setting
        alien_image = 'image/alien2.bmp'

        #load the image and set the rect
        self.image = pygame.image.load(alien_image)
        self.rect = self.image.get_rect()

        #aliens on the left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #location
        self.x = float(self.rect.x)

    def check_edges(self):

    	screen_rect = self.screen.get_rect()
    	if self.rect.right >= screen_rect.right:
    		return True
    	elif self.rect.right <= 0:
    		return True

    def update(self, ai_setting):
    	'''move aliens right'''
    	self.x += (self.ai_setting.alien_speed_factor * ai_setting.fleet_direction)
    	self.rect.x = self.x

    def blitme (self):
        self.screen.blit(self.image, self.rect)