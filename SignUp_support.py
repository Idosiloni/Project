#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#	 Jan 22, 2021 05:39:48 PM +0200	 platform: Windows NT
#	 Jan 22, 2021 05:41:27 PM +0200	 platform: Windows NT
#	 Jan 22, 2021 06:37:53 PM +0200	 platform: Windows NT
from socket import *
import sys
import sqlite3
import Main_support
from time import sleep
try:
	import Tkinter as tk
except ImportError:
	import tkinter as tk

try:
	import ttk
	py3 = False
except ImportError:
	import tkinter.ttk as ttk
	py3 = True

def set_Tk_var():
	global che50
	che50 = tk.StringVar()
	global che51
	che51 = tk.StringVar()

def init(top, gui, *args, **kwargs):
	global w, top_level, root
	w = gui
	top_level = top
	root = top
	ClearChecks()
	
	
from queue import Queue
conn_q = Queue()
def client_send():
	while True:
		if conn_q.empty() == False:
			data = conn_q.get()
			print ("client_send:" + data )
			Main_support.my_socket.sendall(data.encode('latin-1'))
		sleep(0.05) #sleep a little before check the queue again
	
	
def btnConfirm_1click(p1):
	print('SignUp_support.btnConfirm_1click')
	#conn = sqlite3.connect('DataBase1.db')
	#c=conn.cursor()
	
	sys.stdout.flush()
	print(w.EntUser.get())
	print(w.EntPass.get())
	if che50.get()=="1":
		print("Student")
		keyword='Student'
	if che51.get()=="1":
		print("Teacher")
		keyword='Teacher'
		
	src= "signUp,"+w.EntUser.get()+","+w.EntPass.get()+","+keyword
	print(src)
	Main_support.my_socket.sendall(src.encode('latin-1'))
	#conn_q.put(src)
		
		#c.execute("INSERT INTO Users(Username,Password,Job) VALUES (?, ?, ?)" ,(w.EntUser.get() ,w.EntPass.get() ,keyword))
	data=Main_support.my_socket.recv(1024).decode()
	print(data)
	if data=="Ok":
		destroy_window()
	else:	 
		print("username already exist")
		w.EntUser.delete(0,len(w.EntUser.get())+1)
		w.EntPass.delete(0,len(w.EntPass.get())+1)
	
def destroy_window():
	# Function which closes the window.
	global top_level
	top_level.destroy()
	top_level = None
	
	
def ClearChecks():
	che50.set("0")
	che51.set("0")




if __name__ == '__main__':
	import SignUp
	SignUp.vp_start_gui()





