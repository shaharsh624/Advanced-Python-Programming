class FileNotFoundError(Exception):
    def __init__(self, file_name):
        self.file_name=file_name

    def __str__(self):
        return f"File Not Found: {self.file_name}"
    

def read_file(file_name):
    try:
        with open(file_name) as file:
            content=file.read()
            print("File content: ", content)
    except IOError:
        raise FileNotFoundError(file_name)
    

if __name__=="__main__":
    try:
        file_name="D:\Fifth Sem\Advance Python\Practical - Theory\exam mid sem\inut.txt"
        read_file(file_name)
    except FileNotFoundError as e:
        print(f"Error occured: {e}")