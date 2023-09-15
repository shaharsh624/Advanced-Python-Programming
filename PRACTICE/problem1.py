# Write a program to copy contain of file X.txt to Y.txt

# Method 1
f1 = open("X.txt", "r")
f2 = open("Y.txt", "w")
f2.write(f1.read())
f1.close()
f2.close()

# Method 2
f1 = open("X.txt", "r")
f2 = open("Y.txt", "w")
for line in f1.readlines():
    f2.write(line)
f1.close()
f2.close()

# Method 3
f1 = open("X.txt", "r")
f2 = open("Y.txt", "w")
for line in f1:
    f2.write(line)
f1.close()
f2.close()