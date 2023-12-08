fpx=open("D:\Fifth Sem\Advance Python\Practical - Theory\exam mid sem\input.txt",'r')
fpy=open('D:\Fifth Sem\Advance Python\Practical - Theory\exam mid sem\output.txt','w+')
for line in fpx:
    fpy.write(line)
fpy.seek(0)
print(fpy.read())
fpx.close()
fpy.close()

with open("output.txt","w") as fp:
    fp.write("my first file\n")
    fp.write("this file\n\n")
    fp.write("contains three lines\n")
    fp.close()

with open("input.txt",'r') as file:
    file.seek(10)
    data=file.read(5)
    print(data)

with open('input.txt','rb') as file:
    file.seek(20)
    position=file.tell()
    print("Current position: ",position)
    data=file.read(10)
    new_position=file.tell()
    print("updated position: ", new_position) 