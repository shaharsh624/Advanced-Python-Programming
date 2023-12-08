import shutil
import datetime
import time
from datetime import date
import os
import sys

today = date.today()
dateFormate = today.strftime("%d_%b_%Y")
currentTime = time.strftime("%H_%M_%S", time.localtime())

# print(dateFormate)
# print(type(currentTime))

srcFilePath = "E:\\Just Code\PDEU Labs\\5th Sem\\Advance_Python Lab\\Practical Classes\\Backup_Program\\example.txt"
destDir = f"E:\\Just Code\PDEU Labs\\5th Sem\\Advance_Python Lab\\Practical Classes\\Backup_Program\\New_Destination\\Backup_{dateFormate}_{currentTime}.txt"

shutil.copy2(srcFilePath, destDir)
print("Backup Successful")
