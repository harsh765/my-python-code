from tkinter import*
import tkinter as tk
m=tk.Tk()
tk.Label(m,text="enter a name  :").grid(row=0)
tk.Label(m,text="enter a your surname  :").grid(row=1)
tk.Entry(m).grid(row=0,column=1)
tk.Entry(m).grid(row=1,column=1)
m.mainloop()

# import tkinter as tk
# def disp():
#         l1.config(text="change",bg="red")
# m=tk.Tk()
# l1=tk.Label(m,text="hello")
# l1.grid(row=0)
# tk.Button(m,text="login",command=disp).grid(row=1)
# m.mainloop()


