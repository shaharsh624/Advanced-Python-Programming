# Generate the CSV file using pyautogui based on given data in txt file and generate the analysis report using pyautogui in txt/csv file.
# Name: Raj Randive
# Roll Number: 21BCP378

import csv
import time

import pandas as pd
import pyautogui

pathSave = "folder1"

# Read data from the provided text file
data = []
with open("data.txt", "r") as file:
    lines = file.readlines()
    for line in lines[1:]:  # Skip the header row
        row = line.strip().split(",")
        data.append(row)

# Create a CSV file from the data
csvFilename = "data.csv"
with open(csvFilename, "w", newline="") as csvfile:
    csvWriter = csv.writer(csvfile)
    csvWriter.writerow(
        ["No", "Customer Name", "Customer Id", "Food Id", "Food Name", "Food Review"]
    )
    csvWriter.writerows(data)

# Load the CSV data into a Pandas DataFrame for analysis
df = pd.read_csv(csvFilename)

# Generate an analysis report (example: count of food items)
analysisReport = df["Food Name"].value_counts()

# Save the analysis report to a text file
analysisReportFilename = "analysis_report.txt"
analysisReport.to_csv(analysisReportFilename, header=True, index=True)

# Use PyAutoGUI to generate the report
pyautogui.hotkey("win", "r")  # Opens the Run dialog
time.sleep(1)
pyautogui.write("notepad")  # Opens Notepad
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.write(analysisReportFilename)
time.sleep(2)
pyautogui.press("enter")
time.sleep(1)
pyautogui.write(analysisReport.to_string())
time.sleep(2)

# Close Notepad and save the report
pyautogui.hotkey("ctrl", "s")
time.sleep(2)
for i in range(9):
    pyautogui.press("tab")
    time.sleep(1)
time.sleep(2)
pyautogui.press("enter")
pyautogui.write(pathSave)
pyautogui.press("enter")
time.sleep(1)
for i in range(5):
    pyautogui.press("tab")
    time.sleep(1)
time.sleep(2)
pyautogui.write(analysisReportFilename)
pyautogui.press("enter")
time.sleep(3)

# Close Notepad
pyautogui.hotkey("alt", "f4")
