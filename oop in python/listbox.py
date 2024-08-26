from tkinter import*
top=Tk()
lb=Listbox(top)
lb.insert(1,'python')
lb.insert(2,'java')
lb.insert(3,'c++')
lb.insert(4,'any other')
lb.grid()
top.mainloop()