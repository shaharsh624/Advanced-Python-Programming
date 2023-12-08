''' Read mode '''
# file1 = open("test1.txt", "rb")
# read_content = file1.read()
# print(read_content)
# file1.close()

''' Write mode '''
# file2 = open("test1.txt", "w")
# file2.write("This is a test file.")
# file2.close()

''' Append mode '''
# file2 = open("test1.txt", "a")
# file2.write("\n" + "This is a test file.")
# file2.close()

''' r+ mode '''
# file1 = open("test1.txt", "r+")
# read_content = file1.read()
# print(read_content)
# file1.write(" This is a test file.")

# file1 = open("test1.txt", "r+")
# read_content_new = file1.read()
# print("New: ", read_content_new)
# file1.close()

''' Using open function '''
# with open("file1.txt", "w") as f:
#     f.write("Hello" + "\n" +  "world!")

''' Read Line '''
# with open("marks.txt", "r") as f:
#     i=0
#     while True:
#         i = i + 1
#         line = f.readline()
#         if not line:
#             break
#         m1 = line.split(",")[0]
#         m2 = line.split(",")[1]
#         print(f"Marks of student {i} in Maths : {m1}")
#         print(f"Marks of student {i} in Maths : {m2}")

''' Write Line '''
# with open("test2.txt", "w") as f:
#     lines = ["test 1\n", "test 2\n", "test 3"]
#     # f.writelines(lines)

#     lines2 = ["test 1", "test 2", "test 3"]
#     for line in lines2 :
#         f.write(line + "\n")

''' Seek Function '''
# Seek moves the cursor to the given location(num).
# with open("file1.txt", "r") as f:
#     f.seek(4)
#     data = f.read()
#     print(data)


''' Tell Function '''
# It shows where the cursor is due to seek().
# with open("file1.txt", "r") as f:
#     f.seek(4)
#     print(f.tell())


''' Truncate Function '''
# Declares size of files (in terms of numner of characters).
with open("file1.txt", "w") as f:
    f.write("Hello World how are you")
    f.truncate(4)