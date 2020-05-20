class CreateTable:

    def __init__(self, connection, table_name, table_def):

        self.__connection = connection
        self.__table_name = table_name
        self.__table_def = table_def

    def create_table(self):
        try:
            self.__connection.connect()
            self.__connection.execute_query(
                f'DROP TABLE IF EXISTS {self.__table_name}')
            self.__connection.execute_query(f'''
                CREATE TABLE {self.__table_name} (
                    {self.__table_def}
                )
            ''')
            msg = f'\nThe table {self.__table_name} has been created'
            self.__connection.execute_query('SHOW TABLES')
            msg += '\n-------- TABLES --------\t'
            tables = self.__connection.get_cursor().fetchall()
            for table in tables[0]:
                msg += f'\n* {table}'
            return msg
        except Exception as ex:
           return ex
