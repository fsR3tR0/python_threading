import threading
import time

def th1():
	print("[+] Th1 started")
	time.sleep(1)
	for i in range(0,10):
		print("th1: ",i)
		time.sleep(0.5)
	print("Th1 ended")

def th2():
	print("[+] Th2 started")
	time.sleep(1)
	for i in range(0,5):
		print("th2: ",i)
		time.sleep(1)
	print("Th2 ended")

def th3():
	time.sleep(5)
	var_in = input("\t Write something:" )
	print("U wrote this: ",var_in)

if __name__ == "__main__":
	t1 = threading.Thread(target=th1)
	t2 = threading.Thread(target=th2)
	t3 = threading.Thread(target=th3)

	t1.start()
	t2.start()
	t3.start()

	t1.join()
	t2.join()
	t3.join()

	print("[+] Main thread ended")
	#print(threading.activeCount())
