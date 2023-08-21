import os
import zipfile


def create_zip(files_to_zip, count):
    zip_filename = "Archive_" + str(count) + ".zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in files_to_zip:
            zipf.write(file)


def find_files():
    count = 0

    # Walking top-down from the root
    for file in os.listdir():
        if file.endswith('.zip'):
            count += 1

    return count


def main():
    n = int(input("Enter number of files to zip: "))
    files_to_zip = []
    for i in range(n):
        file = input("Enter file name with extension: ")
        files_to_zip.append(file)

    create_zip(files_to_zip, find_files())


if __name__ == "__main__":
    main()
