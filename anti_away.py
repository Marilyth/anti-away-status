import pyautogui
import time
from random import randint
import typer

def do_actions(distance: int = 600, left_click: bool = False, press_button: str = None, sleep_interval: int = 60, max_sleep_interval: int = None):
    while True:
        if distance > 0:
            x_direction = randint(-distance, distance)
            y_direction = randint(-distance, distance)

            pyautogui.moveRel(x_direction, y_direction, 1)
        
        if left_click:
            pyautogui.click()
        
        if press_button:
            pyautogui.press(press_button)

        time.sleep(randint(sleep_interval, max_sleep_interval if max_sleep_interval else sleep_interval))

if __name__ == "__main__":
    typer.run(do_actions)
