import schedule
import subprocess
import time


def job():
    subprocess.run(["python", "casestudy_collect_data.py"])


schedule.every(2).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)