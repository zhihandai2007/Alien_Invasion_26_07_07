import pygame
import sys

class Controller:

    def __init__(self,screen):
        self.screen = screen

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()