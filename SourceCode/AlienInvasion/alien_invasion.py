import sys
import pygame

def run_game():

    #初始化游戏
    pygame.init()

    #创建一个屏幕对象，尺寸是1200*800
    screen = pygame.display.set_mode((1200,800))

    #设置窗口标题
    pygame.display.set_caption("Alien Invasion")

    #游戏主循环
    while True:

        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #让最近绘制的屏幕可见
        pygame.display.flip()

run_game()