class FetchData:

    def __init__(self, connection, table_name, columns='*', conditions=None):
        self.__connection = connection
        self.__table_name = table_name
        self.__columns = columns
        self.__conditions = conditions

    def getRows(self):
        try:
            self.__connection.connect()
            stm = f'SELECT {self.__columns}  FROM {self.__table_name}'
            if self.__conditions:
                stm += f' {self.__conditions}'
            self.__connection.execute_query(stm)
            return self.__connection.get_cursor().fetchall()
        except Exception as ex:
           return ex


    def getRowById(self,id):
        try:
            self.__connection.connect()
            self.__connection.execute_query(f'SELECT {self.__columns}  FROM {self.__table_name} WHERE id={id}')
            return self.__connection.get_cursor().fetchone()
            
        except Exception as ex:
            return ex