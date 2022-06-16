import pygame.font
from lasergun import Gun
from pygame.sprite import Group


class Scores():  # вывод игровой информации
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_high_score()
        self.image_lives()

    def image_score(self):  # делаем из текста картинку
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (32, 32, 32))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_high_score(self):
        self.hight_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (32, 32, 32))
        self.hight_score_rect = self.hight_score_image.get_rect()
        self.hight_score_rect.centerx = self.screen_rect.centerx
        self.hight_score_rect.top = self.screen_rect.top + 20

    def image_lives(self): # количество жизней
        self.lives = Group()
        for lives_number in range(self.stats.guns_left):
            live = Gun(self.screen)
            live.rect.x = 15 + lives_number * live.rect.width
            live.rect.y = 20
            self.lives.add(live)

    def show_score(self):  # вывод счета на экран
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.hight_score_image, self.hight_score_rect)
        self.lives.draw(self.screen)