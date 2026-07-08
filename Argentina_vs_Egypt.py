import sys
import pygame

from settings import Settings


class AlienInvasion :

    def __init__(self):
        #"游戏初始化"
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
        (self.settings.logic_screen_width,
         self.settings.logic_screen_height),
        pygame.FULLSCREEN | pygame.SCALED   # ✅ 全屏 + 自动适配
    )
        pygame.display.set_caption("Argentina_vs_Egypt")

    def run_game(self):
        #"游戏运行主循环"
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)

            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()