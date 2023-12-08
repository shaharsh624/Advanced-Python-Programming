# import csv
# with open('csv_file.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# with open('csv_file.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     data = {}
#     for row in reader:
#         data[row['Name']] = int(row['Marks1']) + int(row['Marks2']) + int(row['Marks3'])

# with open('csv_output.csv', "w", newline="") as file:
#     fields = ["Name", "Sum"]
#     writer = csv.DictWriter(file, fieldnames=fields)
#     writer.writeheader()
#     for name, avg in data.items():
#         writer.writerow({"Name":name, "Sum":avg})


import csv
with open("csv_file.csv", "r") as fr:
    summary = {}
    reader = csv.DictReader(fr)
    for row in reader:
        print(row)
        name = row['Name']
        marks1 = int(row['Marks1'])
        marks2 = int(row['Marks2'])
        marks3 = int(row['Marks3'])
        score = [marks1, marks2, marks3]
        avg = round(sum(score) / len(score), 2)
        summary[name] = avg
    print(summary)

with open("csv_output.csv", "w", newline='') as fo:
    fieldnames = ['Name', 'Average']
    writer = csv.DictWriter(fo, fieldnames=fieldnames)
    writer.writeheader()
    for name, avg in summary.items():
        writer.writerow({"Name":name, "Average":avg})