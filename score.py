# Author: Wilyendri Duran
# Homwork 4: videoGame
# Ethan Cerami

from pygame.sprite import Group
from character import Character

class Score():
    """Initialize characters lives"""
    
    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.stats = ai_game.stats
        self.prep_character()
                

    def prep_character(self):
        """Show how many lives are left"""
        self.characters = Group()
        for life in range(self.stats.lives_left):
            character = Character(self.ai_game)
            character.rect.x = 10 + life * character.rect.width
            character.rect.y = 10
            self.characters.add(character)

    def show_lives(self):
        """Draw lives left to the screen"""
        self.characters.draw(self.screen)