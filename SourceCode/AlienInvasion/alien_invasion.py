import sys
import pygame

def run_game():

    #��ʼ����Ϸ
    pygame.init()

    #����һ����Ļ���󣬳ߴ���1200*800
    screen = pygame.display.set_mode((1200,800))

    #���ô��ڱ���
    pygame.display.set_caption("Alien Invasion")

    #��Ϸ��ѭ��
    while True:

        #���Ӽ��̺�����¼�
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #��������Ƶ���Ļ�ɼ�
        pygame.display.flip()

run_game()