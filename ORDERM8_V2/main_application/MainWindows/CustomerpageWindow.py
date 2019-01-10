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
        Tk.Label(self.basic_information_window, text=customer_name).grid(row=0, column=0, sticky=Tk.W)
        Tk.Label(self.basic_information_window, text="Address: " + customer[4]).grid(row=1, column=0, sticky=Tk.W)
        Tk.Label(self.basic_information_window, text="Phone Number: " + customer[3]).grid(row=2, column=0, sticky=Tk.W)
        Tk.Label(self.basic_information_window, text="Payment Method: " + customer[5]).grid(row=3, column=0, sticky=Tk.W)
        Tk.Label(self.basic_information_window, text="Order Method: " + customer[7]).grid(row=4, column=0, sticky=Tk.W)
