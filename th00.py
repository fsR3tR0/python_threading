import threading
import time

def th1():
	print("Th1 start")
	for i in range(0,10):
		print("t1: "+str(i))
		time.sleep(1)
	"""	print("Nem jo")
		exit()"""
	print("Th1 vege")

def th2():
	print("Th2 start")
	for i in range(0,11):
		print("t2: "+str(i))
		time.sleep(1)
	print("Th2 vege")

th1 = threading.Thread(target = th1)
th1.start()
th2 = threading.Thread(target = th2)
th2.start()
th1.join()
th2.join()
print("Vega")
