#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Jan 22, 2021 06:05:13 PM +0200  platform: Windows NT

import sys

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

import Main_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Main (root)
    Main_support.init(root, top)
    root.mainloop()

w = None
def create_Main(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Main(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Main (w)
    Main_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Main():
    global w
    w.destroy()
    w = None

class Main:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+664+322")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Online Class")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.titel = tk.Label(top)
        self.titel.place(relx=0.433, rely=0.067, height=41, width=104)
        self.titel.configure(activebackground="#f9f9f9")
        self.titel.configure(activeforeground="black")
        self.titel.configure(background="#d9d9d9")
        self.titel.configure(disabledforeground="#a3a3a3")
        self.titel.configure(foreground="#000000")
        self.titel.configure(highlightbackground="#d9d9d9")
        self.titel.configure(highlightcolor="black")
        self.titel.configure(text='''Menu''')

        self.btnSign = tk.Button(top)
        self.btnSign.place(relx=0.433, rely=0.244, height=24, width=107)
        self.btnSign.configure(activebackground="#ececec")
        self.btnSign.configure(activeforeground="#000000")
        self.btnSign.configure(background="#d9d9d9")
        self.btnSign.configure(disabledforeground="#a3a3a3")
        self.btnSign.configure(foreground="#000000")
        self.btnSign.configure(highlightbackground="#d9d9d9")
        self.btnSign.configure(highlightcolor="black")
        self.btnSign.configure(pady="0")
        self.btnSign.configure(text='''SignUp''')
        self.btnSign.bind('<Button-1>',lambda e:Main_support.btn_1click(e))

        self.btnLog = tk.Button(top)
        self.btnLog.place(relx=0.433, rely=0.356, height=24, width=107)
        self.btnLog.configure(activebackground="#ececec")
        self.btnLog.configure(activeforeground="#000000")
        self.btnLog.configure(background="#d9d9d9")
        self.btnLog.configure(disabledforeground="#a3a3a3")
        self.btnLog.configure(foreground="#000000")
        self.btnLog.configure(highlightbackground="#d9d9d9")
        self.btnLog.configure(highlightcolor="black")
        self.btnLog.configure(pady="0")
        self.btnLog.configure(text='''LogIn''')
        self.btnLog.bind('<Button-1>',lambda e:Main_support.btnLog_1click(e))

        self.btnExit = tk.Button(top)
        self.btnExit.place(relx=0.467, rely=0.667, height=24, width=67)
        self.btnExit.configure(activebackground="#ececec")
        self.btnExit.configure(activeforeground="#000000")
        self.btnExit.configure(background="#d9d9d9")
        self.btnExit.configure(disabledforeground="#a3a3a3")
        self.btnExit.configure(foreground="#000000")
        self.btnExit.configure(highlightbackground="#d9d9d9")
        self.btnExit.configure(highlightcolor="black")
        self.btnExit.configure(pady="0")
        self.btnExit.configure(text='''Exit''')
        self.btnExit.bind('<Button-1>',lambda e:Main_support.btnExit_1click(e))

if __name__ == '__main__':
    vp_start_gui()





