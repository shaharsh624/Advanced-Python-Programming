class FileNotFoundError(Exception):
    def __init__(self,filename):
        self.filename=filename
    def __str__(self):
        return f"File not found: {self.filename}"
    
def read_file(filename):
    try:
        with open(filename) as file:
            content=file.read()
            print("File content: ", content)
    except IOError:
        raise FileNotFoundError(filename)
    
if __name__=="__main__":
    try:
        filename="D:\Fifth Sem\Advance Python\Practical - Theory\exam mid sem\inpu.txt"
        read_file(filename)
    except FileNotFoundError as e:
        print("File not found: ",e)