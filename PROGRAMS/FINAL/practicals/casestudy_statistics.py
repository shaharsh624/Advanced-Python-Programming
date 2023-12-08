import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('system_data.csv', names=["TIME", "CPU", "DISK", "MEMORY"])

time = data["TIME"]
cpu = data["CPU"]
disk = data["DISK"]
memory = data["MEMORY"]

print("Average of CPU Usage: ", np.average(cpu))
print("Mean of DISK Usage: ", np.mean(disk))
print("Median of MEMORY Usage: ", np.median(memory))

plt.plot(time, cpu, label="CPU Usage")
plt.xlabel("Time")
plt.ylabel("CPU Usage")
plt.title("CPU Time Series")
plt.legend()
plt.show()
