import tkinter as Tk
import sys
sys.path.append("/Users/PeterLevett/Documents/My Actual Documents/SideProjects/ORDERM8/ORDERM8_V2/SQL_functions")
import selection as sel


class SearchWindow(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
        self.customer_display_frame = Tk.Frame(self)
        self.selection = sel.Selection()

    def clear_search_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.customer_display_frame = Tk.Frame(self)

    def display_all_customers(self):
        self.clear_search_window()
        display_all_customers_canvas = Tk.Canvas(self, width=800, height=800, scrollregion=(0, 0, 0, 2000))
        all_entries_scroll = Tk.Scrollbar(self, orient="vertical", command=display_all_customers_canvas.yview)
        self.customer_display_frame = Tk.Frame(self)  # I don't understand why this needs to be here.
        display_all_customers_canvas.configure(yscrollcommand=all_entries_scroll.set)
        all_entries_scroll.pack(side='right', fill='y')
        display_all_customers_canvas.pack(side="left", fill='y')
        display_all_customers_canvas.create_window((0, 0), window=self.customer_display_frame, anchor='nw')
        Tk.Label(self.customer_display_frame, text="Name").grid(row=0, column=0)
        Tk.Label(self.customer_display_frame, text="Phone").grid(row=0, column=1)
        Tk.Label(self.customer_display_frame, text="Address").grid(row=0, column=2)
        self.return_all_customers()
        return self.customer_display_frame

    def return_all_customers(self):
        all_customer_data = self.selection.select_all_from_table(1)
        first_customer_row = 1
        for item in all_customer_data:
            name = item[1] + " " + item[2]
            phone = item[3]
            address = item[4]
            Tk.Label(self.customer_display_frame, text=name).grid(row=first_customer_row, column=0)
            Tk.Label(self.customer_display_frame, text=phone).grid(row=first_customer_row, column=1)
            Tk.Label(self.customer_display_frame, text=address).grid(row=first_customer_row, column=2)
            first_customer_row += 1

