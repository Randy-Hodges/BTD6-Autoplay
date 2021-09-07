import pyautogui
import numpy as np
import cv2
import time

import autoplayV2

print('-----------')

current_map = ''

def find_image(given_image: str):
    '''
    See if bonus rewards symbol is on the screen.
    :returns: True if symbol found, false otherwise.
              Location of best match.
    '''
    found = False # found symbol
    location = [0, 0]

    method = cv2.TM_SQDIFF_NORMED

    # Read images 
    image = pyautogui.screenshot()
    # make image compatible with cv2
    large_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    small_image = cv2.imread(given_image)

    result = cv2.matchTemplate(small_image, large_image, method)

    # We want the minimum squared difference
    maxLoc, minLoc, comparedLoc, _ = cv2.minMaxLoc(result)

    # Location of best match
    MPx,MPy = comparedLoc
    location = [MPx, MPy]

    if maxLoc < .05:
        print('Found it')
        found = True
        return found, location
    else:
        return found, location


def find_bonus_rewards_symbol():   
    '''
    Finds the map that contains the bonus reward and starts up a game in that map.
    
    :returns: action script of map selected
              if the bonus rewards symbol was found (bool)
    '''
    page_num = 1 # there are two expert map selection pages

    # Click so that we consistently see the left expert maps screen
    click_play()
    time.sleep(.7)  
    click_beginner() 
    time.sleep(.1)
    click_expert()
    time.sleep(1)

    # Check for symbol on expert page 1
    found_symbol, location = find_image('reference_images/bonus_rewards.png')
    if found_symbol:
        expert_map = get_expert_map(location, page_num)
        # load up a game
        click(location)
        time.sleep(.2)
        click_hard()
        time.sleep(.5)
        click_standard()
        return expert_map, True

    # Check for symbol on expert page 2
    click_page_right()
    time.sleep(1)
    page_num += 1
    found_symbol, location = find_image('reference_images/bonus_rewards.png')
    if found_symbol:
        expert_map = get_expert_map(location, page_num)
        # load up a game
        click(location)
        time.sleep(.2)
        click_hard()
        time.sleep(.5)
        click_standard()
        return expert_map, True
    else:
        print('Reward symbol not found')
        return 'None', False


def get_expert_map(position, page_num):
    '''
    Get the expert map from the position of the bonus rewards symbol.

    :returns: list of actions (from action_scripts)
    '''
    global current_map
    # Expert Map names
    page_one = [['sanctuary_script', 'ravine_script', 'flooded_valley_script'],
                ['infernal_script', 'bloody_puddles_script', 'workshop_script']]
    page_two = [['quad_script', 'dark_castle_script', 'muddy_puddles_script'],
                ['ouch_script']]
    # dimensions of screen
    height = autoplayV2.screen_height
    width = autoplayV2.screen_width

    # indicies of map names
    xindex = None
    yindex = None

    if position[1] < height/3:
        yindex = 0 # tis in upper portion of screen
    else:
        yindex = 1 # symbol is in lower portion of screen

    if position[0] < width/2.5:
        xindex = 0 # left
    elif width/2.5 <= position[0] <= width-width/2.5:
        xindex = 1 # middle
    else:
        xindex = 2 # right

    if page_num == 1:
        expert_map = page_one[yindex][xindex]
    elif page_num == 2:
        expert_map = page_two[yindex][xindex]
    else:
        print('invalid page number in get_expert_map()')
        exit()
    print(expert_map)

    # Update current map (used for logging)
    current_map = expert_map

    # Update game_loop code to include sanctuary script
    if expert_map == 'sanctuary_script':
        autoplayV2.map_is_sanctuary = True
        autoplayV2.manual_rounds = True
    else:
        autoplayV2.map_is_sanctuary = False
        autoplayV2.manual_rounds = False

    # Convert expert_map string into variable and access the correct script
    expert_map_module = __import__('action_scripts.collection_scripts.' + expert_map, fromlist=[expert_map])
    action_list = getattr(expert_map_module, expert_map)

    return action_list


# region ------------- Clicking-Only Methods -----------------
def click(position):
    '''Click the desired position'''
    pyautogui.moveTo(position)
    pyautogui.click(position)

# region   Very simple click-one-position functions
def click_play():
    '''Click the play button'''
    pyautogui.moveTo(835, 930)
    pyautogui.click(835, 930)

def click_beginner():
    '''Click the beginner button'''
    pyautogui.moveTo(582, 981)
    pyautogui.click(582, 981)

def click_expert():
    '''Click the Expert button'''
    pyautogui.moveTo(1338, 976)
    pyautogui.click(1338, 976)

def click_page_right():
    '''Click the right arrow on the map selection screen'''
    pyautogui.moveTo(1642, 432)
    pyautogui.click(1642, 432)

def click_hard():
    '''Click the hard game mode'''
    pyautogui.moveTo(1296, 418)
    pyautogui.click(1296, 418)

def click_standard():
    '''Click the standard game mode'''
    pyautogui.moveTo(632, 587)
    pyautogui.click(632, 587)

def click_home():
    '''Click the home button after victory (or loss in chimps mode)'''
    pyautogui.moveTo(785, 836)
    pyautogui.click(785, 836)

def click_home_loss():
    '''Click the home button after loss (continue button exists)'''
    pyautogui.moveTo(703, 830)
    pyautogui.click(703, 830)

def click_victory_next():
    '''Click the next button after victory'''
    pyautogui.moveTo(939, 907)
    pyautogui.click(939, 907)

# endregion

def collect_event():
    '''Collect event rewards after beating a level'''
    # Click 'collect'
    pyautogui.moveTo(962, 683)
    pyautogui.click(962, 683)
    
    # Wait for animation
    time.sleep(3)

    # Rapidly click across the screen to collect rewards
    for i in range(30):
        x = 553 + i*30
        pyautogui.moveTo(x, 544)
        pyautogui.click(x, 544)
        time.sleep(.1)

    # Exit to home screen
    pyautogui.moveTo(81, 55)
    pyautogui.click(81, 55)

# endregion


def main():

    num_games = 25
    beat_level = False
    broken_log = []

    for i in range(num_games):
        # Launch game with the bonus rewards symbol
        expert_map, found = find_bonus_rewards_symbol()
        if found:
            # Beat the level
            beat_level = autoplayV2.game_loop(expert_map)
        else:
            print('Reward symbol not found, exitting program')
            exit()
        # log if we somehow didn't beat the level
        if beat_level == False:
            print('didnt beat level')
            broken_log.append(current_map)
            # Exit to main menu by pressing home button
            click_home_loss()
            time.sleep(.1)
            click_home() # shouldn't be needed, but it's there just in case
        else:
            # Exit to home after victory
            click_victory_next()
            time.sleep(1.5)
            click_home()
            time.sleep(1.5)
            
        time.sleep(5)
        # Collect event rewards if needed
        found_collection, _ = find_image('reference_images/collection_event.png')
        if found_collection:
            collect_event() 
        
        # Clear stored monkeys from previous level
        autoplayV2.monkey_dict.clear()

        # Show updated stats of session
        print(f'Number of games won: {i + 1 - len(broken_log)}')
        print('broken_log:')
        for item in broken_log:
            print(item) 

        time.sleep(2)

if __name__ == '__main__':
    main()
