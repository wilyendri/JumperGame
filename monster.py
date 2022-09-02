# Author: Wilyendri Duran
# Homwork 4: videoGame
# Ethan Cerami

import pygame
from pygame.sprite import Sprite

class Monster(Sprite):
    """A class tha represent a single mosnter"""

    def __init__(self, ai_game):
        """Initialize the monster and set starting point"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.setting = ai_game.settings

        # Load monster image
        self.image = pygame.image.load('image/monster.bmp')
        self.rect = self.image.get_rect()

        # Start monster on the bottom right of the screen
        self.rect.bottomright = self.screen_rect.bottomright
        
        # Store the monster in the exact horizontal's position
        self.x = float(self.rect.x)

    # Move monster horizontally
    def update(self):
        """Move monster once the character start moving"""
        self.x -= self.setting.monster_speed
        self.rect.x = self.x

    def draw_monster(self):
        """Draw monster to the screen"""
        self.screen.blit(self.image, self.rect)


