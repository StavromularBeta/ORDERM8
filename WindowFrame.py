import Tkinter as tk
import SQL_functions


class WindowFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

    def clear_window_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def home_page(self):
        for widget in self.winfo_children():
            widget.destroy()
        tk.Label(self, text="This is the homepage.", font=self.parent.new_cust_font).grid()

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
        tk.Label(self.search_result_frame, text="ID", font=self.parent.label_cust_font).grid(row=0,
                                                                                             sticky=tk.W,
                                                                                             padx=10)
        tk.Label(self.search_result_frame, text="Name", font=self.parent.label_cust_font).grid(row=0,
                                                                                               column=1,
                                                                                               sticky=tk.W,
                                                                                               padx=10)
        tk.Label(self.search_result_frame, text="Phone Number", font=self.parent.label_cust_font).grid(row=0,
                                                                                                       column=2,
                                                                                                       sticky=tk.W,
                                                                                                       padx=10)
        tk.Label(self.search_result_frame, text="Address", font=self.parent.label_cust_font).grid(row=0,
                                                                                                  column=3,
                                                                                                  sticky=tk.W,
                                                                                                  padx=10)
        tk.Label(self.search_result_frame, text="Payment Method", font=self.parent.label_cust_font).grid(row=0, column=4, sticky=tk.W, padx=10)
        rowstart = 1
        for customer_entry in search_results:
            colstart = 0
            for item in customer_entry:
                tk.Label(self.search_result_frame, text=item).grid(row=rowstart,column=colstart, sticky=tk.W, padx=10)
                colstart += 1
            rowstart +=1

    def new_order(self):
        self.clear_window_frame()
        self.order_sheet_label = tk.Label(self, text="New Order Sheet", font=self.parent.new_cust_font)
        self.order_sheet = tk.Text(self, borderwidth=1)
        self.submit_order_button = tk.Button(self, text="Submit Order", command=self.submit_new_order)
        self.customer_order_entry_label = tk.Label(self, text="Customer Name", font=self.parent.label_cust_font)
        self.customer_order_name_enty = tk.Entry(self)
        self.order_sheet.grid(row=1, padx=10, columnspan=3)
        self.order_sheet_label.grid(row=0, sticky=tk.W, padx=10)
        self.submit_order_button.grid(row=2, column=2, sticky=tk.W, padx=10)
        self.customer_order_entry_label.grid(row=2, column=0, sticky=tk.E, padx=10)
        self.customer_order_name_enty.grid(row=2, column=1)

    def submit_new_order(self):
        order = self.order_sheet.get(1.0, tk.END)
        customer_id = 1
        SQL_functions.input_new_order(customer_id, order)

