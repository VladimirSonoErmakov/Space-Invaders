import pygame

class Ino(pygame.sprite.Sprite):
    """класс одного пришельца"""
    
    def __init__ (self, screen):
        """инициализация и изначальная позиция"""
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        
    def draw(self):
        """рисуем врага"""    
        self.screen.blit(self.image, self.rect)
        
    def update (self):
        """перемещаем врагов"""
        self.y += 0.05
        self.rect.y = self.y