import sys
import pygame
from ship import Ship
from settings import Settings

def run_game():

    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,
        ai_settings.screen_height))

    #set screen title
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    while True:

        #listen input event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.background_color)
        ship.blitme()
        pygame.display.flip()

run_game()