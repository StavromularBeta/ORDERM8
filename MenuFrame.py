import Tkinter as tk


class MenuFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, background="#D24C45")
        self.parent = parent

    def create_rolodex_buttons(self):
        self.home_page_button = tk.Button(self,
                                          text="Home",
                                          highlightbackground="#F57C76",
                                          width=12,
                                          height=3,
                                          command=self.parent.window_frame.home_page)
        self.view_all_customers = tk.Button(self,
                                            text="View All \nCustomers",
                                            highlightbackground="#F57C76",
                                            width=12,
                                            height=3,
                                            command=self.parent.window_frame.populate_entries)
        self.search_customers_button = tk.Button(self,
                                                 text="Search \nCustomers",
                                                 highlightbackground="#F57C76",
                                                 width=12,
                                                 height=3,
                                                 command=self.parent.window_frame.generate_customer_search)
        self.new_customer_button = tk.Button(self,
                                             text="Enter New \nCustomer",
                                             width=12,
                                             height=3,
                                             highlightbackground="#D24C45",
                                             command=self.parent.window_frame.load_new_customer)
        self.new_order_button = tk.Button(self,
                                          text="Place\n New Order",
                                          width=12,
                                          height=3,
                                          highlightbackground="#D24C45",
                                          command=self.parent.window_frame.new_order)
        self.sizer_square = tk.Canvas(self,
                                      width=127,
                                      height=5,
                                      background="#D24C45",
                                      highlightbackground="#D24C45")
        self.sizer_square_1 = tk.Canvas(self,
                                        width=127,
                                        height=5,
                                        background="#D24C45",
                                        highlightbackground="#D24C45")
        self.sizer_square_2 = tk.Canvas(self,
                                        width=127,
                                        height=5,
                                        background="#D24C45",
                                        highlightbackground="#D24C45")
        self.sizer_square_3 = tk.Canvas(self,
                                        width=127,
                                        height=5,
                                        background="#D24C45",
                                        highlightbackground="#D24C45")
        self.sizer_square_4 = tk.Canvas(self,
                                      width=127,
                                      height=5,
                                      background="#D24C45",
                                      highlightbackground="#D24C45")

        self.home_page_button.grid(row=1)
        self.view_all_customers.grid(row=3)
        self.search_customers_button.grid(row=5)
        self.new_customer_button.grid(row=7)
        self.new_order_button.grid(row=9)
        self.sizer_square.grid(row=0)
        self.sizer_square_1.grid(row=2)
        self.sizer_square_2.grid(row=4)
        self.sizer_square_3.grid(row=6)
        self.sizer_square_4.grid(row=8)
