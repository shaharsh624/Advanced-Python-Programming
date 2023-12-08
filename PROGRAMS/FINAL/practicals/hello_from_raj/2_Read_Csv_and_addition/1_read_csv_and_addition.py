data = []
with open("E:/Just Code/PDEU Labs/Advance_Python/Practical Classes/1_2/file.csv") as pt:
    for line in pt:
        values = line.rstrip().split(',')
        int_values = [int(val) for val in values]
        sum_value = sum(int_values)
        int_values.append(sum_value)
        data.append(int_values)


for row in data:
    print(row)
