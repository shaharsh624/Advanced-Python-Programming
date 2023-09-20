import subprocess 
import shutil
import os

def copy_files(source, backup):
    try:
        # Check if the source is a file
        if os.path.isfile(source):
            shutil.copy(source, backup)
            print(f"Backup from {source} to {backup} successful")
        else:
            print(f"Source {source} is not a valid file.")
    except Exception as e:
        print(f"Error while copying: {e}")

source="D:\Fifth Sem\Advance Python\Practical - Theory\exam mid sem\input.txt"
backup=[
    "D:/Fifth Sem/Advance Python/Practical - Theory/exam mid sem/csv",
    "D:/Fifth Sem/Advance Python/Practical - Theory/exam mid sem/orders",
    "D:/Fifth Sem\Advance Python/Practical - Theory/exam mid sem/backup"
]


processes=[]

for backup_folder in backup:
    process=subprocess.Popen(
        ["python","-c",f"import sys; sys.path.insert(0,'{source}');import backup_script;"'{source}'";"'{backup_folder}'";backup_script.copy_files('{source}','{backup_folder}')"]
    )
    processes.append(process)

for process in processes:
    process.wait()
print("all backup done")

