import pygame


class Enemy(pygame.sprite.Sprite):  # класс пришельца

    def __init__(self, screen):  # инициализация пришельца и его позиции
        super(Enemy, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):  # вывод пришельца на экран
        self.screen.blit(self.image, self.rect)

    def update(self):  # перемещаем пришельцев вниз
        self.y += 0.03
        self.rect.y = self.y
