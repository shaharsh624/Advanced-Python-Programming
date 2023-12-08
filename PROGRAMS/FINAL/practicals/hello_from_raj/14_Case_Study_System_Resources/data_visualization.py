import numpy as np
import matplotlib.pyplot as plt
import csv

# Read data from the CSV file, skipping the header row
data = []
with open('resource_usage.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Skip the header row
    for row in reader:
        data.append(list(map(float, row)))

# Convert data to a NumPy array
data = np.array(data)

# Extract columns
timestamp, cpu_percent, memory_percent, disk_percent = data.T

# Calculate statistics
average_cpu = np.mean(cpu_percent)
average_memory = np.mean(memory_percent)
average_disk = np.mean(disk_percent)

# Create line plots
plt.figure(figsize=(10, 6))
plt.plot(timestamp, cpu_percent, label='CPU Usage (%)')
plt.plot(timestamp, memory_percent, label='Memory Usage (%)')
plt.plot(timestamp, disk_percent, label='Disk Usage (%)')

# Add labels and legend
plt.xlabel('Timestamp')
plt.ylabel('Usage (%)')
plt.legend()

# Show the plots
plt.show()

print(f'Average CPU Usage: {average_cpu:.2f}%')
print(f'Average Memory Usage: {average_memory:.2f}%')
print(f'Average Disk Usage: {average_disk:.2f}%')
