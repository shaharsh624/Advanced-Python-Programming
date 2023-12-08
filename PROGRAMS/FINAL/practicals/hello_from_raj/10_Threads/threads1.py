import threading
import time


def oddEven(x):
    if x % 2 == 0:
        print(x)
    else:
        print("--")


def tellEvenOdd(x):
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")


num = 56
thread1 = threading.Thread(target=oddEven(num))
thread2 = threading.Thread(target=tellEvenOdd(num))

thread1.start()
thread2.start()

# thread1.join()
# thread2.join()

print("Threads finished execution.")
