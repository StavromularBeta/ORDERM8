from Tkinter import *
import ROLODEX
master = Tk()

Label(master, text="Name").grid(row=0)
Label(master, text="Phone Number").grid(row=1)
Label(master, text="Address").grid(row=2)
Label(master, text="Payment Method").grid(row=3)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)

name = str(e1.get())
phoneNumber = str(e2.get())
address = str(e3.get())
payMethod = str(e4.get())

Button(master, text="Quit", command=master.quit).grid(row=4,column=0)
Button(master, text="Enter Customer", command=ROLODEX.input_entry(name,phoneNumber,address,payMethod)).grid(row=4,column=1)

mainloop()