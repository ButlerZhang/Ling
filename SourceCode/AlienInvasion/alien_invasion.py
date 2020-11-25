import pygame
import game_functions as gf

from ship import Ship
from settings import Settings
from pygame.sprite import Group



def run_game():
    """游戏处理框架"""

    #初始化所有导入的pygame模块
    pygame.init()

    #使用默认配置
    ai_settings = Settings()

    #初始化准备显示的窗口
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,
        ai_settings.screen_height))

    #设置窗口标题
    pygame.display.set_caption("Alien Invasion")

    #创建一个飞船
    ship = Ship(ai_settings, screen)

    #用来保存所有子弹的Group
    bullets = Group()

    #创建一群外星人
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:

        #检测事件
        gf.check_events(ai_settings, screen, ship, bullets)

        #更新飞船位置
        ship.update()

        #更新子弹位置，同时删除无用的子弹
        gf.update_bullets(bullets)

        #更新外星人位置，需要先更新子弹，再更新外星人
        gf.update_aliens(ai_settings, aliens)

        #重新绘制屏幕
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()