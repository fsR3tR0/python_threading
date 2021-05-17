import threading
import time

sem = threading.Semaphore()

def th_sem1():
	while True:
		sem.acquire()
		print(1)
		time.sleep(1)
		sem.release()
		time.sleep(1)

def th_sem2():
	while True:
		sem.acquire()
		print(2)
		time.sleep(1)
		sem.release()
		time.sleep(1)

th1 = threading.Thread(target = th_sem1)
th1.start()
th2 = threading.Thread(target = th_sem2)
th2.start()
th1.join()
th2.join()
print("Vega")


