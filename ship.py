import pygame


class Ship:
    """Clas for Ship"""

    def __init__(self, ai_game):
        """Initialise ship and its start position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # make every ship in bottom, center part of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store ship horizzontal position
        self.x = float(self.rect.x)

        # movements
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update from self.x
        self.rect.x = self.x

    def blitme(self):
        """draw the ship in its position"""
        self.screen.blit(self.image, self.rect)
