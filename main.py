import sys

import pygame


class AlienInvasion:
    """General class """

    def __init__(self):
        """Initial resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Main cycle"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        pygame.display.flip()


#if __name__ == '__main__':
    # Start new example and start new game
#    ai = AlienInvasion()
 #   ai.run_game()
