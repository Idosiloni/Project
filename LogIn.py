#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Jan 22, 2021 06:33:57 PM +0200  platform: Windows NT

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

import LogIn_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = LogIn (root)
    LogIn_support.init(root, top)
    root.mainloop()

w = None
def create_LogIn(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_LogIn(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = LogIn (w)
    LogIn_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_LogIn():
    global w
    w.destroy()
    w = None

class LogIn:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+670+230")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("LogIn")
        top.configure(background="#d9d9d9")

        self.LblLog = tk.Label(top)
        self.LblLog.place(relx=0.45, rely=0.089, height=31, width=64)
        self.LblLog.configure(background="#d9d9d9")
        self.LblLog.configure(disabledforeground="#a3a3a3")
        self.LblLog.configure(foreground="#000000")
        self.LblLog.configure(text='''LogIn''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.533, rely=0.244, height=20, relwidth=0.14)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.LblUsr = tk.Label(top)
        self.LblUsr.place(relx=0.383, rely=0.244, height=21, width=74)
        self.LblUsr.configure(background="#d9d9d9")
        self.LblUsr.configure(disabledforeground="#a3a3a3")
        self.LblUsr.configure(foreground="#000000")
        self.LblUsr.configure(text='''Username''')

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.533, rely=0.378, height=20, relwidth=0.14)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.LblPass = tk.Label(top)
        self.LblPass.place(relx=0.383, rely=0.378, height=21, width=74)
        self.LblPass.configure(background="#d9d9d9")
        self.LblPass.configure(cursor="fleur")
        self.LblPass.configure(disabledforeground="#a3a3a3")
        self.LblPass.configure(foreground="#000000")
        self.LblPass.configure(text='''Password''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.BtnConfirm = tk.Button(top)
        self.BtnConfirm.place(relx=0.467, rely=0.511, height=34, width=57)
        self.BtnConfirm.configure(activebackground="#ececec")
        self.BtnConfirm.configure(activeforeground="#000000")
        self.BtnConfirm.configure(background="#d9d9d9")
        self.BtnConfirm.configure(disabledforeground="#a3a3a3")
        self.BtnConfirm.configure(foreground="#000000")
        self.BtnConfirm.configure(highlightbackground="#d9d9d9")
        self.BtnConfirm.configure(highlightcolor="black")
        self.BtnConfirm.configure(pady="0")
        self.BtnConfirm.configure(text='''Confirm''')
        self.BtnConfirm.bind('<Button-1>',lambda e:LogIn_support.btnConfirm_1click(e))

if __name__ == '__main__':
    vp_start_gui()





