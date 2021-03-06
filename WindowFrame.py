import tkinter as tk
import SQL_functions
import Homepage_support.HomepageFrame as HF
import datetime
from collections import Counter


class WindowFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

    def clear_window_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    # Home Page Functions

    def home_page(self):
        self.clear_window_frame()
        tk.Label(self, text=HF.generate_current_time(), font=self.parent.new_cust_font).grid(row=0, padx=2)
        tk.Label(self, text=HF.generate_time_until_cutoff(), font=self.parent.new_cust_font).grid(row=0,
                                                                                                  column=1,
                                                                                                  sticky=tk.W)
        tk.Label(self, text="Tasks", font=self.parent.new_cust_font).grid(row=1, padx=2, pady=2, sticky=tk.NW)
        startrow = self.generate_labels_for_daily_tasks() + 1
        tk.Label(self, text="Current Customers", font=self.parent.new_cust_font).grid(row=startrow,
                                                                                      padx=2,
                                                                                      pady=2,
                                                                                      sticky=tk.W)
        self.generate_customer_simple_lookup(startrow)
        self.generate_labels_for_daily_customers(startrow)
        canvas_and_toolbar = HF.create_weekly_customer_figure(self)
        canvas_and_toolbar.get_tk_widget().grid(row=1, column=1, rowspan=15, sticky=tk.W)
        self.homepage_average_graph = HF.create_weekly_average_customer_figure(self,
                                                                               self.all_average_past_order_graph_data())
        self.homepage_average_graph.get_tk_widget().grid(row=1, column=2, rowspan=15, padx=2, sticky=tk.W)

    def generate_labels_for_daily_tasks(self):
        startrow = 2
        daily_tasks = HF.generate_tasks_for_day()
        for item in daily_tasks:
            tk.Label(self, text=" - " + item[1]).grid(row=startrow, padx=2, sticky=tk.W)
            startrow += 1
        return startrow

    def generate_customer_simple_lookup(self, startrow):
        self.search_result_frame = tk.Frame(self)
        self.search_result_frame.grid(row=startrow+2, columnspan=3, sticky=tk.W)
        self.search_select_frame = tk.Frame(self)
        self.search_select_frame.grid(row=startrow+1, columnspan=3, sticky=tk.W)
        self.option_variable = tk.StringVar(self)
        self.option_variable.set('First Name')
        self.search_options = tk.OptionMenu(self.search_select_frame, self.option_variable, "First Name", "Last Name")
        self.search_options.grid(row=1, column=0, sticky=tk.W)
        self.search_entry_field = tk.Entry(self.search_select_frame)
        self.search_entry_field.grid(row=1, column=1, sticky=tk.W)
        tk.Button(self.search_select_frame, text="search", command=self.simple_search_database).grid(row=1, column=2, sticky=tk.W)

    def simple_search_database(self):
        search_type = self.option_variable.get()
        search_entry = self.search_entry_field.get()
        if search_type == "First Name":
            search_results = SQL_functions.search_by_customer_first_name(search_entry)
        elif search_type == "Last Name":
            search_results = SQL_functions.search_by_customer_last_name(search_entry)
        elif search_type == "Phone Number":
            search_results = SQL_functions.search_by_customer_phone_number(search_entry)
        self.simple_display_results(search_results)

    def simple_display_results(self, search_results):
        for widget in self.search_result_frame.winfo_children():
            widget.destroy()
        tk.Label(self.search_result_frame, text="Add", font=self.parent.label_cust_font).grid(row=0,
                                                                                               column=0,
                                                                                               sticky=tk.W,
                                                                                               padx=4)
        tk.Label(self.search_result_frame, text="First Name", font=self.parent.label_cust_font).grid(row=0,
                                                                                               column=1,
                                                                                               sticky=tk.W,
                                                                                               padx=10)
        tk.Label(self.search_result_frame, text="Last Name", font=self.parent.label_cust_font).grid(row=0,
                                                                                               column=2,
                                                                                               sticky=tk.W,
                                                                                               padx=10)
        rowstart = 1
        for self.customer_entry in search_results:
            tk.Button(self.search_result_frame,
                      text="ADD",
                      width=4,
                      height=2,
                      command=lambda i=self.customer_entry: self.enter_customer_and_refresh_homepage(i)).grid(row=rowstart,
                                                                                                                      column=0,
                                                                                                                      sticky=tk.W,
                                                                                                                      padx=10)
            tk.Label(self.search_result_frame, text=self.customer_entry[1]).grid(row=rowstart,
                                                                            column=1,
                                                                            sticky=tk.W,
                                                                            padx=10)
            tk.Label(self.search_result_frame, text=self.customer_entry[2]).grid(row=rowstart,
                                                                            column=2,
                                                                            sticky=tk.W,
                                                                            padx=10)
            rowstart += 1

    def generate_labels_for_daily_customers(self, startrow):
        customer_list = HF.get_todays_current_customers()
        self.active_customer_frame = tk.Frame(self)
        self.active_customer_frame.grid(row=startrow+3, column=0, sticky=tk.W)
        tk.Label(self.active_customer_frame, text="Today's Active Customers", font=self.parent.label_cust_font).grid(row=0,
                                                                                                                     column=0,
                                                                                                                     sticky= tk.W)
        active_customer_row_counter = 1
        for item in customer_list:
            tk.Label(self.active_customer_frame, text=item).grid(row=active_customer_row_counter, column=0, sticky=tk.W)
            active_customer_row_counter += 1

    def enter_customer_and_refresh_homepage(self, customer_id):
        HF.enter_customer_into_daily(customer_id[0])
        self.home_page()



    # New Customer Entry Functions

    def load_new_customer(self):
        self.clear_window_frame()
        self.input_customer_label = tk.Label(self, text="New Customer Entry", font=self.parent.new_cust_font).grid(row=0, columnspan=2)
        self.first_name_label = tk.Label(self, text="First Name", font=self.parent.label_cust_font).grid(row=1, sticky=tk.W)
        self.last_name_label = tk.Label(self, text="Last Name", font=self.parent.label_cust_font).grid(row=2, sticky=tk.W)
        self.phone_label = tk.Label(self, text="Phone Number", font=self.parent.label_cust_font).grid(row=3, sticky=tk.W)
        self.address_label = tk.Label(self, text="Address", font=self.parent.label_cust_font).grid(row=4, sticky=tk.W)
        self.payment_label = tk.Label(self, text="Payment Method", font=self.parent.label_cust_font).grid(row=5, sticky=tk.W)
        self.e1 = tk.Entry(self)
        self.e2 = tk.Entry(self)
        self.e3 = tk.Entry(self)
        self.e4 = tk.Entry(self)
        self.e5 = tk.Entry(self)
        self.e1.grid(row=1, column=1, columnspan=2, sticky=tk.W)
        self.e2.grid(row=2, column=1, columnspan=2, sticky=tk.W)
        self.e3.grid(row=3, column=1, columnspan=2, sticky=tk.W)
        self.e4.grid(row=4, column=1, columnspan=2, sticky=tk.W)
        self.e5.grid(row=5, column=1, columnspan=2, sticky=tk.W)
        tk.Button(self, text="Enter Customer", command=self.input_entry).grid(row=6, column=0, columnspan=2, pady=10)

    def input_entry(self):
        self.customerFirstName = self.e1.get()
        self.customerLastName = self.e2.get()
        self.customerPhoneNumber = self.e3.get()
        self.customerAddress = self.e4.get()
        self.customerPayMethod = self.e5.get()
        SQL_functions.input_entry(self.customerFirstName,
                                  self.customerLastName,
                                  self.customerPhoneNumber,
                                  self.customerAddress,
                                  self.customerPayMethod)

    # Existing Customer Functions

    def populate_entries(self):
        self.clear_window_frame()
        self.allentries_canvas = tk.Canvas(self, width=800, height=800, scrollregion=(0,0,0,3600))
        self.allentries_scroll = tk.Scrollbar(self, orient="vertical", command=self.allentries_canvas.yview)
        self.allentries_frame = tk.Frame(self)
        self.allentries_canvas.configure(yscrollcommand=self.allentries_scroll.set)
        self.allentries_scroll.pack(side='right', fill='y')
        self.allentries_canvas.pack(side="left", fill='y')
        self.allentries_canvas.create_window((0,0), window=self.allentries_frame, anchor='nw')
        self.entries_label = tk.Label(self.allentries_frame, text="Existing Customer Entries", font=self.parent.new_cust_font).grid(row=1,
                                                                                                                   columnspan=3,
                                                                                                                   sticky=tk.W)
        self.entrylist = SQL_functions.return_all_entries()
        self.rowstart = 2
        tk.Label(self.allentries_frame, text='View', font=self.parent.label_cust_font).grid(row=self.rowstart,
                                                                           column=0,
                                                                           sticky=tk.W,
                                                                           padx=4)
        tk.Label(self.allentries_frame, text='First Name', font=self.parent.label_cust_font).grid(row=self.rowstart,
                                                                                 column=1,
                                                                                 sticky=tk.W,
                                                                                 padx=10)
        tk.Label(self.allentries_frame, text='Last Name', font=self.parent.label_cust_font).grid(row=self.rowstart,
                                                                                column=2,
                                                                                sticky=tk.W,
                                                                                padx=10)
        tk.Label(self.allentries_frame, text='Phone Number', font=self.parent.label_cust_font).grid(row=self.rowstart,
                                                                                   column=3,
                                                                                   sticky=tk.W,
                                                                                   padx=10)
        tk.Label(self.allentries_frame, text='Address', font=self.parent.label_cust_font).grid(row=self.rowstart,
                                                                              column=4,
                                                                              sticky=tk.W,
                                                                              padx=10)
        tk.Label(self.allentries_frame, text='Payment Method', font=self.parent.label_cust_font).grid(row=self.rowstart,
                                                                                     column=5,
                                                                                     sticky=tk.W,
                                                                                     padx=10)
        self.rowstart += 1
        for item in self.entrylist:

            tk.Button(self.allentries_frame,
                      text='GO',
                      width=4,
                      height=2,
                      command=lambda item=item: self.customer_page(item)).grid(row=self.rowstart,
                                                                               column=0,
                                                                               sticky=tk.W,
                                                                               padx=10)
            tk.Label(self.allentries_frame, text=item[1]).grid(row=self.rowstart, column=1, sticky=tk.W, padx=10)
            tk.Label(self.allentries_frame, text=item[2]).grid(row=self.rowstart, column=2, sticky=tk.W, padx=10)
            tk.Label(self.allentries_frame, text=item[3]).grid(row=self.rowstart, column=3, sticky=tk.W, padx=10)
            tk.Label(self.allentries_frame, text=item[4]).grid(row=self.rowstart, column=4, sticky=tk.W, padx=10)
            tk.Label(self.allentries_frame, text=item[5]).grid(row=self.rowstart, column=5, sticky=tk.W, padx=10)
            self.rowstart += 1

    # Customer Page Functions

    def customer_page(self, customer_entry):
        self.clear_window_frame()
        self.current_customer_entry = customer_entry
        self.customer_information_frame = tk.Frame(self)
        self.customer_delivery_preferences_frame = tk.Frame(self)
        self.customer_information_frame.grid(row=0, column=0, sticky=tk.W)
        self.customer_delivery_preferences_frame.grid(row=1, column=0, sticky=tk.W)
        self.customer_food_preferences_frame = tk.Frame(self)
        self.customer_food_preferences_frame.grid(row=1, column=1, sticky=tk.W)
        tk.Label(self.customer_information_frame, text=customer_entry[1] + " " + customer_entry[2], font=self.parent.label_cust_font).grid(row=0,
                                                                                                                column=0,
                                                                                                                sticky=tk.W)
        tk.Label(self.customer_information_frame, text="Phone : " + str(customer_entry[3])).grid(row=1, column=0, sticky=tk.W)
        tk.Label(self.customer_information_frame, text="Address : " + str(customer_entry[4])).grid(row=2, column=0, sticky=tk.W)
        tk.Label(self.customer_information_frame, text="Preferred payment method : " + customer_entry[5]).grid(row=3, column=0, sticky=tk.W)
        tk.Label(self.customer_delivery_preferences_frame, text="Delivery Preferences", font=self.parent.label_cust_font).grid(row=0, column=0, sticky=tk.W)
        self.customer_delivery_preferences_textbox = tk.Text(self.customer_delivery_preferences_frame,
                                                             borderwidth=1,
                                                             width=65,
                                                             height=20,
                                                             wrap="word",
                                                             highlightbackground="#D24C45")
        self.insert_delivery_preferences_onstart()
        self.customer_delivery_preferences_textbox.grid(row=2,
                                                        column=0,
                                                        padx=2,
                                                        sticky=tk.W)
        self.customer_delivery_preferences_textbox_savebutton = tk.Button(self.customer_delivery_preferences_frame,
                                                                          text="Save Preferences",
                                                                          command=self.save_customer_delivery_preferences)
        self.customer_delivery_preferences_textbox_savebutton.grid(row=3,
                                                                   column=0,
                                                                   padx=2,
                                                                   sticky=tk.W)
        tk.Label(self.customer_food_preferences_frame,
                 text="Food Preferences",
                 font=self.parent.label_cust_font).grid(row=0, column=0, padx=5, sticky=tk.W)
        self.customer_food_preferences_textbox = tk.Text(self.customer_food_preferences_frame,
                                                         borderwidth=1,
                                                         width=65,
                                                         height=20,
                                                         wrap="word",
                                                         highlightbackground="#D24C45")
        self.insert_food_preferences_onstart()
        self.customer_food_preferences_textbox_savebutton = tk.Button(self.customer_food_preferences_frame,
                                                                      text="Save Preferences",
                                                                      command=self.save_customer_food_preferences)
        self.customer_food_preferences_textbox_savebutton.grid(row=3, column=0, padx=5, sticky=tk.W)
        self.customer_food_preferences_textbox.grid(row=1, column=0, padx=5, sticky=tk.W)
        self.delete_current_customer_button = tk.Button(self.customer_information_frame,
                                                        text="Delete Customer",
                                                        command=self.delete_current_customer)
        self.delete_current_customer_button.grid(row=0, column=2, sticky=tk.E)
        self.recent_customer_orders_frame = tk.Frame(self)
        self.recent_customer_orders_frame.grid(row=3, column=0, padx=2, sticky=tk.W)
        tk.Label(self.recent_customer_orders_frame,
                 text="Last 10 Customer Orders",
                 font=self.parent.label_cust_font,
                 ).grid(row=0, column=0, padx=2, sticky=tk.W)
        self.past_customer_orders(customer_entry[0])
        self.average_graph = HF.create_weekly_average_customer_figure(self.recent_customer_orders_frame,
                                                                      self.average_past_order_graph_data(customer_entry[0]))
        self.average_graph.get_tk_widget().grid(row=0, column=1, rowspan=10, padx=2, sticky=tk.W)



    def past_customer_orders(self, customer_id):
        #just all orders for now.
        all_customer_orders = SQL_functions.select_recent_activity(customer_id)
        rowstart = 1
        for item in all_customer_orders:
            tk.Label(self.recent_customer_orders_frame, text=item[2]).grid(row=rowstart,
                                                                           column=0,
                                                                           padx=2,
                                                                           sticky=tk.W)
            rowstart += 1

    def average_past_order_graph_data(self, customer_id):
        past_customer_orders = SQL_functions.select_all_activity(customer_id)
        dates = []
        for item in past_customer_orders:
            dates.append(item[2])
        days = []
        for item in dates:
            days.append(datetime.datetime.strptime(item, "%Y-%m-%d").weekday())
        day_counter = Counter(days)
        week_dictionary = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        for key, value in day_counter.items():
            if key in week_dictionary:
                week_dictionary[key] = value
            else:
                pass
        total_orders = 0
        for key, value in week_dictionary.items():
            total_orders = total_orders + value
        for key, value in week_dictionary.items():
            week_dictionary[key] = float(value/total_orders)*100
        return week_dictionary

    def all_average_past_order_graph_data(self):
        past_customer_orders = SQL_functions.return_all_customer_entries_from_daily_customers()
        dates = []
        for item in past_customer_orders:
            dates.append(item[2])
        days = []
        for item in dates:
            days.append(datetime.datetime.strptime(item, "%Y-%m-%d").weekday())
        day_counter = Counter(days)
        week_dictionary = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
        for key, value in day_counter.items():
            if key in week_dictionary:
                week_dictionary[key] = value
            else:
                pass
        total_orders = 0
        for key, value in week_dictionary.items():
            total_orders = total_orders + value
        for key, value in week_dictionary.items():
            week_dictionary[key] = float(value/total_orders)*100
        print(total_orders)
        return week_dictionary

    def delete_current_customer(self):
        SQL_functions.delete_customer_and_customer_records(self.current_customer_entry[0])
        self.populate_entries()

    def insert_food_preferences_onstart(self):
        try:
            startup_food_preferences = SQL_functions.get_latest_foodprefs(self.current_customer_entry[0])[3]
            self.customer_food_preferences_textbox.insert('end-1c', startup_food_preferences)
        except TypeError:
            startup_food_preferences = 'Enter Food Preferences Here!'
            self.customer_food_preferences_textbox.insert('end-1c', startup_food_preferences)

    def insert_delivery_preferences_onstart(self):
        try:
            startup_delivery_preferences = SQL_functions.get_latest_customerprefs(self.current_customer_entry[0])[3]
            self.customer_delivery_preferences_textbox.insert('end-1c', startup_delivery_preferences)
        except TypeError:
            startup_delivery_preferences = 'Enter Delivery Notes Here!'
            self.customer_delivery_preferences_textbox.insert('end-1c', startup_delivery_preferences)

    def save_customer_delivery_preferences(self):
        delivery_preferences = self.customer_delivery_preferences_textbox.get("1.0", 'end-1c')
        SQL_functions.new_customer_delivery_preference(self.current_customer_entry[0], delivery_preferences)

    def save_customer_food_preferences(self):
        food_preferences = self.customer_food_preferences_textbox.get("1.0", 'end-1c')
        SQL_functions.new_customer_food_preference(self.current_customer_entry[0], food_preferences)


    # Customer Search Functions

    def generate_customer_search(self):
        self.clear_window_frame()
        tk.Label(self, text="Search Customers", font=self.parent.new_cust_font).grid(row=1,
                                                                                     columnspan=2)
        self.search_result_frame = tk.Frame(self)
        self.search_result_frame.grid(row=4, columnspan=3)
        self.option_variable = tk.StringVar(self)
        self.option_variable.set('First Name')
        self.search_options = tk.OptionMenu(self, self.option_variable, "First Name", "Last Name", "Phone Number")
        self.search_options.grid(row=2)
        self.search_entry_field = tk.Entry(self)
        self.search_entry_field.grid(row=2,column=1)
        tk.Button(self, text="search", command=self.search_database).grid(row=2, column=2)

    def search_database(self):
        search_type = self.option_variable.get()
        search_entry = self.search_entry_field.get()
        if search_type == "First Name":
            search_results = SQL_functions.search_by_customer_first_name(search_entry)
        elif search_type == "Last Name":
            search_results = SQL_functions.search_by_customer_last_name(search_entry)
        elif search_type == "Phone Number":
            search_results = SQL_functions.search_by_customer_phone_number(search_entry)
        self.display_results(search_results)

    def display_results(self, search_results):
        for widget in self.search_result_frame.winfo_children():
            widget.destroy()
        tk.Label(self.search_result_frame, text="View", font=self.parent.label_cust_font).grid(row=0,
                                                                                               column=0,
                                                                                               sticky=tk.W,
                                                                                               padx=4)
        tk.Label(self.search_result_frame, text="First Name", font=self.parent.label_cust_font).grid(row=0,
                                                                                               column=1,
                                                                                               sticky=tk.W,
                                                                                               padx=10)
        tk.Label(self.search_result_frame, text="Last Name", font=self.parent.label_cust_font).grid(row=0,
                                                                                               column=2,
                                                                                               sticky=tk.W,
                                                                                               padx=10)
        tk.Label(self.search_result_frame, text="Phone Number", font=self.parent.label_cust_font).grid(row=0,
                                                                                                       column=3,
                                                                                                       sticky=tk.W,
                                                                                                       padx=10)
        tk.Label(self.search_result_frame, text="Address", font=self.parent.label_cust_font).grid(row=0,
                                                                                                  column=4,
                                                                                                  sticky=tk.W,
                                                                                                  padx=10)
        tk.Label(self.search_result_frame, text="Payment Method", font=self.parent.label_cust_font).grid(row=0,
                                                                                                         column=5,
                                                                                                         sticky=tk.W,
                                                                                                         padx=10)
        rowstart = 1
        for customer_entry in search_results:
            tk.Button(self.search_result_frame,
                      text="GO",
                      width=4,
                      height=2,
                      command=lambda i=customer_entry: self.customer_page(i)).grid(row=rowstart,
                                                                                                column=0,
                                                                                                sticky=tk.W,
                                                                                                padx=10)
            tk.Label(self.search_result_frame, text=customer_entry[1]).grid(row=rowstart,
                                                                            column=1,
                                                                            sticky=tk.W,
                                                                            padx=10)
            tk.Label(self.search_result_frame, text=customer_entry[2]).grid(row=rowstart,
                                                                            column=2,
                                                                            sticky=tk.W,
                                                                            padx=10)
            tk.Label(self.search_result_frame, text=customer_entry[3]).grid(row=rowstart,
                                                                            column=3,
                                                                            sticky=tk.W,
                                                                            padx=10)
            tk.Label(self.search_result_frame, text=customer_entry[4]).grid(row=rowstart,
                                                                            column=4,
                                                                            sticky=tk.W,
                                                                            padx=10)
            tk.Label(self.search_result_frame, text=customer_entry[5]).grid(row=rowstart,
                                                                            column=5,
                                                                            sticky=tk.W,
                                                                            padx=10)
            rowstart += 1

    # Ordering Functions

    def new_order(self):
        self.clear_window_frame()
        self.order_sheet_label = tk.Label(self, text="New Order Sheet", font=self.parent.new_cust_font)
        self.order_sheet = tk.Text(self, borderwidth=1, highlightbackground="#D24C45")
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

    # Graphs Functions

    def graphs_page(self):
        self.clear_window_frame()
        self.graphs_canvas = tk.Canvas(self, width=800, height=800, scrollregion=(0,0,0,1200))
        self.graphs_scroll = tk.Scrollbar(self, orient="vertical", command=self.graphs_canvas.yview)
        self.graphs_frame = tk.Frame(self)
        self.graphs_canvas.configure(yscrollcommand=self.graphs_scroll.set)
        self.graphs_scroll.pack(side='right', fill='y')
        self.graphs_canvas.pack(side="left", fill='y')
        self.graphs_canvas.create_window((0,0), window=self.graphs_frame, anchor='nw')
        self.graphs_label = tk.Label(self.graphs_frame, text="Graphs", font=self.parent.new_cust_font)
        self.graphs_label.grid(row=0, column=0)
        canvas_and_toolbar = HF.create_weekly_customer_figure(self.graphs_frame)
        canvas_and_toolbar.get_tk_widget().grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        canvas_and_toolbar = HF.create_monthly_customer_figure(self.graphs_frame)
        canvas_and_toolbar.get_tk_widget().grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        canvas_and_toolbar = HF.create_yearly_customer_figure(self.graphs_frame)
        canvas_and_toolbar.get_tk_widget().grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
