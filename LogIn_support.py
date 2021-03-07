#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Jan 22, 2021 06:13:02 PM +0200  platform: Windows NT
#    Jan 22, 2021 06:34:37 PM +0200  platform: Windows NT

import sys
import sqlite3
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

def btnConfirm_1click(p1):
    username=False
    password=False
    type1=''
    print('LogIn_support.btnConfirm_1click')
    sys.stdout.flush()
    print(w.Entry1.get())
    print(w.Entry2.get())
    conn = sqlite3.connect('DataBase1.db')
    data=w.Entry1.get()
    data1=w.Entry2.get()
    cursor = conn.execute("SELECT * from Users")
    for row in cursor:
        if row[0] == data:
            username=True
            type1=row[2]
        if row[1] ==  data1:
            password=True
    if username and password:
        if type1=='Student':
            print('im in')
            import Student
            Student.create_Student(root,'Hello',top_level)
        if type1=='Teacher':
            print('im in')
            import Teacher
            Teacher.create_Teacher_first(root,'Hello',top_level)
    else:
        w.Entry1.delete(0,len(w.Entry1.get())+1)
        w.Entry2.delete(0,len(w.Entry2.get())+1)
        
    conn.commit()
    conn.close()
def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import LogIn
    LogIn.vp_start_gui()





