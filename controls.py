import pygame, sys
import time
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
    
def update(bg_color, screen, stats, sc,  gun, inos, bullets):
    """обновление экрана"""
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()
    
    
def update_bullets(screen, stats, sc, inos, bullets):
    """обновляем позиции пулек"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets)) #проверяем что улетевщие за предел экрана пульки не жрут память
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collisions:
        for inos in collisions.values():
            stats.score += 1 * len(inos) 
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)
    
        
    
def gun_kill(stats, screen, sc, gun, inos, bullets):
    """пушка разбита"""
    if stats.gun_left > 0:
        stats.gun_left -= 1
        sc.image_guns()
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()
        

def update_inos(stats, screen, sc, gun, inos, bullets):
    """обновление позицию пришельцев"""
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, sc, gun, inos, bullets)
    inos_check(stats, screen, sc, gun,inos, bullets)


def inos_check (stats, screen, sc, gun,inos, bullets):
    """проверка добралась ли армия до края экрана"""
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun,inos, bullets)
            break

def create_army(screen, inos):
    """создаеь армию пришельцев"""
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((800 - 100 -  2 * ino_height) / ino_height)
    
    for row_number in range(number_ino_y - 5): 
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + ino_width * ino_number
            ino.y = ino_height + ino_height * row_number
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + 1 *ino.rect.height * row_number
            inos.add(ino)
    
def check_high_score(stats, sc):
     """проверяем появление нового рекорда"""
     if stats.score > stats.hiscore:
        stats.hiscore = stats.score
        sc.image_high_score()
        with open('hiscore.txt', 'w') as f:
            f.write(str(stats.hiscore))
        