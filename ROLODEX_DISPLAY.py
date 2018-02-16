from Tkinter import *
import ROLODEX


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.create_entries_and_scroll()
        self.create_input_customer()
        self.populate_entries()


    def create_entries_and_scroll(self):
        self.scrollbar = Scrollbar(self)
        self.text = Text(self, height=6, width=60)
        self.scrollbar.grid(column=3, row=5)
        self.text.grid(column=0, row=5, columnspan=2)
        self.scrollbar.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scrollbar.set)

    def input_entry(self):
        self.customerName = self.e1.get()
        self.customerPhoneNumber = self.e2.get()
        self.customerAddress = self.e3.get()
        self.customerPayMethod = self.e4.get()
        ROLODEX.input_entry(self.customerName, self.customerPhoneNumber, self.customerAddress, self.customerPayMethod)
        self.populate_entries()

    def create_input_customer(self):
        self.name_label = Label(self, text="Name").grid(row=0)
        self.phone_label = Label(self, text="Phone Number").grid(row=1)
        self.address_label = Label(self, text="Address").grid(row=2)
        self.payment_label = Label(self, text="Payment Method").grid(row=3)
        self.e1 = Entry(self)
        self.e2 = Entry(self)
        self.e3 = Entry(self)
        self.e4 = Entry(self)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)
        self.e4.grid(row=3, column=1)
        Button(self, text="Quit", command=self.quit).grid(row=4, column=0)
        Button(self, text="Enter Customer", command=self.input_entry).grid(row=4, column=1)

    def populate_entries(self):
        self.entrylist = ROLODEX.return_all_entries()
        for item in self.entrylist:
            self.text.insert(END, item)

app = Application()
app.master.title('ORDERM8')
mainloop()


