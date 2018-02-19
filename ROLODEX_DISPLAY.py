from Tkinter import *
import tkFont
import ROLODEX


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.new_cust_font = tkFont.Font(size=30, weight='bold')
        self.label_cust_font = tkFont.Font(size=16, weight='bold')
        self.grid()
        self.create_input_customer()
        self.populate_entries()


    def input_entry(self):
        self.customerName = self.e1.get()
        self.customerPhoneNumber = self.e2.get()
        self.customerAddress = self.e3.get()
        self.customerPayMethod = self.e4.get()
        ROLODEX.input_entry(self.customerName, self.customerPhoneNumber, self.customerAddress, self.customerPayMethod)
        self.populate_entries()

    def create_input_customer(self):
        self.input_customer_label = Label(self, text="New Customer Entry", font=self.new_cust_font).grid(row=0, columnspan=2)
        self.name_label = Label(self, text="Name", font=self.label_cust_font).grid(row=1, sticky=W)
        self.phone_label = Label(self, text="Phone Number", font=self.label_cust_font).grid(row=2, sticky=W)
        self.address_label = Label(self, text="Address", font=self.label_cust_font).grid(row=3, sticky=W)
        self.payment_label = Label(self, text="Payment Method", font=self.label_cust_font).grid(row=4, sticky=W)
        self.e1 = Entry(self)
        self.e2 = Entry(self)
        self.e3 = Entry(self)
        self.e4 = Entry(self)
        self.e1.grid(row=1, column=1, columnspan=2, sticky=W)
        self.e2.grid(row=2, column=1, columnspan=2, sticky=W)
        self.e3.grid(row=3, column=1, columnspan=2, sticky=W)
        self.e4.grid(row=4, column=1, columnspan=2, sticky=W)
        #Button(self, text="Quit", command=self.quit).grid(row=8, column=0, columnspan=2, pady=10)
        Button(self, text="Enter Customer", command=self.input_entry).grid(row=5, column=0, columnspan=2, pady=10)

    def populate_entries(self):
        self.entries_label = Label(self, text="Existing Customer Entries", font=self.new_cust_font).grid(row=6,
                                                                                                         columnspan=3,
                                                                                                         sticky=W)
        self.entrylist = ROLODEX.return_all_entries()
        self.rowstart = 7
        Label(self, text='ID', font=self.label_cust_font).grid(row=self.rowstart, column=0, sticky=W, padx=4)
        Label(self, text='Name', font=self.label_cust_font).grid(row=self.rowstart, column=1, sticky=W, padx=10)
        Label(self, text='Phone Number', font=self.label_cust_font).grid(row=self.rowstart, column=2, sticky=W, padx=10)
        Label(self, text='Address', font=self.label_cust_font).grid(row=self.rowstart, column=3, sticky=W, padx=10)
        Label(self, text='Payment Method', font=self.label_cust_font).grid(row=self.rowstart, column=4, sticky=W, padx=10)
        self.rowstart += 1
        for item in self.entrylist:
            Label(self, text=item[0]).grid(row=self.rowstart, column=0, sticky=W, padx=4)
            Label(self, text=item[1]).grid(row=self.rowstart, column=1, sticky=W, padx=10)
            Label(self, text=item[2]).grid(row=self.rowstart, column=2, sticky=W, padx=10)
            Label(self, text=item[3]).grid(row=self.rowstart, column=3, sticky=W, padx=10)
            Label(self, text=item[4]).grid(row=self.rowstart, column=4, sticky=W, padx=10)
            self.rowstart += 1
        return self.rowstart

app = Application()
app.master.title('ORDERM8')
mainloop()


