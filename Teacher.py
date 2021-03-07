#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#    Mar 01, 2021 05:09:39 PM +0200  platform: Windows NT

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

import Teacher_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Teacher_first (root)
    Teacher_support.init(root, top)
    root.mainloop()

w = None
def create_Teacher_first(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Teacher_first(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Teacher_first (w)
    Teacher_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Teacher_first():
    global w
    w.destroy()
    w = None

class Teacher_first:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+621+233")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1,  1)
        top.title("Online Class")
        top.configure(background="#d9d9d9")

        self.UserDetails = tk.Text(top)
        self.UserDetails.place(relx=0.017, rely=0.022, relheight=0.142
                , relwidth=0.273)
        self.UserDetails.configure(background="white")
        self.UserDetails.configure(font="TkTextFont")
        self.UserDetails.configure(foreground="black")
        self.UserDetails.configure(highlightbackground="#d9d9d9")
        self.UserDetails.configure(highlightcolor="black")
        self.UserDetails.configure(insertbackground="black")
        self.UserDetails.configure(selectbackground="blue")
        self.UserDetails.configure(selectforeground="white")
        self.UserDetails.configure(wrap="word")

        self.ClassDetails = tk.Text(top)
        self.ClassDetails.place(relx=0.683, rely=0.022, relheight=0.142
                , relwidth=0.29)
        self.ClassDetails.configure(background="white")
        self.ClassDetails.configure(font="TkTextFont")
        self.ClassDetails.configure(foreground="black")
        self.ClassDetails.configure(highlightbackground="#d9d9d9")
        self.ClassDetails.configure(highlightcolor="black")
        self.ClassDetails.configure(insertbackground="black")
        self.ClassDetails.configure(selectbackground="blue")
        self.ClassDetails.configure(selectforeground="white")
        self.ClassDetails.configure(wrap="word")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.483, rely=0.178, relheight=0.744
                , relwidth=0.492)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(cursor="fleur")

        self.LabelFrame = tk.Label(self.Frame1)
        self.LabelFrame.place(relx=0.339, rely=0.03, height=28, width=97)
        self.LabelFrame.configure(background="#d9d9d9")
        self.LabelFrame.configure(disabledforeground="#a3a3a3")
        self.LabelFrame.configure(foreground="#000000")
        self.LabelFrame.configure(text='''Schedule''')

        self.Btn_Send = tk.Button(self.Frame1)
        self.Btn_Send.place(relx=0.407, rely=0.657, height=44, width=67)
        self.Btn_Send.configure(activebackground="#ececec")
        self.Btn_Send.configure(activeforeground="#000000")
        self.Btn_Send.configure(background="#d9d9d9")
        self.Btn_Send.configure(disabledforeground="#a3a3a3")
        self.Btn_Send.configure(foreground="#000000")
        self.Btn_Send.configure(highlightbackground="#d9d9d9")
        self.Btn_Send.configure(highlightcolor="black")
        self.Btn_Send.configure(pady="0")
        self.Btn_Send.configure(text='''Send''')
        self.Btn_Send.bind('<Button-1>',lambda e:Teacher_support.Send_Click(e))

        self.Date = tk.Entry(self.Frame1)
        self.Date.place(relx=0.373, rely=0.149, height=20, relwidth=0.319)
        self.Date.configure(background="white")
        self.Date.configure(cursor="fleur")
        self.Date.configure(disabledforeground="#a3a3a3")
        self.Date.configure(font="TkFixedFont")
        self.Date.configure(foreground="#000000")
        self.Date.configure(insertbackground="black")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.169, rely=0.119, height=41, width=44)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Date''')

        self.Time = tk.Entry(self.Frame1)
        self.Time.place(relx=0.373, rely=0.269, height=20, relwidth=0.319)
        self.Time.configure(background="white")
        self.Time.configure(disabledforeground="#a3a3a3")
        self.Time.configure(font="TkFixedFont")
        self.Time.configure(foreground="#000000")
        self.Time.configure(insertbackground="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.169, rely=0.239, height=41, width=44)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Time''')

        self.ClassType = tk.Entry(self.Frame1)
        self.ClassType.place(relx=0.373, rely=0.388, height=20, relwidth=0.319)
        self.ClassType.configure(background="white")
        self.ClassType.configure(cursor="fleur")
        self.ClassType.configure(disabledforeground="#a3a3a3")
        self.ClassType.configure(font="TkFixedFont")
        self.ClassType.configure(foreground="#000000")
        self.ClassType.configure(insertbackground="black")

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.169, rely=0.358, height=41, width=44)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(cursor="fleur")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Type''')

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.169, rely=0.478, height=41, width=44)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(cursor="fleur")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Content''')

        self.Content = tk.Entry(self.Frame1)
        self.Content.place(relx=0.373, rely=0.507, height=20, relwidth=0.319)
        self.Content.configure(background="white")
        self.Content.configure(disabledforeground="#a3a3a3")
        self.Content.configure(font="TkFixedFont")
        self.Content.configure(foreground="#000000")
        self.Content.configure(insertbackground="black")

        self.Btn_Exit = tk.Button(self.Frame1)
        self.Btn_Exit.place(relx=0.407, rely=0.806, height=44, width=67)
        self.Btn_Exit.configure(activebackground="#ececec")
        self.Btn_Exit.configure(activeforeground="#000000")
        self.Btn_Exit.configure(background="#d9d9d9")
        self.Btn_Exit.configure(disabledforeground="#a3a3a3")
        self.Btn_Exit.configure(foreground="#000000")
        self.Btn_Exit.configure(highlightbackground="#d9d9d9")
        self.Btn_Exit.configure(highlightcolor="black")
        self.Btn_Exit.configure(pady="0")
        self.Btn_Exit.configure(text='''Exit''')
        self.Btn_Exit.bind('<Button-1>',lambda e:Teacher_support.Exit_Click(e))

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.017, rely=0.178, relheight=0.744
                , relwidth=0.458)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#d9d9d9")

        self.LabelFrame1 = tk.Label(self.Frame2)
        self.LabelFrame1.place(relx=0.364, rely=0.03, height=21, width=69)
        self.LabelFrame1.configure(background="#d9d9d9")
        self.LabelFrame1.configure(disabledforeground="#a3a3a3")
        self.LabelFrame1.configure(foreground="#000000")
        self.LabelFrame1.configure(text='''Chat''')

        self.Chat = tk.Text(self.Frame2)
        self.Chat.place(relx=0.073, rely=0.119, relheight=0.848, relwidth=0.869)
        self.Chat.configure(background="white")
        self.Chat.configure(font="TkTextFont")
        self.Chat.configure(foreground="black")
        self.Chat.configure(highlightbackground="#d9d9d9")
        self.Chat.configure(highlightcolor="black")
        self.Chat.configure(insertbackground="black")
        self.Chat.configure(selectbackground="blue")
        self.Chat.configure(selectforeground="white")
        self.Chat.configure(wrap="word")

        self.Title = tk.Label(top)
        self.Title.place(relx=0.4, rely=0.044, height=41, width=94)
        self.Title.configure(background="#d9d9d9")
        self.Title.configure(disabledforeground="#a3a3a3")
        self.Title.configure(foreground="#000000")
        self.Title.configure(text='''Label''')

if __name__ == '__main__':
    vp_start_gui()




