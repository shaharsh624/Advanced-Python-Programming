class FileNotFoundError(Exception):
    def __init__(self, file):
        self.file = file
    def __str__(self):
        return f"File not found: {self.file}"

class NullData(Exception):
    def __init__(self):
        return f"NaN data found"

def read_file(file):
    try:
        with open(file, "r") as f:
            content = f.read()            
            print(content)
    except NullData:
        raise NullData()
    except IOError:
        raise FileNotFoundError(file)

if __name__ == "__main__":
    try:
        read_file("example.txt")
    except FileNotFoundError as e:
        print(f"Error occurred: {e}")