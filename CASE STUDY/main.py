import subprocess
import schedule
import time

def job():
    subprocess.run(["python", "collect_data.py"])

schedule.every(2).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
