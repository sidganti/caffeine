"""
Logic to keep screen awake
"""
import random
import time
import threading
import sys

import pyautogui
from pynput import keyboard


class _Caffiene:
    """
    Internal class to encapsulate data
    """
    def __init__(self, runtime) -> None:
        self.runtime = runtime

        # keyboard listener initialization
        self._key_listener = keyboard.Listener(
            on_press=self._key_pressed,
            suppress=True
        )
        self._key_listener.daemon = True

        # pyautogui initialization
        pyautogui.FAILSAFE = True
        self._SCREEN_WIDTH, self._SCREEN_HEIGHT = pyautogui.size()
        self._TWEENING_FUNCTIONS = [
            pyautogui.easeInQuad,
            pyautogui.easeOutQuad,
            pyautogui.easeInOutQuad,
            pyautogui.easeInBounce,
            pyautogui.easeInElastic
        ]

    def run(self):
        """
        Starts background threads and main logic
        """
        return self.start()

    def start(self):
        """
        Starts background threads and main logic
        """
        self._key_listener.start()

        end_time = time.monotonic() + self.runtime
        while self._under_runtime(end_time):
            interval = random.randint(5, 10)
            interval_time = time.monotonic() + interval

            mouse_thread = threading.Thread(target=self._move_mouse)
            mouse_thread.daemon = True
            mouse_thread.start()

            while time.monotonic() < interval_time and self._under_runtime(end_time):
                if not self._key_listener.is_alive():
                    self.stop()

                time.sleep(0.01)

    def _under_runtime(self, end_time: float) -> bool:
        """
        Check to keep running the program
        """
        if self.runtime == 0:
            return True

        curr_time = time.monotonic()
        return curr_time < end_time

    def _move_mouse(self) -> None:
        """
        Moves mouse to random position on screen
        """
        pos_x = random.randint(0, self._SCREEN_WIDTH)
        pos_y = random.randint(0, self._SCREEN_HEIGHT)
        duration = random.randint(1, 5)
        tween = random.choice(self._TWEENING_FUNCTIONS)

        try:
            pyautogui.moveTo(pos_y, pos_x, duration, tween)
        except pyautogui.FailSafeException:
            pass

    def _key_pressed(self, key):
        """
        Wrapper to terminate instance from key_listener
        """
        self.stop()

    def stop(self) -> None:
        """
        Safely terminates instance
        """
        sys.exit()


"""TODO:
add hotcorner support
add cli running indicator
"""
def caffeine(runtime: int = 0) -> None:
    """
    Keeps the screen awake for specifed duration
    """
    caff_job = _Caffiene(runtime)
    try:
        caff_job.run()
    except KeyboardInterrupt:
        sys.exit()
