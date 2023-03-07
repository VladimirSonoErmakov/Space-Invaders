import pygame, sys
from bullet import Bullet
from enemy import Ino

def events(screen, gun, bullets):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: #нажатие
            if event.key == pygame.K_RIGHT: #право
                gun.mright = True
            elif event.key == pygame.K_LEFT: #лево
                gun.mleft = True    
            elif event.key == pygame.K_SPACE: #пробел
                new_bullet = Bullet (screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP: #отжатие
            if event.key == pygame.K_RIGHT: # право
                gun.mright = False
            elif event.key == pygame.K_LEFT: #лево
                gun.mleft = False
    
def update(bg_color, screen, gun, inos, bullets):
    """обновление экрана"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()
    
def update_bullets(bullets):
    """обновляем позиции пулек"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets)) #проверяем что улетевщие за предел экрана пульки не жрут память

def create_army(screen, inos):
    """создаеь армию пришельцев"""
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 2 * ino_width) / ino_width)
    
    for ino_number in range(number_ino_x):
        ino = Ino(screen)
        ino.x = ino_width + ino_width * ino_number
        ino.rect.x = ino.x
        
    
 