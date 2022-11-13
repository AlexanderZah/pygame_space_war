import pygame
from gun import Gun
import controls
from pygame.sprite import Group
import time
from stats import Stats
from score import Scores


FPS = 60
clock = pygame.time.Clock()

def run():
    pygame.init()
    screen = pygame.display.set_mode((500, 600))
    pygame.display.set_caption('Space war')
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen,inos)
    stats = Stats()
    sc = Scores(screen,stats)
    while True:
        clock.tick(FPS)

        if stats.run_game == True:
            controls.events(screen,gun,bullets)
            gun.update_gun()
            controls.update_bullets(bg_color, screen, gun, bullets)
            controls.update(bg_color, screen, gun, bullets,inos,stats,sc)
            controls.update_inos(stats,gun,screen,inos,bullets)
run()