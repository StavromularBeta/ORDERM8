import Tkinter as tk


class BannerFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background='#B52B24')
        self.parent = parent
        self.make_banner()

    def make_banner(self):
        tk.Label(self, text="ORDERM8", font=self.parent.new_cust_font, background='#B52B24', pady=5, padx=7).grid()
