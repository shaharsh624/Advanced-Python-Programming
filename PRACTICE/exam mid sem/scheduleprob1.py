import schedule
import time

def task():
    print("ha ha kar raha hu...")

#execute job at every 5 sec, min, hour, days, week
schedule.every(5).seconds.do(task)
schedule.every(5).minutes.do(task)
schedule.every(5).hours.do(task)
schedule.every(5).days.do(task)
schedule.every(5).weeks.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)
