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


def input_entry():
    customerName = e1.get()
    customerPhoneNumber = e2.get()
    customerAddress = e3.get()
    customerPayMethod = e4.get()
    ROLODEX.input_entry(customerName, customerPhoneNumber, customerAddress, customerPayMethod)


Button(master, text="Quit", command=master.quit).grid(row=4,column=0)
Button(master, text="Enter Customer", command=input_entry).grid(row=4, column=1)

mainloop()