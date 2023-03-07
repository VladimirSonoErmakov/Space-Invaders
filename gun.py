import pygame

class Gun():
    def __init__(self, screen):
        """инит пушки"""
        
        self.screen = screen
        self.image = pygame.image.load('images/canon.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.screen_rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False
        
        
    def output(self):
        """отрисовка"""    
        self.screen.blit(self.image, self.rect)
    
    def update_gun(self):
        """обновление позиции"""  
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 0.2
        if self.mleft and self.rect.left > 0:
            self.center -= 0.2
        self.rect.centerx = self.center
        