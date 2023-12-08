import os

for i in range(1,11):
    file_name = 'file' + str(i) + '.txt'
    f = open(file_name, "w")
    f.close()