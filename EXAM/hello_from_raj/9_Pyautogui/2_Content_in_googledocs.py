import time

import pyautogui

text = "Name: Raj Randive, Roll No: 21BCP378.  This is something written, and this paragraph has to be written in google docs using pyautogui library. So i am writing anything just to paste it to the google docs.\n"

pyautogui.press("win")
time.sleep(0.5)
pyautogui.write("Chrome")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.press("\t")
pyautogui.press("enter")

time.sleep(1)
pyautogui.write("https://docs.google.com/document/u/0/create?usp=docs_home&ths=true")
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(2)
pyautogui.write(text)


# Check on this link whether the content is written or Not:
# https://docs.google.com/document/d/1Cb607Vz-VJ3xNclypijfG6V_mY91JqPDXv-WJItNUrY/edit
