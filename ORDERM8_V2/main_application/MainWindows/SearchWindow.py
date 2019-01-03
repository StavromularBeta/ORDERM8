import tkinter as Tk
import sys
sys.path.append("/Users/PeterLevett/Documents/My Actual Documents/SideProjects/ORDERM8/ORDERM8_V2/SQL_functions")
import selection as sel


class SearchWindow(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
        self.customer_display_frame = Tk.Frame(self)
        self.search_frame = Tk.Frame(self)
        self.all_customer_display_frame = Tk.Frame(self)
        self.selection = sel.Selection()

    def clear_search_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.customer_display_frame = Tk.Frame(self)
        self.search_frame = Tk.Frame(self)
        self.all_customer_display_frame = Tk.Frame(self)

    def display_all_customers(self, search=None):
        self.clear_search_window()
        display_all_customers_canvas = Tk.Canvas(self.customer_display_frame, width=450, height=800, scrollregion=(0, 0, 0, 2000))
        all_entries_scroll = Tk.Scrollbar(self.customer_display_frame, orient="vertical", command=display_all_customers_canvas.yview)
        self.all_customer_display_frame = Tk.Frame(self)  # I don't understand why this needs to be here.
        display_all_customers_canvas.configure(yscrollcommand=all_entries_scroll.set)
        all_entries_scroll.pack(side='right', fill='y')
        display_all_customers_canvas.pack(side="left", fill='y')
        display_all_customers_canvas.create_window((0, 0), window=self.all_customer_display_frame, anchor='nw')
        Tk.Label(self.all_customer_display_frame, text="Name").grid(row=0, column=0)
        Tk.Label(self.all_customer_display_frame, text="Phone").grid(row=0, column=1)
        Tk.Label(self.all_customer_display_frame, text="Address").grid(row=0, column=2)
        if search:
            self.return_searched_customers(search)
        else:
            self.return_all_customers()
        self.customer_display_frame.grid(row=0, column=0)

    def return_all_customers(self):
        all_customer_data = self.selection.select_all_from_table(1)
        first_customer_row = 1
        for item in all_customer_data:
            name = item[2] + " " + item[1]
            phone = item[3]
            address = item[4]
            Tk.Button(self.all_customer_display_frame,
                      text=name,
                      command=lambda item=item: self.parent.display_customerpage(item)).grid(row=first_customer_row, column=0)
            Tk.Label(self.all_customer_display_frame, text=phone).grid(row=first_customer_row, column=1)
            Tk.Label(self.all_customer_display_frame, text=address).grid(row=first_customer_row, column=2)
            first_customer_row += 1

    def search_customers(self):
        self.search_frame = Tk.Frame(self)
        Tk.Label(self.search_frame, text="Search Customers").grid(row=0, column=0)
        search_result_frame = Tk.Frame(self.search_frame)
        search_result_frame.grid(row=1, column=0, columnspan=3)
        self.option_variable = Tk.StringVar(search_result_frame)
        self.option_variable.set('First Name')
        search_options = Tk.OptionMenu(search_result_frame, self.option_variable, "First Name", "Last Name")
        search_options.grid(row=0)
        self.search_entry_field = Tk.Entry(search_result_frame)
        self.search_entry_field.grid(row=0, column=1)
        Tk.Button(search_result_frame, text="search", command=self.search_database_for_customers).grid(row=0, column=2)
        Tk.Button(search_result_frame, text="all", command=self.parent.display_searchpage).grid(row=0, column=3)
        self.search_frame.grid(row=0, column=1, sticky=Tk.NW)

    def search_database_for_customers(self):
        search_type = self.option_variable.get()
        entry_field = self.search_entry_field.get()
        if search_type == "First Name":
            search_results = self.selection.select_from_rolodex_table_with_conditions(3, (entry_field,))
        elif search_type == "Last Name":
            search_results = self.selection.select_from_rolodex_table_with_conditions(2, (entry_field,))
        self.parent.display_searchpage(search_results)

    def return_searched_customers(self, search):
        first_customer_row = 1
        for item in search:
            name = item[2] + " " + item[1]
            phone = item[3]
            address = item[4]
            Tk.Button(self.all_customer_display_frame,
                      text=name,
                      command=lambda item=item: self.parent.display_customerpage(item)).grid(row=first_customer_row, column=0)
            Tk.Label(self.all_customer_display_frame, text=phone).grid(row=first_customer_row, column=1)
            Tk.Label(self.all_customer_display_frame, text=address).grid(row=first_customer_row, column=2)
            first_customer_row += 1
