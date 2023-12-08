# Zip Files
from zipfile import ZipFile
import os

directory = 'Practical Classes/Practical_4/folder1'
filePaths = []

for root, directories, files in os.walk(directory):
    for filename in files:
        path = os.path.join(root, filename)
        filePaths.append(path)

print("Following files will be zipped: ")
for fileName in filePaths:
    print(fileName)

with ZipFile('E:/Just Code/PDEU Labs/5th Sem/Advance_Python Lab/Practical Classes/Practical_4/myFiles.zip', 'w') as zip:
    # writing each file one by one
    for file in filePaths:
        zip.write(file)

print('All files zipped successfully!')
