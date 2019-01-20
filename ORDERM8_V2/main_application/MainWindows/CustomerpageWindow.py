import tkinter as Tk
import sys
sys.path.append("/Users/PeterLevett/Documents/My Actual Documents/SideProjects/ORDERM8/ORDERM8_V2/SQL_functions")
import editentry


class CustomerpageWindow(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
        self.basic_information_window = Tk.Frame(self)
        self.update_information_frame = Tk.Frame(self)
        self.update_entry = Tk.Entry(self.update_information_frame)
        self.edit_entry = editentry.EditEntry()
        self.rolodex_converter = {"First Name": 3,
                                  "Last Name": 2,
                                  "Address": 5,
                                  "Phone Number": 4,
                                  "Payment Method": 6,
                                  "Order Method": 8,}

    def clear_customer_page_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.basic_information_window = Tk.Frame(self)
        self.update_information_frame = Tk.Frame(self)

    def generate_customer_page(self, customer):
        customer_name = customer[2] + " " + customer[1]
        self.basic_information_window.grid(row=0, column=0)
        Tk.Label(self.basic_information_window, text=customer_name).grid(row=0, column=0, sticky=Tk.W)
        Tk.Label(self.basic_information_window, text="Address: " + customer[4]).grid(row=1, column=0, sticky=Tk.W)
        Tk.Label(self.basic_information_window, text="Phone Number: " + customer[3]).grid(row=2, column=0, sticky=Tk.W)
        Tk.Label(self.basic_information_window, text="Payment Method: " + customer[5]).grid(row=3, column=0, sticky=Tk.W)
        Tk.Label(self.basic_information_window, text="Order Method: " + customer[7]).grid(row=4, column=0, sticky=Tk.W)

    def update_customer_information(self, customer):
        self.update_information_frame.grid(row=1, column=0)
        self.update_entry.grid(row=0, column=0, columnspan=2)
        option_variable = Tk.StringVar(self.update_information_frame)
        option_variable.set('First Name')
        update_options = Tk.OptionMenu(self.update_information_frame,
                                       option_variable,
                                       "First Name",
                                       "Last Name",
                                       "Address",
                                       "Phone Number",
                                       "Payment Method",
                                       "Order Method").grid(row=1, column=0)
        update_entry_button = Tk.Button(self.update_information_frame,
                                        text="Update",
                                        command=lambda: self.update_db(customer, option_variable)).grid(row=1, column=1)

    def update_db(self, customer, option_variable):
        desired_update = self.update_entry.get()
        self.edit_entry.edit_rolodex_entry(self.rolodex_converter[option_variable.get()], desired_update, customer[0])
        self.clear_customer_page_window()
        self.parent.display_customerpage(customer)
