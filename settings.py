# Author: Wilyendri Duran
# Homwork 4: videoGame
# Ethan Cerami

class Settings:
    """A class to store all the settings for Jumper"""

    def __init__(self):
        # Screen settings
        self.screen_width = 1600
        self.screen_hight = 600
        self.bg_color = (130, 200, 90)

        # Character settings
        self.ch_lives = 4

        # Monster settings
        self.monsters_allowed_on_screen = 10
        # TESTING:
        self.increment_speedup_scale = 1.3
        self.increment_speed_every = 3 # Every 3 monsters

    def initialize_dynamic_settings(self):
        """Intiliaze settings that change throught the game."""
        self.ch_speed = 2
        self.monster_speed = 0.8

    def increase_speed(self):
        """Increase speed setiings"""
        self.ch_speed = self.ch_speed * self.increment_speedup_scale
        self.monster_speed = self.monster_speed * self.increment_speedup_scale




