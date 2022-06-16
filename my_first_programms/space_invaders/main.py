import pygame
import controls
from lasergun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption('Space * Invaders')
    bg_color = (32, 32, 32)
    gun = Gun(screen)
    bullets = Group()
    enemies = Group()
    controls.create_army(screen, enemies)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game == True:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, enemies, bullets)
            controls.update_bullets(screen, stats, sc, enemies, bullets)
            controls.update_enemies(stats, screen, sc, gun, enemies, bullets)


run()
