import pygame
from pygame.locals import *

from game_utility import ScreenInitializer
from game_utility import GameFlow

"""Initialize pygame and run the game."""

if __name__ == "__main__":
    pygame.init()
    pygame.event.get()
    game_instance = GameFlow(pygame)
    game_instance.run_game_logic()
