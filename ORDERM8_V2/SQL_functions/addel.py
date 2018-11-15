from connector import Connector


class AdDel(Connector):
    def __init__(self):
        super(AdDel, self).__init__()
        super(self.__class__, self).__init__()

    def new_rolodex_entry(self, values):
        # last_name,first_name,phone_number,address,pay_method,active
        values_tuple = (values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7])
        query = 'INSERT INTO rolodex VALUES (?,?,?,?,?,?,?)'
        return self.connector(query, values_tuple)
