import pygame

from pygame.sprite import Sprite



class Bullet(Sprite):
    """一个子弹，继承自精灵类"""

    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen

        #在屏幕左下角创建子弹，然后立刻设置成从飞船射出来的坐标
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #保存浮点数的Y坐标，方便精细控制
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """更新子弹的Y坐标"""

        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """绘制子弹"""

        pygame.draw.rect(self.screen, self.color, self.rect)
