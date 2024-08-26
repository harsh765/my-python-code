import tkinter as tk
from tkinter import *
m=tk.Tk()
def disp():
    tk.Label(m,text="hello edit").grid(row=0)
def sunn():
     tk.Label(m,text="hello view").grid(row=3)
def jk():
      tk.Label(m,text="hello cut").grid(row=2)
mb=Menu(m)
mi1=Menu(mb,tearoff=3)
mi2=Menu(mb,tearoff=5)
mi3=Menu(mb,tearoff=7)
mi1.add_separator() 
mi1.add_command(label="cut",command=jk)
mi1.add_command(label="edit",command=disp)
mi1.add_command(label="view",command=sunn)
mb.add_cascade(label="file",menu=mi1)
mi1.add_cascade(label="edit",menu=mi2)
mb.add_cascade(label="view",menu=mi3)
m.config(menu=mb)
m.mainloop()