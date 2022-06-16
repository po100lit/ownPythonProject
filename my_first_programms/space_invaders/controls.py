import pygame
import sys
from bullet import Bullet
from enemy import Enemy
import time


def events(screen, gun, bullets):  # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # move to the right
            if event.key == pygame.K_RIGHT:
                gun.m_right = True
            elif event.key == pygame.K_LEFT:  # move to the left
                gun.m_left = True
            elif event.key == pygame.K_SPACE:  # fired by space
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                gun.m_right = False
            elif event.key == pygame.K_LEFT:
                gun.m_left = False


def update(bg_color, screen, stats, sc, gun, enemies, bullets):  # обновление экрана
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    enemies.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, sc, enemies, bullets):  # обновляем позиции пуль
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
    if collisions:
        for enemies in collisions.values():
            stats.score += 10 * len(enemies)
        sc.image_score()
        check_highscore(stats, sc)
        sc.image_lives()
    if len(enemies) == 0:
        bullets.empty()
        create_army(screen, enemies)


def gun_kill(stats, screen, sc, gun, enemies, bullets):  # стокновение пушки и армии
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_lives()
        enemies.empty()
        bullets.empty()
        create_army(screen, enemies)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def update_enemies(stats, screen, sc, gun, enemies, bullets):  # обновляем позиции пришельцев
    enemies.update()
    if pygame.sprite.spritecollideany(gun, enemies):
        gun_kill(stats, screen, sc, gun, enemies, bullets)
    enemies_check(stats, screen, sc, gun, enemies, bullets)

def enemies_check(stats, screen, sc, gun, enemies, bullets): # проверка опустились пришельцы до низа
    screen_rect = screen.get_rect()
    for enemy in enemies.sprites():
        if enemy.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, enemies, bullets)
            break


def create_army(screen, enemies):  # создаем армию пришельцев
    enemy = Enemy(screen)
    enemy_width = enemy.rect.width
    number_enemy_x = int((700 - 2 * enemy_width) / enemy_width)
    enemy_height = enemy.rect.height
    number_enemy_y = int((800 - 100 - 2 * enemy_height) / enemy_height)
    for row_number in range(number_enemy_y - 1):
        for enemy_number in range(number_enemy_x):
            enemy = Enemy(screen)
            enemy.x = enemy_width + (enemy_width * enemy_number)
            enemy.y = enemy_height + (enemy_height * row_number)
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.rect.height + (enemy.rect.height * row_number)
            enemies.add(enemy)

def check_highscore(stats, sc): # проверка рекорда
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('hs.txt', 'w') as f:
            f.write(str(stats.high_score))
