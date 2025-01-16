import random

import pygame

from loading import splash_screen
from game import CreateGame
from main_menu import menu

if __name__ == "__main__":
    pygame.init()

    splash_screen()
    menu()
