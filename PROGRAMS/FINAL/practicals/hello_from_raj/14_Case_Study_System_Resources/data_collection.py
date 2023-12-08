import csv
import time

import psutil
import schedule


def collect_data():
    timestamp = time.time()
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent

    with open('resource_usage.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([timestamp, cpu_percent, memory_percent, disk_percent])

if __name__ == '__main__':
    schedule.every(5).seconds.do(collect_data)
    
    i=0
    while i<10:
        schedule.run_pending()
        time.sleep(1)