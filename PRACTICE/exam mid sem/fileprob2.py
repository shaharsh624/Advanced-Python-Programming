fp=open("D:\Fifth Sem\Advance Python\Practical - Theory\exam mid sem\input.txt")
reader=fp.read()
word=0
char=0
line=0
my_list={}
space=0
char_wo_space=0
for x in reader:
    char+=1
    if x==" ":
        word+=1
        space+=1
    elif x=="\n":
        word+=1
        line+=1
    elif x!=" ":
        char_wo_space+=1
    if x in my_list:
        my_list[x]+=1
    if x not in my_list:
        my_list[x]=1
    

print("word:", word)
print("char:",char)
print("space: ",space)
print("count with space:", char_wo_space)
print("line:",line)
print(my_list)

