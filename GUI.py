from Tkinter import *
import ROLODEX
import tkFont


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.new_cust_font = tkFont.Font(size=30, weight='bold')
        self.label_cust_font = tkFont.Font(size=16, weight='bold')
        self.grid()
        self.create_button_container()
        self.create_rolodex_buttons()

    def create_button_container(self):
        self.container = Frame(self)
        self.container.grid()

    def load_new_customer(self):
        self.new_customer_button.grid_forget()
        self.view_all_customers.grid_forget()
        self.create_input_customer()

    def create_input_customer(self):
        self.input_customer_label = Label(self.container, text="New Customer Entry", font=self.new_cust_font).grid(row=0, columnspan=2)
        self.name_label = Label(self.container, text="Name", font=self.label_cust_font).grid(row=1, sticky=W)
        self.phone_label = Label(self.container, text="Phone Number", font=self.label_cust_font).grid(row=2, sticky=W)
        self.address_label = Label(self.container, text="Address", font=self.label_cust_font).grid(row=3, sticky=W)
        self.payment_label = Label(self.container, text="Payment Method", font=self.label_cust_font).grid(row=4, sticky=W)
        self.e1 = Entry(self.container)
        self.e2 = Entry(self.container)
        self.e3 = Entry(self.container)
        self.e4 = Entry(self.container)
        self.e1.grid(row=1, column=1, columnspan=2, sticky=W)
        self.e2.grid(row=2, column=1, columnspan=2, sticky=W)
        self.e3.grid(row=3, column=1, columnspan=2, sticky=W)
        self.e4.grid(row=4, column=1, columnspan=2, sticky=W)
        Button(self.container, text="Enter Customer", command=self.input_entry).grid(row=5, column=0, columnspan=2, pady=10)
        Button(self.container, text="Main Menu", command=self.main_menu).grid(row=5, column=3, columnspan=2, pady=10)

    def input_entry(self):
        self.customerName = self.e1.get()
        self.customerPhoneNumber = self.e2.get()
        self.customerAddress = self.e3.get()
        self.customerPayMethod = self.e4.get()
        #here is where you need to check for errors.
        ROLODEX.input_entry(self.customerName, self.customerPhoneNumber, self.customerAddress, self.customerPayMethod)


    def load_all_customers(self):
        self.new_customer_button.grid_forget()
        self.view_all_customers.grid_forget()
        self.populate_entries()

    def populate_entries(self):
        Button(self.container, text="Main menu", command=self.main_menu).grid(row=0)
        self.entries_label = Label(self.container, text="Existing Customer Entries", font=self.new_cust_font).grid(row=1,
                                                                                                         columnspan=3,
                                                                                                         sticky=W)
        self.entrylist = ROLODEX.return_all_entries()
        self.rowstart = 2
        Label(self.container, text='ID', font=self.label_cust_font).grid(row=self.rowstart, column=0, sticky=W, padx=4)
        Label(self.container, text='Name', font=self.label_cust_font).grid(row=self.rowstart, column=1, sticky=W, padx=10)
        Label(self.container, text='Phone Number', font=self.label_cust_font).grid(row=self.rowstart, column=2, sticky=W, padx=10)
        Label(self.container, text='Address', font=self.label_cust_font).grid(row=self.rowstart, column=3, sticky=W, padx=10)
        Label(self.container, text='Payment Method', font=self.label_cust_font).grid(row=self.rowstart, column=4, sticky=W, padx=10)
        self.rowstart += 1
        for item in self.entrylist:
            Label(self.container, text=item[0]).grid(row=self.rowstart, column=0, sticky=W, padx=4)
            Label(self.container, text=item[1]).grid(row=self.rowstart, column=1, sticky=W, padx=10)
            Label(self.container, text=item[2]).grid(row=self.rowstart, column=2, sticky=W, padx=10)
            Label(self.container, text=item[3]).grid(row=self.rowstart, column=3, sticky=W, padx=10)
            Label(self.container, text=item[4]).grid(row=self.rowstart, column=4, sticky=W, padx=10)
            self.rowstart += 1
        return self.rowstart

    def main_menu(self):
        for widget in self.container.winfo_children():
            widget.destroy()
        self.create_rolodex_buttons()


    def create_rolodex_buttons(self):
        self.new_customer_button = Button(self.container, text="Enter New Customer", command=self.load_new_customer)
        self.view_all_customers = Button(self.container, text="View All Customers", command=self.load_all_customers)
        self.new_customer_button.grid()
        self.view_all_customers.grid(row=1)

app = Application()
app.master.title('ORDERM8')
mainloop()
