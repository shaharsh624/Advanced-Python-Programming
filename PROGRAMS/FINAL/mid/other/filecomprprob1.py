import zipfile

zip_path="D:\Fifth Sem\Advance Python\Practical - Theory\exam mid sem\zippedfile.zip"

extract_folder="D:/Fifth Sem/Advance Python/Practical - Theory/exam mid sem/"

try:
    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        zip_file.extractall(extract_folder)

    print(f"files extracted to {extract_folder}")

except zipfile.BadZipFile as e:
    print(f"Error: Bad Zip File - {e}")
except FileNotFoundError as e:
    print(f"File not found:{e}")
except Exception as e:
    print(f"An error occurred: {e}")
