from connector import Connector


class Selection(Connector):
    def __init__(self):
        super(Selection, self).__init__()
        super(self.__class__, self).__init__()
        self.table_names = {1: 'rolodex',
                            2: 'orders',
                            3: 'customer_preferences',
                            4: 'day_duties',
                            5: 'daily_customers'}
        self.rolodex_field_names = {1: 'id',
                                    2: 'last_name',
                                    3: 'first_name',
                                    4: 'phone_number',
                                    5: 'address',
                                    6: 'pay_method',
                                    7: 'status',
                                    8: 'order_method'}

    def select_all_from_table(self, table_number, print_view=None):
        query = "SELECT * FROM " + self.table_names[table_number]
        if print_view:
            for item in self.connector(query):
                print(item)
        else:
            return self.connector(query)

    def select_from_rolodex_table_with_conditions(self, field_number, condition, print_view=None):
        query = "SELECT * FROM rolodex WHERE " + self.rolodex_field_names[field_number] + " = (?)"
        if print_view:
            for item in self.connector(query, condition):
                print(item)
        else:
            return self.connector(query, condition)



