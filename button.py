# Author: Wilyendri Duran
# Homwork 4: videoGame
# Ethan Cerami

import pygame.font

class Button:
    """Class that output button to start game"""
    
    def __init__(self, ai_game, msg):
        """Initiliaze button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build button's rect and center it
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Button message
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn message into a rendered image and center text on button"""
        self.msg_image = self.font.render(msg, True, self.text_color,\
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then the message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
            

