from connector import Connector


class EditEntry(Connector):
    def __init__(self):
        super(EditEntry, self).__init__()
        super(self.__class__, self).__init__()
        self.rolodex_field_names = {1: 'id',
                                    2: 'last_name',
                                    3: 'first_name',
                                    4: 'phone_number',
                                    5: 'address',
                                    6: 'pay_method',
                                    7: 'status',
                                    8: 'order_method'}

    def edit_rolodex_entry(self, field, update, customer_id):
        query = 'UPDATE rolodex SET ' + self.rolodex_field_names[field] + " = '" + update + "' WHERE id = " +\
                str(customer_id)
        print(query)
        return self.connector(query)
