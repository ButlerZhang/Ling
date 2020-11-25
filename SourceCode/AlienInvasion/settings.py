class Settings():
    """所有配置信息"""

    def __init__(self):
        self.screen_width = 900
        self.screen_height = 600

        #screen background color
        #red_color = (255,0,0)
        #blue_color = (0,0,255)
        #green_color = (0,255,0)
        self.background_color = (230, 230, 230)

        #飞船移动速度
        self.ship_speed_factor = 1.5

        #子弹移动速度
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60

        #同时最多能射出多少个子弹
        self.bullets_allowed = 3

        #外星人移动速度
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1 #1向右，-1向左，方便计算
