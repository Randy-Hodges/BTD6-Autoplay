#usr bin shit
#
#
# Desc:
#
# TODO: fix the click() and position methods to work on other people's screens
#


import ctypes

import keyboard
import pyautogui

import playsound
import time
from PIL import Image, ImageGrab
from pytesseract import pytesseract
import numpy as np

from monkey_hotkeys import hotkeys
from ravine_script import script as rscript
from class_definitions import Monkey
from class_definitions import Action
print('------------------')


# region Initial Set-up
# Setting up tesseract
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract

# Variables to determine screenshot ranges (formed-from/affects tests done on my local computer)
test_scrn_width = 1920 #1536
test_scrn_height = 1080 #864

# Get screen size
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(f'Screensize: {screensize}')

# Define storage important to running a game
monkey_dict = {}
# endregion

def get_money():
    '''Extract money value using a small screenshot of the game'''
    # First indicator a screenshot is going to be taken
    # playsound.playsound(r"D:\randy\Audio\Sound Effects\The Nut Button - When Memes Become Reality.mp3")

    print_stats = False
    # Screenshot
    img = ImageGrab.grab(bbox = (int(320/test_scrn_width*int(screensize[0])), # left bound
                                int(10/test_scrn_height*int(screensize[1])), # upper bound
                                int(500/test_scrn_width*int(screensize[0])), # right bound
                                int(75/test_scrn_height*int(screensize[1]))  # lower bound
                            )
    )
    # img.show()
    img = np.asfarray(img)
    height = len(img)
    width = len(img[0])
    img.setflags(write=1)
    for loop1 in range(height):
        for loop2 in range(width):
            r,g,b = img[loop1,loop2]
            if sum([r,g,b]) < 700:
                img[loop1,loop2] = [0,0,0]

    img = Image.fromarray(np.uint8(img))
    # img.show()

    # Convert to text. (psm 6,7,8 seem to be best)
    text = pytesseract.image_to_string(img, config='--psm 7')
    if print_stats: print(f'Text:{text}')
    money = ''

    # Convert money text to number
    try:
        for char in text:
            if char.isdigit():
                money += char
        money = int(money)
        print(f'**********************money:{money}')
    except:
        if print_stats: print('money not recognized')
        money = -1

    return money


def get_round():
    '''Extract round value using a small screenshot of the game'''
    # First indicator a screenshot is going to be taken
    playsound.playsound(r"D:\randy\Audio\Sound Effects\The Nut Button - When Memes Become Reality.mp3")

    # Screenshot
    img = ImageGrab.grab(bbox = (int(1480/test_scrn_width*int(screensize[0])), # left bound
                                int(10/test_scrn_height*int(screensize[1])), # upper bound
                                int(1570/test_scrn_width*int(screensize[0])), # right bound
                                int(75/test_scrn_height*int(screensize[1]))  # lower bound
                            )
    )
    img.show()

    # 6,7,8 seem to be best
    text = pytesseract.image_to_string(img, config='--psm 7')
    print(f'Text:{text}')
    round = ''

    # Convert money text to number
    try:
        for char in text:
            if char.isdigit():
                round += char
        money = int(round)
        print(f'round:{round}')
    except:
        print('round not recognized')
        round = -1

    return round


def start():
    '''start the game/round'''
    pyautogui.press('space')
    pyautogui.press('space')


def do_action(action: Action) -> bool:
    '''Perform the given action. This function assumes there is enough money to do so.'''
    ####
    # Placing actions
    if action.type == 'place' or action.type == 'monkey':
        # check if monkey already in monkey_dict
        if action.name in monkey_dict:
            print(f'YO. Your duplicated a monkey name dude. Fix that please. Name:{action.name}')

        # add monkey to monkey_dict
        monkey_dict[action.name] = Monkey(position=action.position, name=action.name, mtype=action.action)

        act_name = action.action
        # Place monkey
        keyboard.press(hotkeys[act_name.title()].lower())
        keyboard.release(hotkeys[act_name.title()].lower())
        pyautogui.moveTo(action.position)
        pyautogui.click(action.position) 

        return True

    ####
    # Upgrading actions
    if action.type == 'upgrade':
        # Update stored monkey data
        monkey: Monkey
        monkey = monkey_dict[action.name]
        monkey.upgrade(int("".join(filter(str.isdigit, action.action))))

        # Click Monkey
        pyautogui.moveTo(monkey.position)
        pyautogui.click(monkey.position)
        time.sleep(.1)

        # Upgrade monkey
        pyautogui.press(hotkeys[action.action.title()])
        
        # Click away to reset gui
        pyautogui.moveTo(1600, 1400)
        pyautogui.click(1600, 1040)

        return True
    
    ####
    # Targeting actions
    if action.type == 'target':
        if action.action == 'Strong':
            # Find monkey
            monkey: Monkey
            monkey = monkey_dict[action.name]

            # Click monkey
            pyautogui.moveTo(monkey.position)
            pyautogui.click(monkey.position)
            print('done clicking')

            # Change targeting from first to strong
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('tab')
            time.sleep(.1)
            pyautogui.keyUp('ctrl')
            pyautogui.keyUp('tab')

            return True

        if action.action == 'First':
            # Find monkey
            monkey: Monkey
            monkey = monkey_dict[action.name]

            # Click monkey
            pyautogui.moveTo(monkey.position)
            pyautogui.click(monkey.position)

            # Change targeting from strong to first
            keyboard.press('tab')
            keyboard.release('tab')

            return True

    ####
    # Starting game
    if action.type == 'start':
        start()
        return True


    # if the actions failed, return False
    return False


def wait_till_victory():
    pass

def game_loop(script):
    '''Play through a game'''
    # Tell if something has gone wrong in the loop, maybe it isn't seeing the money correctly
    broken_counter = 0
    broken_thresh = 10000

    # To monitor script
    script_pos = 0
    action: Action
    action = script[script_pos]

    # To monitor gold  
    old_gold = 0
    old_gold_break = 0

    #### 
    # Main Loop
    while script_pos < len(script):
        broken_counter += 1

        # Get current money amount
        current_gold = get_money()
        # Account for a misread of the gold
        if current_gold > old_gold*3 and old_gold_break <= 2:
            old_gold_break += 1
            # print('old gold problem')
            continue
        else:
            old_gold = current_gold
            old_gold_break = 0

        # Do action if affordable
        if action.cost == None or action.cost <= current_gold:
            # Try to do the action (if it fails 3 times, return out of function)
            for _ in range(3):
                print(f'Performing action: {action.name} {action.action}')
                done = do_action(action)
                time.sleep(.1)
                if done:
                    script_pos += 1
                    action = script[script_pos]
                    print(f'Next action name: {action.name} {action.action}')
                    break
            else:
                print('action failed to complete 3 times, stopping game loop')
                return False

        if broken_counter > broken_thresh:
            print('Nothing has occurred within broken_thresh amount of loops. Something has probably gone wrong.')
            return False

        time.sleep(.5)

    # All actions have been completed, wait for game to end
    wait_till_victory()

# get_money()
# exit()

playsound.playsound(r"D:\randy\Audio\Sound Effects\The Nut Button - When Memes Become Reality.mp3")

game_loop(rscript)

            
        




