"""
Logic to keep screen awake
"""
import random
import time
import threading

import pyautogui
from pynput import keyboard

"""TODO:
prevent more than one thread existing at a time [maybe time how long a thread takes]
make sure program does run not longer than specified [try raising exceptions to quit threads (specifically for mouse_thread)],
convert to class,
replace quit with sys.exit
"""
def caffeine(runtime: int = 0) -> None:
    """
    Keeps the screen awake for specifed duration
    """
    pyautogui.FAILSAFE = True
    SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
    TWEENING_FUNCTIONS = [
        pyautogui.easeInQuad,
        pyautogui.easeOutQuad,
        pyautogui.easeInOutQuad,
        pyautogui.easeInBounce,
        pyautogui.easeInElastic
    ]

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
        print('thread registered', time.monotonic())
        pos_x = random.randint(0, SCREEN_WIDTH)
        pos_y = random.randint(0, SCREEN_HEIGHT)
        duration = random.randint(1, 5)
        tween = random.choice(TWEENING_FUNCTIONS)
        print('duration', duration)

        try:
            pyautogui.moveTo(pos_y, pos_x, duration, tween)
        except pyautogui.FailSafeException:
            print('killed by mouse')
        print('thread killed', time.monotonic())
        quit()

    def key_pressed(key) -> None:
        listener.stop()

    listener = keyboard.Listener(
        on_press=key_pressed,
        suppress=True
    )
    listener.daemon = True
    listener.start()

    end_time = time.monotonic() + runtime
    while under_runtime():
        interval = random.randint(5, 10)
        print('interval', interval)
        interval_time = time.monotonic() + interval

        # move_mouse()
        mouse_thread = threading.Thread(target=move_mouse)
        mouse_thread.daemon = True
        mouse_thread.start()

        while time.monotonic() < interval_time and under_runtime():
            if not listener.is_alive():
                print('killed by key')
                quit()
            # if not mouse_thread.is_alive():
            #     print('killed by mouse')
            #     quit()
            time.sleep(0.1)
        else:
            mouse_thread.join()
    else:
        print('killed by time')
        quit()
