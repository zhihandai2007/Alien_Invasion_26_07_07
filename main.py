import sys
import pygame

import constants 
from core.engine import Engine

def main():
    pygame.init()

    screen = pygame.display.set_mode(
        (constants.LOGIC_SCREEN_WIDTH,
         constants.LOGIC_SCREEN_HEIGHT),
        pygame.FULLSCREEN | pygame.SCALED
    )
    pygame.display.set_caption("Argentina_vs_Egypt")

    engine = Engine(screen)
    engine.run()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()