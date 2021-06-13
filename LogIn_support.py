#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Jan 22, 2021 06:13:02 PM +0200  platform: Windows NT
#    Jan 22, 2021 06:34:37 PM +0200  platform: Windows NT
from socket import *
import sys
import sqlite3
import Main_support
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



def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
data=""
data1=""


def btnConfirm_1click(p1):
    print('LogIn_support.btnConfirm_1click')
    sys.stdout.flush()
    print(w.Entry1.get())
    print(w.Entry2.get())
    global data
    global data1
    data=w.Entry1.get()
    data1=w.Entry2.get()

    src = "LogIn," + data + "," + data1
    print(src)
    Main_support.my_socket.sendall(src.encode('latin-1'))
    #w.Entry1.delete(0,len(w.Entry1.get())+1)
    #w.Entry2.delete(0,len(w.Entry2.get())+1)
    #print('wrong')
    data2 = Main_support.my_socket.recv(1024).decode()
    print(data2)
    if data2=="ERROR":
        print("wrong")
        w.Entry1.delete(0, len(data) + 1)
    else:

        if data2 == 'Student':
            print('im in')
            import Student
            Student.create_Student(root, 'Hello', top_level)
        if data2 == 'Teacher':
            print('im in')
            import Teacher
            Teacher.create_Teacher_first(root, 'Hello', top_level)

class User1:
    def __init__(self):
        self.Username = data
        self.Password = data1

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import LogIn
    LogIn.vp_start_gui()





