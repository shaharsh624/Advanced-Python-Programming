import os

# os.mkdir("G7")
# os.mkdir("G8")
# os.mkdir("G9")

# g7 = ['1.txt', '2.txt']
# g8 = ['1.txt', '2.txt', '3.txt']
# g9 = ['2.txt', '3.txt', '4.txt']

# for file in g7:
#     with open (os.path.join("G7", file), 'w'):
#         pass

# for file in g8:
#     with open (os.path.join("G8", file), 'w'):
#         pass

# for file in g9:
#     with open (os.path.join("G9", file), 'w'):
#         pass


files_g7 = os.listdir("G7")
files_g8 = os.listdir("G8")
files_g9 = os.listdir("G9")

s = set()
s.add(files_g7)
s.add(files_g8)
s.add(files_g9)
s.intersection(s)

# for file1 in files_g7 :
#     for file2 in files_g8 :
#         if (file1 == file2):
#             common_files.append(file1)
# for file3 in files_g9:
#     if (file3 in common_files):
#         with open (os.path.join("G7", file3), 'r') as f:
#             line = f.read()
#             lines = line.split("\n")
#             print(lines[1])

    
