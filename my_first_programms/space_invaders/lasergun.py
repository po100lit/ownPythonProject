import pygame
from pygame.sprite import Sprite


class Gun(Sprite):
        
    def __init__(self, screen):  # инициализация пушки
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/lasergun.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.m_right = False
        self.m_left = False

    def output(self):  # отрисовка пушки
        self.screen.blit(self.image, self.rect)

    def update_gun(self):  # обновление позиции пушки
        if self.m_right and self.rect.right < self.screen_rect.right:
            self.center += 0.3
        elif self.m_left and self.rect.left > 0:
            self.center -= 0.3
        self.rect.centerx = self.center

    def create_gun(self): # новая пушка после смерти
        self.center = self.screen_rect.centerx