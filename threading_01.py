import threading
import time
import sys
import os

class Complex:
	def __init__(self,Re,Im):
		self.Re = Re
		self.Im = Im

	def print(self):
		print("\nValos: ",self.Re,"- Kepzetes: ",self.Im)

class FileHandling:
	def __init__(self,mit,hogyan):
		self.mit = mit
		self.rw = hogyan
		self.fp = open(mit,hogyan)

def th1():
	print("[+] Th1 started")
	time.sleep(1)
	for i in range(0,10):
		print("th1: ",i)
		time.sleep(0.5)
		print(threading.activeCount())
	print("Th1 ended")

def th2():
	print("[+] Th2 started")
	time.sleep(1)
	for i in range(0,5):
		print("th2: ",i)
		print(threading.activeCount())
		time.sleep(1)
	print("Th2 ended")

def th3():
	time.sleep(6.5)
	print("[+] Th3 started")
	print(threading.activeCount())
	var_in = input("\t Write something:" )
	print("\nU wrote this: ",var_in)
	print(threading.activeCount())

def th4():
	time.sleep(7)
	print("[+] Th4 started")
	lol = Complex(2.4,5.6)
	lol.print()
	print(lol.Re,"-",lol.Im)
	print(threading.activeCount())

def th5():
	print("[+] Th5 started")
	fo = FileHandling("thread_test.txt","r")
	print("\t\t===")
	while True:
		c = fo.fp.read(1)
		if c == '':
			break
		else:
			print(c,end='')
	print("\t\t===")
	fo.fp.close()
	print("File bezarva")
	print("\tCounter: ",threading.activeCount())

def stop_threading():
	os._exit(1)

if __name__ == "__main__":
	print("Na mehet")
	time.sleep(1)
	#sys.exit()
	try:
		t1 = threading.Thread(target=th1)
		t2 = threading.Thread(target=th2)
		t3 = threading.Thread(target=th3)
		t4 = threading.Thread(target=th4)
		t5 = threading.Thread(target=th5)

		t1.start()
		t2.start()
		t3.start()
		t4.start()
		t5.start()

		t1.join()
		t2.join()
		t3.join()
		t4.join()
		t5.join()

		print("Counter: ",threading.activeCount())
		print("[+] Main thread ended")
	except KeyboardInterrupt as e:
		print("\n[+]Interrupted\nSystem shutdown...")
		stop_threading()
		#sys.exit("Leall")
