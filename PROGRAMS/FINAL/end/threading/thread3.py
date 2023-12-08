from time import sleep
from threading import Thread


class CustomThread(Thread):
    def run(self):
        sleep(1)
        print("This is coming from another thread")
        self.value = 99


thread = CustomThread()
thread.start()
print("Waiting for the thread to finish")
thread.join()
value = thread.value
print(f"Got: {value}")
