class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)


f = open('requirements.txt', 'r')
data = f.readline().lower()
data = data.replace('os:', "")
list = []
try:
    if data == "ubuntu\n":
        ver = f.readline().lower()
        ver = ver.replace('os_version:', '')
        if ver == str('18.02' + '\n'):
            python = f.readline().lower()
            python = python.replace('python:', '')
            if python == str('3.7' + '\n'):
                fianl = 'RUN apt-get install python' + python
                temp = 'RUN python3 -m pip install '
                temp2 = f.read().lower()
                temp2 = temp2.split('\n')
                for i in temp2:
                    list.append(temp + i)
                print(fianl)
                str = ''
                for i in list:
                    str = str + i
                    str = str + '\n'
                print(str)
        else:
            raise CustomException("OS Version not allowed.")
    else:
        raise CustomException("OS not allowed.")

except CustomException as e:
    print(e)
try:
    f2 = open('get.txt', 'a')
    f2.write('\n')
    f2.write(fianl)
    f2.write('\n')
    f2.write(str)
    f2.write('RUN echo "Compilation Successful"')
    f2.close()
except:
    pass
