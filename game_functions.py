import sys
from time import sleep

import pygame
from bullet import Bullet
from alien import Alien
from button import Button

def fire_bullet(ai_setting, screen, ship, bullets):
    if len(bullets) < ai_setting.bullet_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)

def check_key_down_events(event,ai_setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        #move the ship right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_key_up_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_setting, screen, ship, bullets, play_button, stats):
    '''call events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, ai_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y, ai_setting)

def check_play_button(stats, play_button, mouse_x, mouse_y, ai_setting):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True
        stats.reset_stats(ai_setting)

def update_screen(ai_setting, screen, ship, aliens, bullets, stats, button):
    #screen color
    screen.fill(ai_setting.bg_color)

    #plot ship
    ship.blitme()
    #plot alien
    aliens.draw(screen)

    #update bullet
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #play button
    if not stats.game_active:
        button.draw_button()

    #display
    pygame.display.flip()

def update_bullets(ai_setting, screen, ship, bullets, aliens):
    '''something with bullets'''
    #update bullets
    bullets.update()

    #delete missing bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    check_bullet_alien_collision(ai_setting, screen, ship, bullets, aliens)

def check_bullet_alien_collision(ai_setting, screen, ship, bullets, aliens):
        #check collitions
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)

    #check if aliens were killed
    if len(aliens) == 0:
        bullets.empty()
        creat_fleet(ai_setting, screen, ship, aliens)

def get_number_alien_x(alien_width, ai_setting):
    available_space_x = ai_setting.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x

def get_number_rows(ai_setting, ship_height, alien_height):
    available_space_y = (ai_setting.screen_height -
        (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def creat_alien(ai_setting, screen, aliens, alien_number, row_number):
    #creat only one alien
    alien = Alien(ai_setting, screen)
    alien.x = alien.rect.width + 2 * alien.rect.width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def creat_fleet(ai_setting, screen, ship, aliens):


    alien = Alien(ai_setting, screen)
    #get number x
    number_alien_x = get_number_alien_x(alien.rect.width, ai_setting)
    number_rows = get_number_rows(ai_setting, ship.rect.height, alien.rect.height)
    #creat aliens
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            creat_alien(ai_setting, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_setting, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_setting, aliens)
            break

def change_fleet_direction(ai_setting, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.fleet_drop_speed
    ai_setting.fleet_direction *= -1

def check_aliens_bottom(ai_setting, screen, stats, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    #check
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #handle like ship_hit
            ship_hit(ai_setting, screen, stats, ship, aliens, bullets)
            break


def update_aliens(ai_setting, screen, stats, ship, aliens, bullets):
    check_fleet_edges(ai_setting, aliens)
    aliens.update(ai_setting)

    #check hit
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_setting, screen, stats, ship, aliens, bullets)

    #check alien on bottom
    check_aliens_bottom(ai_setting, screen, stats, ship, aliens, bullets)

def ship_hit(ai_setting, screen, stats, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1

        #empty aliens and bullets
        aliens.empty()
        bullets.empty()

        #creat a new
        creat_fleet(ai_setting, screen, ship, aliens)
        ship.center_ship()

        sleep(1)

    else:
        stats.game_active = False
