import tkinter as Tk
from MainWindows import HomepageWindow as Hpw, GraphsWindow as Grw, SearchWindow as Srw, EditAddWindow as Eaw


class MainWindow(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.HomepageWindow = Hpw.HomepageWindow(self)
        self.GraphsWindow = Grw.GraphsWindow(self)
        self.SearchWindow = Srw.SearchWindow(self)
        self.EditAddWindow = Eaw.EditAddWindow(self)

    def clear_main_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.HomepageWindow = Hpw.HomepageWindow(self)
        self.GraphsWindow = Grw.GraphsWindow(self)
        self.SearchWindow = Srw.SearchWindow(self)
        self.EditAddWindow = Eaw.EditAddWindow(self)

    def display_homepage(self):
        self.clear_main_window()
        self.HomepageWindow.Homepage()
        self.HomepageWindow.grid()

    def display_graphspage(self):
        self.clear_main_window()
        self.GraphsWindow.graphs()
        self.GraphsWindow.grid()

    def display_searchpage(self, search=None):
        self.clear_main_window()
        if search:
            self.SearchWindow.display_all_customers(search)
        else:
            self.SearchWindow.display_all_customers()
        self.SearchWindow.search_customers()
        self.SearchWindow.grid()

    def display_editaddpage(self):
        self.clear_main_window()
        self.EditAddWindow.edit_add()
        self.EditAddWindow.grid()
