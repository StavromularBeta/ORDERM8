from connector import Connector


class CreateTb(Connector):
    def __init__(self):
        super(CreateTb, self).__init__()
        super(self.__class__, self).__init__()
        self.table_dictionary = {1: """ CREATE TABLE IF NOT EXISTS rolodex (
                                           id integer PRIMARY KEY,
                                           last_name text,
                                           first_name text,
                                           phone_number text,
                                           address text,
                                           pay_method text,
                                           status BOOLEAN,
                                           order_method text ) """,
                                 2: """ CREATE TABLE IF NOT EXISTS orders (
                                           id integer PRIMARY KEY,
                                           customer_id smallint,
                                           order_lines text,
                                           order_time text,
                                           delivery_time text ) """,
                                 3: """CREATE TABLE IF NOT EXISTS customer_preferences (
                                           id integer PRIMARY KEY,
                                           customer_id integer,
                                           field_id integer,
                                           description text) """,
                                 4: """CREATE TABLE IF NOT EXISTS day_duties (
                                          id integer PRIMARY KEY,
                                          date_of_entry DATE,
                                          day_of_week text,
                                          task text) """,
                                 5: """CREATE TABLE IF NOT EXISTS daily_customers (
                                          id integer PRIMARY KEY,
                                          custid SMALLINT,
                                          todays_date DATE )
                                    """
                                 }

    def create_table(self, dictionary_index):
        query = self.table_dictionary[dictionary_index]
        return self.connector(query)


#db = CreateTb()
#db.create_table(1)
#db.create_table(2)
#db.create_table(3)
#db.create_table(4)
#db.create_table(5)