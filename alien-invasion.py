#!/usr/bin/python
from setting import Setting
from ship import Ship
from alien import Alien
import game_functions as gf
from game_stats import GameStats
from button import Button

import sys
from pygame.sprite import Group
import pygame

def run_game():
    #inition
    pygame.init()
    ai_setting = Setting()
    #screen
    screen = pygame.display.set_mode((
        ai_setting.screen_width,
        ai_setting.screen_height))
    #title
    pygame.display.set_caption("Alien-Invasion")

    #creat button
    play_button = Button(ai_setting, screen, "Play")
    #creat stats
    stats = GameStats(ai_setting)
    #creat a ship
    ship = Ship(screen, ai_setting)
    #creat bullets
    bullets = Group()
    #creat aliens
    aliens = Group()

    #aliens
    gf.creat_fleet(ai_setting, screen, ship, aliens)

    #loop
    while True:

        #monitor
        gf.check_events(ai_setting, screen, ship, bullets, play_button, stats)

        if stats.game_active:
            #ship the ship.update
            ship.update()
            
            #update bullets
            gf.update_bullets(ai_setting, screen, ship, bullets, aliens)

            #update aliens
            gf.update_aliens(ai_setting,screen, stats, ship, aliens, bullets)

        #update the screen
        gf.update_screen(ai_setting, screen, ship, aliens, bullets, stats, play_button)


run_game()