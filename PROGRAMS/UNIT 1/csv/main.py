import csv
percentage = {}
with open('data.csv', newline='') as file:
    reader = csv.reader(file)
    index = 0
    for row in reader:
        if (row[0] != "Name"):
            percentage[row[0]] = (int(row[2]) + int(row[3]) + int(row[4]))/3
print(percentage)

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in reader:
        writer.writerow([])