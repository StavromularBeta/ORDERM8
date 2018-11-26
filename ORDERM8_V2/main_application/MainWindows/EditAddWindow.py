import tkinter as Tk
import sys
sys.path.append("/Users/PeterLevett/Documents/My Actual Documents/SideProjects/ORDERM8/ORDERM8_V2/SQL_functions")
import addel as ad


class EditAddWindow(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
        self.add_delete_query = ad.AdDel()
        self.add_new_customer_frame = Tk.Frame(self)
        self.e1 = Tk.Entry(self.add_new_customer_frame)
        self.e2 = Tk.Entry(self.add_new_customer_frame)
        self.e3 = Tk.Entry(self.add_new_customer_frame)
        self.e4 = Tk.Entry(self.add_new_customer_frame)
        self.e5 = Tk.Entry(self.add_new_customer_frame)
        self.e6 = Tk.Entry(self.add_new_customer_frame)

    def clear_edit_add_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.add_new_customer_frame = Tk.Frame(self)
        self.e1 = Tk.Entry(self.add_new_customer_frame)
        self.e2 = Tk.Entry(self.add_new_customer_frame)
        self.e3 = Tk.Entry(self.add_new_customer_frame)
        self.e4 = Tk.Entry(self.add_new_customer_frame)
        self.e5 = Tk.Entry(self.add_new_customer_frame)
        self.e6 = Tk.Entry(self.add_new_customer_frame)

    def edit_add(self):
        edit_add_label = Tk.Label(self, text="Edit/Add")
        new_customer_entry_frame = self.generate_new_customer_frame()
        edit_add_label.grid(row=0)
        new_customer_entry_frame.grid(row=1)

    def generate_new_customer_frame(self):
        Tk.Label(self.add_new_customer_frame, text="New Customer Entry").grid(row=0, columnspan=2)
        Tk.Label(self.add_new_customer_frame, text="First Name").grid(row=1, sticky=Tk.W)
        Tk.Label(self.add_new_customer_frame, text="Last Name").grid(row=2, sticky=Tk.W)
        Tk.Label(self.add_new_customer_frame, text="Phone Number").grid(row=3, sticky=Tk.W)
        Tk.Label(self.add_new_customer_frame, text="Address").grid(row=4, sticky=Tk.W)
        Tk.Label(self.add_new_customer_frame, text="Payment Method").grid(row=5, sticky=Tk.W)
        Tk.Label(self.add_new_customer_frame, text="Order Method").grid(row=6, sticky=Tk.W)
        self.e1.grid(row=1, column=1, columnspan=2, sticky=Tk.W)
        self.e2.grid(row=2, column=1, columnspan=2, sticky=Tk.W)
        self.e3.grid(row=3, column=1, columnspan=2, sticky=Tk.W)
        self.e4.grid(row=4, column=1, columnspan=2, sticky=Tk.W)
        self.e5.grid(row=5, column=1, columnspan=2, sticky=Tk.W)
        self.e6.grid(row=6, column=1, columnspan=2, sticky=Tk.W)
        Tk.Button(self, text="Enter Customer", command=self.input_entry).grid(row=6, column=0, columnspan=2, pady=10)
        return self.add_new_customer_frame

    def input_entry(self):
        customer_first_name = self.e1.get()
        customer_last_name = self.e2.get()
        customer_phone_number = self.e3.get()
        customer_address = self.e4.get()
        customer_pay_method = self.e5.get()
        customer_order_method = self.e6.get()
        customer_entry = [None,
                          customer_last_name,
                          customer_first_name,
                          customer_phone_number,
                          customer_address,
                          customer_pay_method,
                          True,
                          customer_order_method]
        self.add_delete_query.new_rolodex_entry(customer_entry)
        self.clear_edit_add_frame()
        self.edit_add()
