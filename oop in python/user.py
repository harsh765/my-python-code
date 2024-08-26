import tkinter as tk

m=tk.Tk()


def display():
    a = l1.get()
    b = l2.get()
    if a== "Darshan" and b == "Borse":
        l3.config(text="Successfully Login")
    else:
        l3.config(text="Invalid credentials")
        

        

    


tk.Label(m,text="user name  :").grid(row=0)
tk.Label(m,text="passworld  :").grid(row=1)
tk.Button(m,text="Login", command=display).grid(row=2, column=1)
tk.Button(m,text="Cancel").grid(row=3,column=1)
l1 = tk.Entry(m)
l1.grid(row=0,column=1)
l2 = tk.Entry(m)
l2.grid(row=1,column=1)

l3 = tk.Label(m, text="")
l3.grid(row=3)
m.mainloop()


