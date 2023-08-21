import os
import shutil

# Make directory
os.mkdir("test1")

# Copy file to folder
shutil.copy("test1.py", "test1")

# Move file to folder
shutil.move("test1.py", "test1")

# List directories in folder
print(os.listdir("test1"))

