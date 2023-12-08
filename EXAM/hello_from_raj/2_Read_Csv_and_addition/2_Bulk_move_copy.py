import os
import shutil


def move_files(source_folder, destination_folder):
    files = os.listdir(source_folder)

    for f in files:
        source_file_path = os.path.join(source_folder, f)
        destination_file_path = os.path.join(destination_folder, f)
        if (int(f[0]) % 2 == 0):
            shutil.move(source_file_path, destination_file_path)
        else:
            shutil.copy(source_file_path, destination_file_path)


source_folder = "E:/Just Code/PDEU Labs/Advance_Python/Practical Classes/1_2/Folder1"
destination_folder = "E:/Just Code/PDEU Labs/Advance_Python/Practical Classes/1_2/Folder2"

move_files(source_folder, destination_folder)
