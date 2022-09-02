##Jumper Game**:
- The obejctive of the game is to try to avoid the monsters coming on your way.

**Rules**:
-The character has 3 lives.
-If the monster touches the character, you lose one life.
-The player has to jump in order to evade the monsters
-Every time the player jumps, another monster is created.
-The character is allowed to jump forward but not backwards.
-The game speed will increment through the game:
	- When three monsters have passed the screen
	- When the character has been hit by a monster
-The game ends when the player has run out of lives

**Controls**:
-Space Bar allows the character to jump in order to evade the monsters.
-The right key arrow moves character to the right of the screen.
-The left key arrow moves character to the left of the screen.
-ESC or Q exits the game.

**Settings**:
To modify the game settings, it must be through the Settings class.
This class specifies the behaviour of the character and monsters.
These behaviours are:
-speed of both character and monster,
-the number of monsters allowed on the screen, 
-the character lives, 
-the size of the screen, 
-colors of the screen,
-speed increment scale,
-how often increment the speed.

**_Running_ _Game_**:
In order to run the game, the jumper.py must be executed. 
The game will initiliaze with a play button on the screen.
Once the button has been cliked, the game starts.

