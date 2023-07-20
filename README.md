# Jumper Game

![Jumper Game Screenshot](screenshot.png)

## Objective

The objective of the game is to try to avoid the monsters coming in your way and survive as long as possible.

## Rules

- The player character has 3 lives.
- If a monster touches the player character, you lose one life.
- The player has to jump in order to evade the monsters.
- Every time the player jumps, another monster is created.
- The character is allowed to jump forward but not backwards.
- The game speed will increment through the game:
  - When three monsters have passed the screen.
  - When the character has been hit by a monster.
- The game ends when the player has run out of lives.

## Controls

- Space Bar: Allows the character to jump in order to evade the monsters.
- Right Arrow Key: Moves the character to the right of the screen.
- Left Arrow Key: Moves the character to the left of the screen.
- ESC or Q: Exits the game.

## Settings

To modify the game settings, it must be done through the Settings class. This class specifies the behavior of the character and monsters.

These configurable settings include:

- Speed of both character and monsters.
- The number of monsters allowed on the screen.
- The character's lives.
- The size and colors of the screen.
- Speed increment scale.
- How often to increment the speed.

## Running the Game

1. Ensure you have Python installed on your system.
2. Execute `jumper.py` to run the game.
3. The game will initialize with a play button on the screen.
4. Once the button has been clicked, the game starts.

Have fun playing the Jumper Game and see how long you can survive!


