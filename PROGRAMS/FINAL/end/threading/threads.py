import threading
import time


def func(seconds):
    print(f"Sleeping for {seconds} second(s)...")
    time.sleep(seconds)


time1 = time.perf_counter()

# Normal execution
# func(4)
# func(2)
# func(1)

time2 = time.perf_counter()

# Threading execution
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

time3 = time.perf_counter()

print(f"(Normal Execution: {time2 - time1}), Thread execution {time3 - time2}")
print(t1.name, t2.name, t3.name)
