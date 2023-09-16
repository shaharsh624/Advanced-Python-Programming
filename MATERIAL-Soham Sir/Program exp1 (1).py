"""
drag mouse and copy
"""

import pyautogui
import time

def automate_mouse_actions():
    # Move the mouse to coordinates (500, 500)
    pyautogui.moveTo(500, 500, duration=1)

    # Simulate a left mouse button click
    pyautogui.click()

    # Move the mouse to coordinates (800, 300) and click
    pyautogui.moveTo(800, 300, duration=1)
    pyautogui.click()

if __name__ == "__main__":
    time.sleep(5)  # Wait for 5 seconds before starting
    automate_mouse_actions()

