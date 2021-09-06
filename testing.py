import ctypes

import keyboard
from numpy.core.numeric import Inf
import pyautogui

import playsound
import time
from PIL import Image, ImageGrab
from pytesseract import pytesseract
import numpy as np
import pyautogui

pyautogui.click([500,500])
exit()

# Variables to determine screenshot ranges (formed-from/affects tests done on my local computer)
test_scrn_width = 1920 
test_scrn_height = 1080 

# Get screen size
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

img = ImageGrab.grab(bbox = (int(170/test_scrn_width*int(screensize[0])), # left bound
                        int(1020/test_scrn_height*int(screensize[1])), # upper bound
                        int(210/test_scrn_width*int(screensize[0])), # right bound
                        int(1060/test_scrn_height*int(screensize[1]))  # lower bound
                    )
)
img.show()
img = np.asfarray(img)
height = len(img)
width = len(img[0])
img.setflags(write=1)
total = 0
n = height*width
for loop1 in range(height):
    for loop2 in range(width):
        r,g,b = img[loop1,loop2]
        total += r
mean = total/n
print(f'mean: {mean}')
