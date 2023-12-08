import shutil

def copy_files(source, backup):
    try:
        shutil.copytree(source, backup)
        print(f"Backup from {source} to {backup} successful")
    except Exception as e:
        print(f"Error while copying: {e}")

if __name__ == "__main__":
    source_path = input("Enter the source path: ")
    backup_path = input("Enter the backup path: ")
    copy_files(source_path, backup_path)