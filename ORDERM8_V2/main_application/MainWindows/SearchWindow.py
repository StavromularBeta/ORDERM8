import tkinter as Tk


class SearchWindow(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent

    def search(self):
        search_label = Tk.Label(self, text="Search")
        search_label.grid()