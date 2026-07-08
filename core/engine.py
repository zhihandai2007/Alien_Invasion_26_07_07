import sys
import pygame
from core import renderer
from core import controller

class Engine:
    def __init__(self,screen):
        self.screen = screen
        self.controller = controller.Controller(screen)
        self.renderer = renderer.Renderer(screen)

    
    def run(self):
            #"游戏运行主循环"
            while True:
                self.controller.input()
                self.renderer.draw()

            