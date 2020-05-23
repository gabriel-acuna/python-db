from conf.settings  import get_db_credentials
import peewee

class DBConnection:

    def __init__(self):
        credentials = get_db_credentials()
        self.__connection=peewee.MySQLDatabase(
                credentials['DB'],
                host=credentials['HOST'],
                port=3306,
                user= credentials['USER'],
                password = credentials['PASSWORD']
            )
    
    def get_connection(self):
        return self.__connection

