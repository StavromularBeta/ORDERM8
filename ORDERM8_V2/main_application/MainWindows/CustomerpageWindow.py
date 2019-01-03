import tkinter as Tk


class CustomerpageWindow(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
        self.basic_information_window = Tk.Frame(self)

    def clear_customer_page_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.basic_information_window = Tk.Frame(self)

    def generate_customer_page(self, customer):
        customer_name = customer[2] + " " + customer[1]
        self.basic_information_window.grid()
        Tk.Label(self.basic_information_window, text=customer_name).grid(row=0, column=0)


