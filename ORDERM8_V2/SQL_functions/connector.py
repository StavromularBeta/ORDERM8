import os, sys, inspect
import sqlite3
# below 3 lines add the parent directory to the path, so that SQL_functions can be found.
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
database_target = parentdir + "/database_files/ORDERM8V2.db"


class Connector(object):
    def __init__(self):
        self.database_target = parentdir + "/database_files/ORDERM8V2.db"

    def connector(self, query):
        db_connection = sqlite3.connect(self.database_target)
        cursor = db_connection.cursor()
        cursor.execute(query)
        db_connection.commit()
        returned_query = cursor
        return returned_query


