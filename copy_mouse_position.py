import pyautogui
import pyperclip
import keyboard

print('Running copy_mouse_position.py. Press the \'insert\' key to copy mouse position.')
print('Press ctrl + c while in the terminal window to exit.')
while True:
    keyboard.wait('insert')
    x, y = pyautogui.position()
    pyperclip.copy(str(x) + ', ' + str(y))   
    print(f'insert was pressed! Copied mouse position ({str(x)}, {str(y)}) to keyboard. Press ctrl + c while in the terminal window to exit. Waiting again...')
    

# pyautogui.displayMousePosition()