import schedule
import time

def task():
    print("ughh abhi bhi kar raha hu")
schedule.every().monday.do(task)

schedule.every().wednesday.at("11:30:50").do(task)

schedule.every().hour.at(":30").do(task)

schedule.every(5).to(10).seconds.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)