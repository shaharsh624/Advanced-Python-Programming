import csv
with open('csv_file.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)