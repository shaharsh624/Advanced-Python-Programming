import os
import csv
import psutil
import datetime
import logging


def get_system_data():
    cpu_usage = psutil.cpu_percent(1)
    disk_usage = psutil.disk_usage("/").total
    memory_usage = psutil.Process(os.getpid()).memory_percent()
    timestamp = datetime.datetime.now()
    system_data = {"timestamp": timestamp, "cpu_usage": cpu_usage, "disk_usage": disk_usage,
                   "memory_usage": memory_usage}

    with open("system_data.csv", "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=system_data.keys())
        writer.writerow(system_data)

    logging.basicConfig(level=logging.DEBUG, filename='system_resource.log')
    logging.debug(
        f"{timestamp} | {cpu_usage} | {disk_usage} | {memory_usage}")


get_system_data()
