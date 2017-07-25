import pygame

class Ship():
    '''almost everything about ship'''
    
    def __init__(self, screen, ai_setting):
        #inition
        self.screen = screen

        #load image and get the rectangle
        src_image = 'image/ship4.bmp'
        self.image = pygame.image.load(src_image)
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.ai_setting = ai_setting

        #ship locate
        self.center = float(self.screen_rect.centerx)

        #ship moving right
        self.moving_right = False
        self.moving_left = False

        #print the ship in the middle
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_setting.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        #plot the ship
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx

        

