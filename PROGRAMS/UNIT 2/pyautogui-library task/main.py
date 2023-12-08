import csv
import pandas as pd
import pyautogui
import time


path_to_save = "C:/Users/harsh/OneDrive - pdpu.ac.in/HARSH/_STUDY MATERIAL/SEM 5/Advanced Python Programming/UNT 2/pyautogui-library task"

# Read data from the provided text file
data = []
with open('UNT 2\pyautogui-library task\data.txt', 'r') as file:
    lines = file.readlines()
    for line in lines[1:]:  # Skip the header row
        row = line.strip().split(',')
        data.append(row)

# Create a CSV file from the data
csv_filename = 'UNT 2\pyautogui-library task\data.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["No", "Customer Name", "Customer Id", "Food Id", "Food Name", "Food Review"])
    csv_writer.writerows(data)

# Load the CSV data into a Pandas DataFrame for analysis
df = pd.read_csv(csv_filename)

# Generate an analysis report (example: count of food items)
analysis_report = df['Food Name'].value_counts()

# Save the analysis report to a text file
analysis_report_filename = 'analysis_report.txt'
analysis_report.to_csv(analysis_report_filename, header=True, index=True)

# Use PyAutoGUI to generate the report
pyautogui.hotkey('win', 'r')  # Opens the Run dialog
time.sleep(1)
pyautogui.write('notepad')    # Opens Notepad
pyautogui.press('enter')
time.sleep(1)
pyautogui.write(analysis_report_filename)
time.sleep(2)
pyautogui.press('enter')
pyautogui.write(analysis_report.to_string())
time.sleep(2)

# Close Notepad and save the report
pyautogui.hotkey('ctrl', 's')
time.sleep(2)
for i in range(9):
    pyautogui.press('tab')
    time.sleep(1)
time.sleep(2)
pyautogui.press('enter')
pyautogui.write(path_to_save)
pyautogui.press('enter')
time.sleep(1)
for i in range(5):
    pyautogui.press('tab')
    time.sleep(1)
time.sleep(2)
pyautogui.write(analysis_report_filename)
pyautogui.press('enter')
time.sleep(3)

# Close Notepad
pyautogui.hotkey('alt', 'f4')
