import pyautogui
import time

def keep_awake():
    while True:
        # Move the mouse slightly
        pyautogui.moveRel(0, 1, duration=0.1)  # Move mouse 1 pixel down
        pyautogui.moveRel(0, -1, duration=0.1)  # Move mouse 1 pixel up
        # Wait for 10 minutes
        time.sleep(6)

if __name__ == "__main__":
    keep_awake()
