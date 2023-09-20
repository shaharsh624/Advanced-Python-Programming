class FileNotFoundError(Exception):
    def __init__(self,filename):
        self.filename=filename
    def __str__(self):
        return f"File Not Found: {self.filename}"
    
class InvalidInputData(Exception):
    def __init__(self, message):
        self.message=message
    def __str__(self):
        return f"Invalid message: {self.message}"
    
class DiskSpaceFullError(Exception):
    def __init__(self,message):
        self.message=message
    def __str__(self):
        return f"Disk Space Full: {self.message}"
    
def read_input_file(filename):
    try:
        with open(filename) as file:
            content= file.read()
        return content
    except FileNotFoundError:
        raise FileNotFoundError(filename)
    except Exception as e:
        raise InvalidInputData(f"Error reading input file: {str(e)}")
    

def process_text_data(content):
    word=0
    list={}
    try:
        if "invalid_data" in content:
            raise InvalidInputData(f"invalid data error")
        #count words
        for c in content:
            if c==" " or c=="\n": 
                word +=1
            
            if c in list:
                list[c]+=1
            else:
                list[c]=1
        
        processed_data = f"Word Count: {word}\nCharacter Frequencies:\n"
        for char, freq in list.items():
            processed_data += f"{char}: {freq}\n"

        return processed_data
    except Exception as e:
        raise InvalidInputData(f"Error processing the data: {str(e)}")
    
    
def write_output_file(output_path, processed_data):
    try:
        with open(output_path, 'w') as file:
            file.write(processed_data)
        return "File written successfully"
    except FileNotFoundError:
        raise FileNotFoundError(output_path)
    except IOError:
        raise DiskSpaceFullError("Disk full unable to write output file")
    except Exception as e:
        raise InvalidInputData(f"Error writing output file: {str(e)}")
    
if __name__=="__main__":
    try:
        filename="D:\Fifth Sem\Advance Python\Practical - Theory\exam mid sem\input.txt"
        input_data=read_input_file(filename)
        processed_data=process_text_data(input_data)
        output_path="D:\Fifth Sem\Advance Python\Practical - Theory\exam mid sem\output.txt"
        write_output_file(output_path, processed_data)

        print("text processing and file writing completed successfully")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except InvalidInputData as e:
        print(f"Error: {e}")
    except DiskSpaceFullError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unhandled error: {str(e)}")


