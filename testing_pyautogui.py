from re import M
import pyautogui
import time 
import pyperclip
import keyboard

print('Running pyautogui test. Press the \'insert\' key to upgrade.')
print('Press ctrl + c while in the terminal window to exit.')
count = 0
while True:
    count += 1
    print(f'count: {count} ', end='')
    keyboard.wait('insert')
    pyautogui.keyDown('alt')
    pyautogui.keyDown('tab')
    time.sleep(.1)
    pyautogui.keyUp('alt') 
    pyautogui.keyUp('tab') 
    print(f'insert was pressed! Press ctrl + c while in the terminal window to exit. Waiting again...')
    

# print('starting| ', end='')
# time.sleep(2)
# # Space
# print(" 3 spaces: ", end='')
# pyautogui.press('|')
# pyautogui.press('space')
# pyautogui.press('space')
# pyautogui.press('space')
# # Tab
# print(" 1 tab:", end='')
# pyautogui.press('|')
# pyautogui.keyDown('tab')
# time.sleep(.1)
# pyautogui.keyUp('tab')
# # Upgrades
# print(" upgrades:", end='')
# pyautogui.press('|')
# pyautogui.press(',')
# pyautogui.press('.')
# pyautogui.press('/')
