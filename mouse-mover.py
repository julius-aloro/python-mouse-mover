
# MOUSE WIGGLER MINI PROJECT

# Mouse mover function **

import time
import pyautogui

def mouse_mover():
    pyautogui.moveTo(341, 921, 3)
    pyautogui.moveTo(1808, 897, 3)
    pyautogui.moveTo(341, 921, 3)

while True:
    time.sleep(120)
    mouse_mover()
