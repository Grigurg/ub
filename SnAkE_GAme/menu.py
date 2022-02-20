import pygame_menu
import pygame
import os
from main import start_game
pygame.init()


def start_main():
    start_game()


screen = pygame.display.set_mode([460, 530])
menu = pygame_menu.Menu('Welcome', 400, 500,
                        theme=pygame_menu.themes.THEME_SOLARIZED)

menu.add.text_input('Name :', default='')
menu.add.button('Play', start_game)
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)
