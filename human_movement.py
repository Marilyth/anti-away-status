import pyautogui
from random import randint, uniform
from pytweening import easeInOutQuad


def cubic_bezier(t, p0, p1, p2, p3):
    """Calculates the cubic bezier curve for the given points and time.
    """
    u = 1 - t
    tt = t * t
    uu = u * u
    uuu = uu * u
    ttt = tt * t
    return uuu * p0 + 3 * uu * t * p1 + 3 * u * tt * p2 + ttt * p3
    

def move_mouse_like_human(x: int, y: int, drag: bool = False):
    """Moves the mouse to the specified coordinates like a human would.
    """
    # Get current mouse position.
    current_mouse_position = pyautogui.position()

    # Add a little deviation to the target position.
    x += randint(-5, 5)
    y += randint(-5, 5)
    
    vector_x = x - current_mouse_position.x
    vector_y = y - current_mouse_position.y

    # Calculate the distance between the current mouse position and the target position.
    distance = ((x - current_mouse_position.x) ** 2 + (y - current_mouse_position.y) ** 2) ** 0.5
    duration = (distance + randint(-100, 100))

    x_path_bezier = [current_mouse_position.x, 
              (current_mouse_position.x + vector_x * uniform(0.4, 0.6)),
              current_mouse_position.x + vector_x * uniform(0.85, 0.9), 
              x]
    y_path_bezier = [current_mouse_position.y, 
              current_mouse_position.y + vector_y * uniform(0.4, 0.6), 
              current_mouse_position.y + vector_y * uniform(0.85, 0.9), 
              y]
    
    # Add a little deviation to the path in points 1 and 2, depending on their distance from the previous point.
    for i in range(1, 3):
        x_distance = (x_path_bezier[i] - x_path_bezier[i - 1])
        y_distance = (y_path_bezier[i] - y_path_bezier[i - 1])

        x_path_bezier[i] += uniform(-x_distance / 2, x_distance / 2)
        y_path_bezier[i] += uniform(-y_distance / 2, y_distance / 2)

    steps = int(duration // 10)
    line_progress = [easeInOutQuad(t / steps) for t in range(steps)]
    
    x_path = [cubic_bezier(t_i, x_path_bezier[0], x_path_bezier[1], x_path_bezier[2], x_path_bezier[3]) for t_i in line_progress]
    y_path = [cubic_bezier(t_i, y_path_bezier[0], y_path_bezier[1], y_path_bezier[2], y_path_bezier[3]) for t_i in line_progress]

    # Update mouse position every 10 ms.
    previous_pause = pyautogui.PAUSE
    pyautogui.PAUSE = 0.01

    # Move the mouse to the target positions along the path.
    for x, y in zip(x_path, y_path):
        if drag:
            pyautogui.dragTo(x, y)
        else:
            pyautogui.moveTo(x, y)
    
    # Reset delay.
    pyautogui.PAUSE = previous_pause

if __name__ == "__main__":
    # Draw the house of the mouse.
    for i in range(3):
        move_mouse_like_human(1000, 700, drag=False)
        move_mouse_like_human(1000, 500, drag=True)
        move_mouse_like_human(1200, 300, drag=True)
        move_mouse_like_human(1400, 500, drag=True)
        move_mouse_like_human(1400, 700, drag=True)
        move_mouse_like_human(1000, 700, drag=True)
        move_mouse_like_human(1400, 500, drag=True)
        move_mouse_like_human(1000, 500, drag=True)
        move_mouse_like_human(1400, 700, drag=True)
