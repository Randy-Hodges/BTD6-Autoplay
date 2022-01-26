<h1 align='center'> BTD6 Autoplay </h1>


### Overview
The game Bloons Tower Defense 6 (BTD6) has seasonal collection events where you get rewarded 'insta monkeys' for playing the game, but you have to play a lot to get the rewards. Screw that. Instead, I made this bot that plays through all of the hardest levels that BTD6 provides, and it runs continuously so I can 'play' the game while I sleep.

Also, if you don't know, BTD6 is a game where you place monkeys (and other towers) on a map and the monkeys try and stop a wave of balloons from reaching the end of the map. ![example play of BTD6](https://user-images.githubusercontent.com/56176262/151027387-73c97797-2bfb-4f7e-a7fa-c9a78a5ec9bf.png)

### Basic Functionality
This bot works by running an action script and by keying off select screenshots of the game. In short, the bot takes a screenshot of the top left of the screen, runs that through a pre-trained neural network to extract a money value, and then references an action script to determine if the next monkey can be placed/upgraded. There are some additional use cases for specific scenarios, but this is generally how the bot works. After a level is beaten, the bot cycles though menus until it finds the next, most optimal level to beat and starts that level.

### Using the bot
If you want to simply beat a level, you can run game_loop(action script) from the autoplayV2.py script. When using a custom action script, make sure that your action script is loaded in and passed into game_loop(). If you are having trouble loading in your action_script, either check the imports in /action_scripts/\_\_init\_\_.py or move your action script into the same folder as autoplayV2.py. 

If you want the bot to repeatedly play through all of the expert levels, you would run play_collection_event.py. However, before running the file you need to make sure that the bot is using the correct bonus rewards image (located in reference_images). This is a small image next to a level that indicates that you will get bonus rewards from playing that level and it changes for every event. Ex:

![bonus rewards](/Autoplay/reference_images/bonus_rewards.png)

This image is how the bot chooses the next level to play. To change this image, alter the string (file path) of the bonus_rewards_image variable to the desired image (The bonus_rewards_image variable is located at the top of the play_collection_event.py file). You can screenshot a new bonus reward symbol and add it to the repo if needed.
 
### Making your own action script
The easiest way to go about this is by looking at one of the already functioning scripts. This will be the fastest way to learn how the Action class works, especially because the examples read very naturally. The action scripts will normally read like 'place [monkey name] [monkey type] at [location]', eg 'place dart1 dart monkey at (50, 20)'. When adding a new script in the action_scripts folder, make sure to check the import statements in \_\_init\_\_.py and see if you need to import your script. Typically when making a new script you will place some monkeys, start the game, and then continue upgrading/placing until the game is over. 
>Quick tip: You can easily copy your mouse position when planning to place monkeys by using the copy_mouse_position.py script. This is located in the root folder.
 
### Things to be aware of
- Since the latest BTD6 update, the current Workshop script no longer beats the Workshop map
- All placements were made using my computer screen's measurements. This may or may not affect performance on your computer.
- Not all of the monkey upgrade costs have been added. When adding a new monkey, make sure to check monkey_info.py to see if the upgrade costs are there. If they aren't and you want to use that new monkey, just add in the monkey costs into the monkey_info dictionary. 
 
### To do
- Scale placement of monkeys with size of computer screen.
- Add in the missing upgrade costs into monkey_info.py
- Update workshop script to beat the level.
- Move the clicking-only methods to their own file.
- Containerize the whole project for deployment on other computers that don't have the necessary packages.
