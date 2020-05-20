from conf.settings  import get_db_credentials
import mysql.connector
from mysql.connector import Error
class DBConnection:

    def __init__(self):
       self.__connection=None
       self.__cursor=None

    
    def connect(self):
        try:
            credentials = get_db_credentials()
            self.__connection = mysql.connector.connect(
                host=credentials['HOST'],
                database=credentials['DB'],
                user= credentials['USER'],
                password = credentials['PASSWORD']
            )
            if self.__connection.is_connected():
                self.__cursor = self.__connection.cursor()
        except Error as error:
            print(error)
    
    def get_connection(self):
        return self.__connection

    def execute_query(self, stmts):
        try:
            self.__cursor.execute(stmts)
            return self.__cursor
        except Error as error:
            print(error)
    
    def close_connection(self):
        if self.__connection:
            self.__cursor.close()
            self.__connection.close()


    def get_cursor(self):
        return self.__cursor
