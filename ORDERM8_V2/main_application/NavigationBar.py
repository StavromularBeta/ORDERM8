import Tkinter as Tk


class NavigationBar(Tk.Frame):
    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.parent = parent

    def make_navbar(self):
        home_page_button = Tk.Button(self, text="Homepage", command=self.parent.MainWindow.display_homepage)
        graphs_button = Tk.Button(self, text="Graphs", command=self.parent.MainWindow.display_graphspage)
        search_button = Tk.Button(self, text="Search", command=self.parent.MainWindow.display_searchpage)
        home_page_button.grid(row=0)
        graphs_button.grid(row=1)
        search_button.grid(row=2)



