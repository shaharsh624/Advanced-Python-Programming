"""
sample code for schedule lib
"""

import schedule
import time

def task1():
    print("Task 1 executed!")

def task2():
    print("Task 2 executed!")

def task3():
    print("Task 3 executed!")

if __name__ == "__main__":
    # Schedule task1 every 2 seconds
    schedule.every(2).seconds.do(task1)
    
    # Schedule task2 every 5 seconds
    schedule.every(5).seconds.do(task2)
    
    # Schedule task3 every day at 8:00 AM
    #schedule.every().day.at("08:00").do(task3)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

