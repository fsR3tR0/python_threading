import threading
import time
import sys
import os

class Complex:
	def __init__(self,Re,Im):
		self.Re = Re
		self.Im = Im

	def print(self):
		print("Valos: ",self.Re,", kepzetes: ",self.Im)

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
	time.sleep(6.5)
	var_in = input("\t Write something:" )
	print("U wrote this: ",var_in)

def th4():
	time.sleep(7)
	lol = Complex(2.4,5.6)
	lol.print()


def stop_threading():
	os._exit(1)
#t1.terminate()
	#t1.stop()
	#t2.stop()
	#t3.stop()
#	t1.stop()

if __name__ == "__main__":
	print("Na mehet")
	time.sleep(1)
	#sys.exit()
	try:
		t1 = threading.Thread(target=th1)
		t2 = threading.Thread(target=th2)
		t3 = threading.Thread(target=th3)
		t4 = threading.Thread(target=th4)
		t1.start()
		t2.start()
		t3.start()
		t4.start()

		t1.join()
		t2.join()
		t3.join()
		t4.join()

		print("[+] Main thread ended")
		#print(threading.activeCount())
	except KeyboardInterrupt as e:
		print("\n[+]Interrupted\nSystem shutdown...")
		stop_threading()
		#sys.exit("Leall")
