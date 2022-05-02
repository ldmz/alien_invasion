import pygame

class Ship:
    """Clas for Ship"""
    def __init__(self, ai_game):
        """Initialise ship and its start position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load ship image and get its rect
        self.image = pygame.image.load('images/ship.bnp')
        self.rect = self.image.get_rect()
        #make every ship in bottom, center part of screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """draw the ship in its position"""
        self.screen.blit(self.image, self.rect)