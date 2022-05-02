import sys

import pygame
from settings import Settings


class AlienInvasion:
    """General class """

    def __init__(self):
        """Initial resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")
        # background color
        self.ba_colour = (230, 230, 230)

    def run_game(self):
        """Main cycle"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # remake screen in every cycle
                self.screen.fill(self.setings.bg_color)
                # show last screen
                pygame.display.flip()


if __name__ == '__main__':
    # Start new example and start new game
    ai = AlienInvasion()
    ai.run_game()
