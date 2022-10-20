import pyautogui
import time
from random import randint

while True:
    current_position = pyautogui.position()
    x_direction = randint(-100, 100)
    y_direction = randint(-100, 100)

    pyautogui.moveRel(x_direction, y_direction, 1)
    time.sleep(5)
