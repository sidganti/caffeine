import pyautogui
import time
import random

# TODO: argparse/click

if __name__ == '__main__':
    SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

    # TODO: have duration param
    while True:
        pos_x = random.randint(0, SCREEN_WIDTH)
        pos_y = random.randint(0, SCREEN_HEIGHT)

        pyautogui.moveTo(pos_y, pos_x)

        time.sleep(1) # TODO: have interval param
