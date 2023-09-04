# Screen size: 1920x1080
# Google Docs - right side
# Code editor - left side

import pyautogui
import time

copy_x, copy_y = 300, 300
pyautogui.click(copy_x, copy_y)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
paste_x, paste_y = 1200, 500
pyautogui.click(paste_x, paste_y)
pyautogui.hotkey('ctrl', 'shift', 'v')

time.sleep(1)
