"""
Logic to keep screen awake
"""
import random
import time

import pyautogui


# TODO: add tweening, keyboard stop, safe termination
def caffeine(runtime: int = 0) -> None:
    """
    Keeps the screen awake for specifed duration
    """
    pyautogui.FAILSAFE = True
    SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

    def under_runtime() -> bool:
        """
        Check to keep running the program
        """
        if runtime == 0:
            return True

        curr_time = time.monotonic()
        return curr_time < end_time

    def move_mouse() -> None:
        """
        Moves mouse to random position on screen
        """
        pos_x = random.randint(0, SCREEN_WIDTH)
        pos_y = random.randint(0, SCREEN_HEIGHT)
        duration = random.randint(1, 5)

        try:
            pyautogui.moveTo(pos_y, pos_x, duration)
        except pyautogui.FailSafeException:
            quit()

    end_time = time.monotonic() + runtime
    while under_runtime():
        interval = random.randint(1, 5)
        interval_time = time.monotonic() + interval

        move_mouse()

        while time.monotonic() < interval_time:
            time.sleep(0.1)
