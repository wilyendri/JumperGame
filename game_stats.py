# Author: Wilyendri Duran
# Homwork 4: videoGame
# Ethan Cerami

class GameStats:
    """Track statitics for Jumper"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        # Start Jumper in an inactive state.
        self.game_active = False
        

    def reset_stats(self):
        """Initialize statitics that can change during the game"""
        self.lives_left = self.settings.ch_lives
         
        

    
        