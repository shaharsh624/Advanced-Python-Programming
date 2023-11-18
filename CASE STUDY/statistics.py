import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read the data
df = pd.read_csv("system_resource.csv", names=['timestamp', 'cpu_usage', 'memory_usage', 'disk_usage'])

# Overview of data
print(df.info())

timestamp = df['timestamp']
cpu_usage = df['cpu_usage']
memory_usage = df['memory_usage']
disk_usage = df['disk_usage']

mean_cpu = np.mean(cpu_usage)
mean_mem = np.mean(memory_usage)
mean_disk = np.mean(disk_usage)

median_cpu = np.median(cpu_usage)
median_mem = np.median(memory_usage)
median_disk = np.median(disk_usage)

std_cpu = np.std(cpu_usage)
std_mem = np.std(memory_usage)
std_disk = np.std(disk_usage)

print("\nStatistics of CPU Usage :: ")
print(f"\tMean: {mean_cpu}\n\tMedian: {median_cpu}\n\tStandard Deviation: {std_cpu}")

print("\nStatistics of Memory Usage :: ")
print(f"\tMean: {mean_mem}\n\tMedian: {median_mem}\n\tStandard Deviation: {std_mem}")

print("\nStatistics of Disk Usage :: ")
print(f"\tMean: {mean_disk}\n\tMedian: {median_disk}\n\tStandard Deviation: {std_disk}")


# Plot the data
plt.plot(timestamp, cpu_usage, label="CPU Usage")
plt.xlabel("Timestamp")
plt.ylabel("CPU Usage")
plt.title("CPU Usage over Time")
plt.legend()
plt.show()

plt.plot(timestamp, memory_usage, label="Memory Usage")
plt.xlabel("Timestamp")
plt.ylabel("Memory Usage")
plt.title("Memory Usage over Time")
plt.legend()
plt.show()

plt.plot(timestamp, disk_usage, label="Disk Usage")
plt.xlabel("Timestamp")
plt.ylabel("Disk Usage")
plt.title("Disk Usage over Time")
plt.legend()
plt.show()
