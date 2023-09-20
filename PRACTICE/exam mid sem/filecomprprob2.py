import zipfile
zipfilename="D:\Fifth Sem\Advance Python\Practical - Theory\exam mid sem\zippedfile.zip"

filestozip=['one.txt','two.txt']

try:
    with zipfile.ZipFile(zipfilename,'w',zipfile.ZIP_DEFLATED) as zipf:
        for filetozip in filestozip:
            zipf.write(filetozip)

    print(f"Files zipped into {zipfilename}")

except FileNotFoundError as e:
    print(f"Error: File not Found {e}")
except Exception as e:
    print(f"An error occurred: {e}")
