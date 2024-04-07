
# MOUSE WIGGLER MINI PROJECT

# Mouse mover function **

import time
import pyautogui

def mouse_mover():
    pyautogui.moveTo(341, 921, 3)    # Moves the pointer to a starting point, duration of movement is 3 seconds (adjust accordingly)
    pyautogui.moveTo(1808, 897, 3)   # Moving pointer ...
    pyautogui.moveTo(341, 921, 3)    # Moves the pointer back to starting point, duration of movement is also 3 seconds

while True:
    # Adjust on how frequent the script runs (120 is in seconds)
    time.sleep(120)
    mouse_mover()
