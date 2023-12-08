import time
from threading import Thread


# a custom function that blocks for a moment
def task1(sleep_time, message):
    # block for a moment
    # display a message
    for i in range(10):
        time.sleep(sleep_time)
        print("Thread1: " + message, i, time.perf_counter())


def task2(sleep_time, message):
    # block for a moment
    # display a message
    for i in range(10):
        time.sleep(sleep_time)
        print("Thread2: " + message, i, time.perf_counter())


# create a thread
thread1 = Thread(target=task1, args=(1.5, "Hello"))
thread2 = Thread(target=task2, args=(2, "Hi"))
# run the thread
thread1.start()
thread2.start()
# wait for the thread to finish
print("Waiting for the thread...")
thread1.join()
thread2.join()
print("Thread completed")
