from time import sleep
from threading import Thread

thread = Thread(target=lambda: sleep(1))
print(thread.is_alive())
thread.start()
print(thread.is_alive())
thread.join()
print(thread.is_alive())


# example of reporting the thread identifier
from threading import Thread
# create the thread
thread = Thread()
# report the thread identifier
print(thread.ident)
# start the thread
thread.start()
# report the thread identifier
print(thread.ident)
