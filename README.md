# BTD6 Autoplay
A project that automatically plays levels in the game Bloons Tower Defense 6 (BTD6) without the use of any internal game data or hacking.

### Overview
The game Bloons Tower Defense 6 (BTD6) has seasonal collection events where you get rewarded 'insta monkeys' for playing the game, but you have to play a lot to get the rewards. Screw that. Instead, I made this bot that plays through all of the hardest levels that BTD6 provides, and it runs continuously so I can 'play' the game while I sleep.

Also, if you don't know, BTD6 is a game where you place monkeys (and other towers) on a map and the monkeys try and stop a wave of balloons from reaching the end of the map. <insert basic game image here>

### Basic Functionality
This bot works by running an action script and by keying off select screenshots of the game. In short, the bot takes a screenshot of the top left of the screen, runs that through a pre-trained neural network to extract a money value, and then references an action script to determine if the next monkey to be placed/upgraded. There are some additional use cases for specific scenarios, but this is generally how the bot works. After a level is beaten, the bot cycles though menus until it finds the next, most optimal level to beat and starts that level.

### Action Script Functionality
The action script is essentially just a list of actions to perform once the player has enough money, and it contains some details such as which monkey to place/upgrade, where to place a monkey and some other info. 
 
### Making your own action script
The easiest way to go about this is by looking at one of the already functioning scripts. This will be the fastest way to learn how the Action class works. Typically, you will place some monkeys, start the game, and then continue upgrading/ placing until the game is over. You can easily copy your mouse position when planning to place monkeys by using the copy_mouse_position.py script.
 
### Things to be aware of
- Since the latest BTD6 update, the current Workshop script no longer beats the Workshop map
- All placements were made using my computer screen's measurements. This may or may not affect performance on your computer.
 
### To do
- scale placement of monkeys with size of computer screen.
- update workshop script to beat the level.
- Containerize the whole project for deployment on other computers that don't have the necessary packages.

Will further update README in the future.
