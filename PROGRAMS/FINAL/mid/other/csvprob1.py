import csv

input_file = "csv1.csv"
output_file = "csv2.csv"

student_grades = {}

with open(input_file, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row["Name"]
        math_score = int(row["Maths"])
        science_score = int(row["Science"])
        english_score = int(row["English"])
        score = [math_score, science_score, english_score]
        average_score = sum(score) / len(score)
        student_grades[name] = average_score

with open(output_file, "w", newline="") as csvfile:
    fieldnames = ["Name", "Average"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for name, average in student_grades.items():
        writer.writerow({"Name": name, "Average": average})

print("Success")
