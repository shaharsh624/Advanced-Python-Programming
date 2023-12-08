import time

import pyautogui

pyautogui.press("win")
pyautogui.write("Notepad")
pyautogui.press("enter")
time.sleep(1)

# Type a message and save it​
pyautogui.write("Hello, world!")
pyautogui.hotkey("ctrl", "s")
