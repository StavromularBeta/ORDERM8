import tkinter as tk
from tkinter import font as tkFont
import MenuFrame
import WindowFrame
import BannerFrame


class MainApplication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, width=1240, height=900)
        self.pack_propagate(0)
        self.pack()
        self.new_cust_font = tkFont.Font(size=30, weight='bold')
        self.label_cust_font = tkFont.Font(size=16, weight='bold')
        self.menu_frame = MenuFrame.MenuFrame(self)
        self.window_frame = WindowFrame.WindowFrame(self)
        self.banner_frame = BannerFrame.BannerFrame(self)
        self.banner_frame.pack(side=tk.TOP, fill=tk.X)
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y, anchor=tk.W)
        self.window_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, anchor=tk.W)
        self.menu_frame.create_rolodex_buttons()
        self.window_frame.home_page()

root = tk.Tk()
root.geometry('1240x900')
MainApplication(root).grid()
root.mainloop()

