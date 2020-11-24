import pygame

class Ship():
    """一艘飞船"""

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #飞船初始位置是居中
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #使用浮点数方便后续的精细控制
        self.center = float(self.rect.centerx)

        #让飞船连续移动的标记
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """更新飞船的坐标"""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """根据当前位置绘制飞船图片"""
        self.screen.blit(self.image, self.rect)
