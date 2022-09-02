# Author: Wilyendri Duran
# Homwork 4: videoGame
# Ethan Cerami

import pygame
from pygame.sprite import Sprite

class Character(Sprite):
    """A class to manage Character"""

    def __init__(self, ai_game):
        super().__init__()
        """Initialize the character and its started position"""
        # Call screen method of the given class
        self.screen = ai_game.screen
        # This is the important part: get the rect of screen
        self.screen_rect = ai_game.screen.get_rect()
        # Character settings
        self.setting = ai_game.settings
        # Load image of character and get its rect
        self.image = pygame.image.load('image/character.bmp')
        self.rect = self.image.get_rect()

        # Start character at the begining of the screen
        self.rect.bottomleft = self.screen_rect.bottomleft

        # Moving character
        self.moving_right = False
        self.moving_left = False
        # Jumping character
        self.jump = False
        self.jump_count = 0
        self.change_sign = 1

        # Store a decimal value for character's horizontal position
        self.x = float(self.rect.x)
        
    def update(self):
        """Update character's position based on the movement flag"""
        
        if self.moving_right and self.rect.right <= self.screen_rect.right:
                self.x += self.setting.ch_speed
        if self.moving_left and self.rect.left > 0:
                self.x -= self.setting.ch_speed
        elif self.jump:
            # Start moving vertical Y if jump is true
            self.rect.y -= 1 * self.change_sign
            # Keep track of vertical movement
            self.jump_count -= 1
            #print(self.rect.y)
            # When it is negative, start moving downwards            
            if self.jump_count < 0:
                # Change sign to start adding instead of substracting
                self.change_sign = -1
            # Avoid moving further the boundaries of the bottom screen
            if self.rect.bottom == self.screen_rect.bottom:
                self.jump = False
                self.jump_count = 0
                self.change_sign = 1              
            
        
        # Update rect object from self.x
        self.rect.x = self.x
        
    def blitme(self):
        """Draw character at its current location"""
        self.screen.blit(self.image, self.rect)

    def restart_character(self):
        """Start character from original position"""
        self.rect.bottomleft = self.screen_rect.bottomleft
        self.x = float(self.rect.x)
        self.jump = False
        self.jump_count = 0
        self.change_sign = 1  


