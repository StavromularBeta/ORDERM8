import Tkinter as tk
import SQL_functions
import tkFont


class MainApplication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.new_cust_font = tkFont.Font(size=30, weight='bold')
        self.label_cust_font = tkFont.Font(size=16, weight='bold')
        self.menu_frame = MenuFrame(self)
        self.window_frame = WindowFrame(self)
        self.banner_frame = BannerFrame(self)
        self.menu_frame.grid(row=0, rowspan=2)
        self.window_frame.grid(row=1, column=1)
        self.banner_frame.grid(row=0, column=1)
        self.menu_frame.create_rolodex_buttons()


class MenuFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

    def create_rolodex_buttons(self):
        self.new_customer_button = tk.Button(self, text="Enter New Customer", command=self.parent.window_frame.load_new_customer)
        self.view_all_customers = tk.Button(self, text="View All Customers", command=self.parent.window_frame.populate_entries)
        self.search_customers_button = tk.Button(self, text="Search Customers", command=self.parent.window_frame.generate_customer_search)
        self.new_customer_button.grid()
        self.view_all_customers.grid(row=1)
        self.search_customers_button.grid(row=3)


class WindowFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

    def clear_window_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def load_new_customer(self):
        self.clear_window_frame()
        self.input_customer_label = tk.Label(self, text="New Customer Entry", font=self.parent.new_cust_font).grid(row=0, columnspan=2)
        self.name_label = tk.Label(self, text="Name", font=self.parent.label_cust_font).grid(row=1, sticky=tk.W)
        self.phone_label = tk.Label(self, text="Phone Number", font=self.parent.label_cust_font).grid(row=2, sticky=tk.W)
        self.address_label = tk.Label(self, text="Address", font=self.parent.label_cust_font).grid(row=3, sticky=tk.W)
        self.payment_label = tk.Label(self, text="Payment Method", font=self.parent.label_cust_font).grid(row=4, sticky=tk.W)
        self.e1 = tk.Entry(self)
        self.e2 = tk.Entry(self)
        self.e3 = tk.Entry(self)
        self.e4 = tk.Entry(self)
        self.e1.grid(row=1, column=1, columnspan=2, sticky=tk.W)
        self.e2.grid(row=2, column=1, columnspan=2, sticky=tk.W)
        self.e3.grid(row=3, column=1, columnspan=2, sticky=tk.W)
        self.e4.grid(row=4, column=1, columnspan=2, sticky=tk.W)
        tk.Button(self, text="Enter Customer", command=self.input_entry).grid(row=5, column=0, columnspan=2, pady=10)

    def input_entry(self):
        self.customerName = self.e1.get()
        self.customerPhoneNumber = self.e2.get()
        self.customerAddress = self.e3.get()
        self.customerPayMethod = self.e4.get()
        SQL_functions.input_entry(self.customerName, self.customerPhoneNumber, self.customerAddress, self.customerPayMethod)

    def populate_entries(self):
        self.clear_window_frame()
        self.entries_label = tk.Label(self, text="Existing Customer Entries", font=self.parent.new_cust_font).grid(row=1,
                                                                                                                   columnspan=3,
                                                                                                                   sticky=tk.W)
        self.entrylist = SQL_functions.return_all_entries()
        self.rowstart = 2
        tk.Label(self, text='ID', font=self.parent.label_cust_font).grid(row=self.rowstart, column=0, sticky=tk.W, padx=4)
        tk.Label(self, text='Name', font=self.parent.label_cust_font).grid(row=self.rowstart, column=1, sticky=tk.W, padx=10)
        tk.Label(self, text='Phone Number', font=self.parent.label_cust_font).grid(row=self.rowstart, column=2, sticky=tk.W, padx=10)
        tk.Label(self, text='Address', font=self.parent.label_cust_font).grid(row=self.rowstart, column=3, sticky=tk.W, padx=10)
        tk.Label(self, text='Payment Method', font=self.parent.label_cust_font).grid(row=self.rowstart, column=4, sticky=tk.W, padx=10)
        self.rowstart += 1
        for item in self.entrylist:
            tk.Label(self, text=item[0]).grid(row=self.rowstart, column=0, sticky=tk.W, padx=4)
            tk.Label(self, text=item[1]).grid(row=self.rowstart, column=1, sticky=tk.W, padx=10)
            tk.Label(self, text=item[2]).grid(row=self.rowstart, column=2, sticky=tk.W, padx=10)
            tk.Label(self, text=item[3]).grid(row=self.rowstart, column=3, sticky=tk.W, padx=10)
            tk.Label(self, text=item[4]).grid(row=self.rowstart, column=4, sticky=tk.W, padx=10)
            self.rowstart += 1
        return self.rowstart

    def generate_customer_search(self):
        self.clear_window_frame()
        tk.Label(self, text="Search Customers", font=self.parent.new_cust_font).grid(row=1, columnspan=2)
        self.search_result_frame = tk.Frame(self)
        self.search_result_frame.grid(row=4, columnspan=3)
        self.option_variable = tk.StringVar(self)
        self.option_variable.set('name')
        self.search_options = tk.OptionMenu(self, self.option_variable, "name", "Phone Number")
        self.search_options.grid(row=2)
        self.search_entry_field = tk.Entry(self)
        self.search_entry_field.grid(row=2,column=1)
        tk.Button(self, text="search", command=self.search_database).grid(row=2, column=2)

    def search_database(self):
        search_type = self.option_variable.get()
        search_entry = self.search_entry_field.get()
        if search_type == "name":
            search_results = SQL_functions.search_by_customer_name(search_entry)
        elif search_type == "Phone Number":
            search_results = SQL_functions.search_by_customer_phone_number(search_entry)
        self.display_results(search_results)

    def display_results(self, search_results):
        for widget in self.search_result_frame.winfo_children():
            widget.destroy()
        tk.Label(self.search_result_frame, text="ID", font=self.parent.label_cust_font).grid(row=0, sticky=tk.W, padx=10)
        tk.Label(self.search_result_frame, text="Name", font=self.parent.label_cust_font).grid(row=0, column=1, sticky=tk.W, padx=10)
        tk.Label(self.search_result_frame, text="Phone Number", font=self.parent.label_cust_font).grid(row=0, column=2, sticky=tk.W, padx=10)
        tk.Label(self.search_result_frame, text="Address", font=self.parent.label_cust_font).grid(row=0, column=3, sticky=tk.W, padx=10)
        tk.Label(self.search_result_frame, text="Payment Method", font=self.parent.label_cust_font).grid(row=0, column=4, sticky=tk.W, padx=10)
        rowstart = 1
        for customer_entry in search_results:
            colstart = 0
            for item in customer_entry:
                tk.Label(self.search_result_frame, text=item).grid(row=rowstart,column=colstart, sticky=tk.W, padx=10)
                colstart += 1
            rowstart +=1


class BannerFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

root = tk.Tk()
MainApplication(root).grid()
root.mainloop()
