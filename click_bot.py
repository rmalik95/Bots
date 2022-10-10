import sys
import pyautogui
from time import sleep
import random

l_button = pyautogui.position(972, 759)
d_button = pyautogui.position(827, 759)
odds = 0.87

while True:
    if random.random() < odds:
        pyautogui.click(972, 759)
    else:
        pyautogui.click(827, 759)

    try:
        random_sleep = random.random() * 5
        sleep(random_sleep)
    except:
        print('Exiting the application')
        sys.exit()
