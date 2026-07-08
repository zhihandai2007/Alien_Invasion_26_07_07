import pygame
import constants

class Renderer:

    def __init__(self,screen):
        self.screen = screen

    def draw(self):
        self.screen.fill(constants.BG_COLOR)

        pygame.display.flip()