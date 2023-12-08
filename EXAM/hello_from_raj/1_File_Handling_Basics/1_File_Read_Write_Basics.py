# ----------------- READ -----------------
# f = open("file1.txt", "r")
# for x in f:
#     print(x)

# ----------------- WRITE -----------------
# f1 = open("file1.txt", "w")
# f1.write("This is overwritten text.")
# f1.write("Also allows multiple lines")

# ----------------- rb -----------------
# f2 = open("file1.txt", "rb")
# file_info = f2.read()
# f2.close()
# print ("Name of the file: ", f2.name)
# print ("Opening mode : ", f2.mode)
# print(file_info)

# ----------------- r+ -----------------
# f3 = open("file1.txt", "r+")
# content = f3.read()
# print(content)

# ----------------- wb+ -----------------
# f3 = open("file1.txt", "wb+")
# content = f3.read()
# print(content)

# ----------------- a -----------------
# f3 = open("file1.txt", "a")
# f3.write(" something appended")


# ----------------- a+ -----------------
f3 = open("file1.txt", "a+")
content = f3.read()
print(content)