# Analysis of System Resource Usage

import os
import psutil
import csv
import datetime
import logging

timestamp = datetime.datetime.now()

# CPU Usgae
cpu_usage = psutil.cpu_percent(1)

# Memory Usage
process = psutil.Process(os.getpid())
mem_usage = process.memory_percent()

# Disk Usage
disk_usage = psutil.disk_usage('/').percent

row = {'timestamp': timestamp, 'cpu_usage': cpu_usage, 'memory_usage': mem_usage, 'disk_usage': disk_usage}
with open('system_resource.csv', 'a', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=row.keys())
    writer.writerow(row)

logging.basicConfig(filename='system_resource.log', level=logging.DEBUG)
logging.debug(f"{timestamp} | {cpu_usage} | {mem_usage} |{disk_usage}")
