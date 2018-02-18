from Tkinter import *
import tkFont
import ROLODEX


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.new_cust_font = tkFont.Font(size=30, weight='bold')
        self.grid()
        self.create_entries_and_scroll()
        self.create_input_customer()
        self.populate_entries()


    def create_entries_and_scroll(self):
        self.scrollbar = Scrollbar(self)
        self.text = Text(self, height=6, width=80, relief=GROOVE)
        self.entries_label = Label(self, text="Existing Customer Entries", font=self.new_cust_font).grid(row=6, columnspan=3)
        self.scrollbar.grid(column=3, row=7,)
        self.text.grid(column=0, row=7, columnspan=2, padx=10, pady=10)
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
        self.input_customer_label = Label(self, text="New Customer Entry", font=self.new_cust_font).grid(row=0, columnspan=3)
        self.name_label = Label(self, text="Name").grid(row=1)
        self.phone_label = Label(self, text="Phone Number").grid(row=2)
        self.address_label = Label(self, text="Address").grid(row=3)
        self.payment_label = Label(self, text="Payment Method").grid(row=4)
        self.e1 = Entry(self)
        self.e2 = Entry(self)
        self.e3 = Entry(self)
        self.e4 = Entry(self)
        self.e1.grid(row=1, column=1)
        self.e2.grid(row=2, column=1)
        self.e3.grid(row=3, column=1)
        self.e4.grid(row=4, column=1)
        Button(self, text="Quit", command=self.quit).grid(row=8, column=0, columnspan=2, pady=10)
        Button(self, text="Enter Customer", command=self.input_entry).grid(row=5, column=0, columnspan=2, pady=10)

    def populate_entries(self):
        self.entrylist = ROLODEX.return_all_entries()
        for item in self.entrylist:
            self.text.insert(END, item)

app = Application()
app.master.title('ORDERM8')
mainloop()


