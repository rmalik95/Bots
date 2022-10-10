import pyautogui
from time import sleep
import random

first_click = pyautogui.click(182, 622)
unmatch_btn = pyautogui.click(1172, 866)
confirm_btn = pyautogui.click(717, 528)

while True:
    pyautogui.click(182, 622)
    random_sleep = random.random() * 5
    sleep(random_sleep)
    pyautogui.click(1172, 866)
    random_sleep = random.random() * 5
    sleep(random_sleep)
    pyautogui.click(717, 528)
    random_sleep = random.random() * 5
    sleep(random_sleep)
