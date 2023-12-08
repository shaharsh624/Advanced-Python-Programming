f1 = open("file.txt", "r")
for line in f1.readlines():
    word = line.split()
    print(word)
f1.close()

with open("file.txt", "a") as f2:
    f2.write("\n      Again writing Hello World")

# Left & Right Stripping 
with open("file.txt", "r+") as f3:
    word = f3.read()
    print(word)

    f3.write("\nHello Again")
