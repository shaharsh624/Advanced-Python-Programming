# Write a code to read file and give you summary of the file.

count_character = 0
count_word = 1
count_space = 0
count_line = 1
frequency_character = {}

f1 = open("file.txt", "r")
data = f1.read()

for x in data:
    if x == ' ':
        count_space += 1
        count_character += 1
        count_word += 1
    elif x == '\n':
        count_word += 1
        count_line += 1
    else:
        count_character += 1
        if x in frequency_character:
            frequency_character[x] += 1
        if x not in frequency_character:
            frequency_character[x] = 1
    
print("Words: ", count_word)
print("Characters with spaces: ", count_character)
print("Characters without spaces: ", count_character-count_space)
print("Spaces: ", count_space)
print("Lines: ", count_line)

f1.close()