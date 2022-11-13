import pygame
import sys
from bullet import Bullet
from ino import Ino
import sys
import time
from stats import Stats

def events(screen,gun, bullets):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.mright = True
            elif event.key == pygame.K_a:
                gun.mleft = True
            elif event.key == pygame.K_w:
                gun.mtop = True
            elif event.key == pygame.K_s:
                gun.mbottom = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            elif event.key == pygame.K_a:
                gun.mleft = False
            elif event.key == pygame.K_w:
                gun.mtop = False
            elif event.key == pygame.K_s:
                gun.mbottom = False


def update(bg_color, screen,gun, bullets,inos,stats,sc):
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    collections = pygame.sprite.groupcollide(bullets,inos,True,True)

    pygame.display.flip()

def update_bullets(bg_color, screen,gun, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def create_army(screen,inos):
    """создаем армию пришельцев"""
    ino = Ino(screen)
    ino_width = ino.rect.width
    ino_height = ino.rect.height
    number_ino_x = (500 - 2 * ino_width) // ino_width
    number_ino_y = (600 - 100 - 2 * ino_height) // ino_height

    for row_number in range(number_ino_y -2):
         for ino_for_x in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + ino_width * ino_for_x
            ino.y = ino_height + ino_height * row_number
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + (ino.rect.height * row_number)
            inos.add(ino)

def gun_kill(stats,gun,screen,inos,bullets):
    if stats.gun_left > 0:


        inos.empty()
        bullets.empty()
        create_army(screen,inos)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()

def update_inos(stats,gun,screen,inos,bullets):
    inos.update()
    if pygame.sprite.spritecollideany(gun,inos):
        gun_kill(stats,gun,screen,inos,bullets)
        stats.gun_left -= 1