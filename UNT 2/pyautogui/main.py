import pyautogui as p
import time

copy_stite = r"C:/Users/harsh/OneDrive - pdpu.ac.in/HARSH/_STUDY MATERIAL/SEM 5/Advanced Python Programming/UNT 2/pyautogui/pyautogui-copy-file.txt"

paste_site = "https://docs.google.com/document/d/1r7UHu9BukC1YtCJAQCw11JXtNsKh_fOFgxgn1hTvlGw/edit?usp=sharing"

# Opening browser
p.hotkey('win')
p.sleep(2)
p.write('brave')
p.press('enter')
time.sleep(3)

# Entering site to copy
p.write(copy_stite)
time.sleep(1)
p.press('enter')

# Copying Data
time.sleep(2)
p.hotkey('ctrl', 'a')
p.hotkey('ctrl', 'c')
time.sleep(2)

# Opening Google Docs
p.hotkey('ctrl', 't')
time.sleep(5)
p.write(paste_site)
time.sleep(1)
p.press('enter')
time.sleep(3)

# Pasting the Data
p.hotkey('ctrl', 'shift', 'v')

time.sleep(1)
