# Author: Wilyendri Duran
# Homwork 4: videoGame
# Ethan Cerami

import sys
from time import sleep

import pygame

from settings import Settings
from character import Character
from monster import Monster
from game_stats import GameStats
from button import Button
from score import Score

class Jumper:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        # Set screen to fullscreen
        self.screen = pygame.display.set_mode\
            ((0,0), pygame.FULLSCREEN)
        pygame.display.set_caption("Jumper Game")

        # Make the game match the full screen
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_hight = self.screen.get_rect().height

        # Instance to store game statistics.
        self.stats = GameStats(self)

        # Create instance oof character
        self.character = Character(self)

        # Group of monsters
        self.monsters = pygame.sprite.Group()

        # Playe button
        self.play_button = Button(self, "Play")

        # Instance to show lives
        self.score = Score(self)

        # Keep of monster removed
        self.montsers_removed = 0



    def run_game(self):
        """Start main loop that runs the game"""
        while True:
            self._check_events()
            # Update character and monsters if game has started
            if self.stats.game_active:
                self.character.update()
                self._update_monster()

            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            # Watch for keyboard and mouse EVENTS
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)



    def _update_screen(self):
        """Update image of the screen and flip to the new one"""
        # Redraw screen during each pass
        self.screen.fill(self.settings.bg_color)
        # Update character
        self.character.blitme()
        # Draw each element of the group b
        for monster in self.monsters.sprites():
            monster.draw_monster()
        # Draw lives left
        self.score.show_lives()
        # Draw play button if game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
        # Update screen by drawing the most recent screm viisble
        pygame.display.flip()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.character.moving_right = True
        # Avoid moving left on the air
        elif event.key == pygame.K_LEFT and self.character.rect.bottom\
             == self.screen.get_rect().bottom:
            self.character.moving_left = True
        # Can only jump when is on the floor (bottom of the screen)
        elif event.key == pygame.K_SPACE and self.character.rect.bottom\
                == self.screen.get_rect().bottom:
            self._create_monster()
            # Making sure character cannot jump to the left
            self.character.moving_left = False
            # How hight the character would jump
            self.character.jump_count = 150
            self.character.jump = True
        # Exit game when ESC is pressed
        elif event.key == pygame.K_ESCAPE\
            or event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.character.moving_right = False
        elif event.key == pygame.K_LEFT and self.character.rect.bottom\
             == self.screen.get_rect().bottom:
            # Making sure character cannot jump to the left
            self.character.moving_left = False
            self.character.jump = False
        elif event.key == pygame.K_SPACE and self.character.rect.bottom\
                == self.screen.get_rect().bottom:
            # Making sure character cannot jump to the left
            self.character.moving_left = False
            self.character.jump = False

    def _create_monster(self):
        """Create monsters"""
        monster = Monster(self)

        if len(self.monsters) < self.settings.monsters_allowed_on_screen:
            self.monsters.add(monster)


    def _update_monster(self):
        """Update the monsters on screen and manages collision"""
        self.monsters.update()
        # Remove monsters that passed left boundary
        for monster in self.monsters.copy():
            if monster.rect.left <= 0:
                self.monsters.remove(monster)
                self.montsers_removed += 1

        # Increment game speed once has passed number of monsters
        if self.montsers_removed == self.settings.increment_speed_every:
            self.settings.increase_speed()
            self.montsers_removed = 0

        # If character and moster collide
        if pygame.sprite.spritecollideany(self.character, self.monsters):
            self._hit_character()

    def _hit_character(self):
        """Respond to the character being hit by a monster"""
        if self.stats.lives_left > 0:

            # Decrement character lives
            self.stats.lives_left -= 1

            # Show lives left
            self.score.prep_character()

            # Get rid of all remaining monsters
            self.monsters.empty()

            # Create new monsters and restart character attributes
            self.character.restart_character()
            self._create_monster()

            # Increment speed once the character has been hit
            self.settings.increase_speed()


            # Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            # Make pointer appear after game has ended
            pygame.mouse.set_visible(True)

    def _check_play_button(self, mouse_pos):
        """Start a new game when button is clicked"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.score.prep_character()
            self.stats.game_active = True

             # Get rid of all remaining monsters
            self.monsters.empty()

            # Create new monster
            self._create_monster()
            self.character.restart_character()
            self.settings.initialize_dynamic_settings()

            # Hide pointer
            pygame.mouse.set_visible(False)


if __name__ == '__main__':
    # Make a game instance and run game
    ai = Jumper()
    ai.run_game()
