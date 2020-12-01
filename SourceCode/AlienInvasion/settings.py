class Settings():
    """所有配置信息"""

    def __init__(self):

        #屏幕设置
        self.screen_width = 900
        self.screen_height = 600

        #screen background color
        #red_color = (255,0,0)
        #blue_color = (0,0,255)
        #green_color = (0,255,0)
        self.background_color = (230, 230, 230)

        #飞船最多有几条命
        self.ship_limit = 3

        #子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60

        #同时最多能射出多少个子弹
        self.bullets_allowed = 3

        #外星人设置
        self.fleet_drop_speed = 10

        #以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1

        #外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
    
        #fleet_direction
        self.fleet_direction = 1 #1向右，-1向左，方便计算

        #记分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置以及点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        #print(self.alien_points)
