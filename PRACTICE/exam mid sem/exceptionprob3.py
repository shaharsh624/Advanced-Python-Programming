try:
    fp=open("D:\Fifth Sem\Advance Python\Practical - Theory\exam mid sem\input.txt",'r')
    for line in fp:
        print(line)
finally:
    fp.close()