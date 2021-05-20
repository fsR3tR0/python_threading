#! /usr/bin/python3

import os
import time
import threading
from tkinter import *
import numpy as np
import sys
from tkinter import messagebox

#global root_tk

class object_tk:
	def __init__(self,name,x,y,geo):
		self.root = Tk()
		self.root.title(name)
		#self.root.config(width=x,height=y)
#		self.root.geometry('1000x1000+100+100')
		self.root.geometry(geo)

def th1():
	print("[+] Th1 started")
	for i in np.arange(2.3,7.9,0.5):
		print(i)
		time.sleep(1)
	print("[-] Th1 finished")

def th2():
	print("[+] Th2 started")
	for k in range(6):
		print(k)
		time.sleep(1.2)
	print("[-] Th2 finished")

def th_tk():
#	global root_tk
	print("Threading for tk")
	root_tk = object_tk("Na menjen")
	root_tk.root.mainloop()

def btn_exit_function():
	if messagebox.askokcancel("Exit","Are you sure?"):
		root.root.destroy()
	else:
		print("Nem lett bezarva")

if __name__ == "__main__":
	t1 = threading.Thread(target=th1)
	t2 = threading.Thread(target=th2)
	#t3 = threading.Thread(target=th_tk)

	root = object_tk("Na menjen",200,200,'500x500+100+100')

	label_00 = Label(root.root,text="Ez lehetne egy szoveg is, de nem az",fg='red',bg='black')
	label_00.config(width=100,height=20)
	label_00.pack()

	messagebox.showinfo("Megy","Mehet?")
	root.root.protocol("WM_DELETE_WINDOW",btn_exit_function)

	t1.start()
	t2.start()
	#t3.start()
	try:
		root.root.mainloop()
		t1.join()
		t2.join()
		#t3.join()
	except:
		e = sys.exc_info()[0]
		print(e)
		e = sys.exc_info()[1]
		print(e)
		e = sys.exc_info()[2]
		print(e)
		print("Except lefutott")
		raise os._exit(1)
	print("Main thread ended")

