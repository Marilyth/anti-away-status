import pyautogui
import time
from random import randint
import typer
from screeninfo import get_monitors

def do_actions(distance: int = 540, left_click: bool = False, press_button: str = None, sleep_interval: int = 60, max_sleep_interval: int = None):
    pyautogui.FAILSAFE = False

    # Determine current monitor.
    mouse_position = pyautogui.position()
    current_monitor = None
    for monitor in get_monitors():
        if monitor.x <= mouse_position.x and monitor.x + monitor.width >= mouse_position.x \
        and monitor.y <= mouse_position.y and monitor.y + monitor.height >= mouse_position.y:
            current_monitor = monitor
            break

    distance = min(distance, min(current_monitor.height // 2, current_monitor.width // 2))

    print(f"Starting actions:\n{current_monitor=}\n{mouse_position=}\n{distance=}\n{left_click=}\n{press_button=}\n{sleep_interval=}\n{max_sleep_interval=}")

    while True:
        if distance > 0:
            mouse_position = pyautogui.position()

            x_direction = randint(-distance, distance)

            # Pick a y such that it forms a radius of distance with x_direction.
            y_distance = (distance ** 2 - x_direction ** 2) ** 0.5
            y_direction = y_distance * ((-1) ** (randint(0, 1)))

            # If directions move outside of screen, inverse them.
            if x_direction + mouse_position.x > (current_monitor.x + current_monitor.width) or x_direction + mouse_position.x < current_monitor.x:
                x_direction *= -1
            if y_direction + mouse_position.y > (current_monitor.y + current_monitor.height) or y_direction + mouse_position.y < current_monitor.y:
                y_direction *= -1

            pyautogui.moveRel(x_direction, y_direction, 1)
        
        if left_click:
            pyautogui.click()
        
        if press_button:
            pyautogui.press(press_button)

        time.sleep(randint(sleep_interval, max_sleep_interval if max_sleep_interval else sleep_interval))

if __name__ == "__main__":
    typer.run(do_actions)
