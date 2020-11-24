import sys
import pygame

from bullet import Bullet



def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):

    #使用背景色填充屏幕
    screen.fill(ai_settings.background_color)

    #绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #根据位置绘制飞船
    ship.blitme()

    #更新所有需要显示的Surface到屏幕上
    pygame.display.flip()

def update_bullets(bullets):
    #这里是Group.update()
    bullets.update()

    #如果子弹已经超出屏幕，则删除它
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
    """发射子弹"""

    #控制子弹的个数
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
