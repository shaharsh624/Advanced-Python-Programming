# // Unzip
import os
import zipfile

back_up = os.listdir(
    "E:/Just Code/PDEU Labs/5th Sem/Advance_Python Lab/Practical Classes/Practical_4/folder1")

i = 1
for f in back_up:
    print(str(i) + ") " + f)
    i = i + 1

n = int(input("Enter number of file to be unzipped: "))
with zipfile.ZipFile(back_up[n-1], 'r') as zipf:
    zipf.extractall("backup")
