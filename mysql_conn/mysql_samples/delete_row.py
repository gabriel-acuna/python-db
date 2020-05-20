class DeleteRow:
    def __init__(self, connection, table_name, conditions):
        self.__connection = connection
        self.__table_name = table_name
        self.__conditions = conditions

    def delete(self):
        stm = f"DELETE FROM {self.__table_name}  {self.__conditions}"
        try:
            self.__connection.connect()
            self.__connection.execute_query(stm)
            self.__connection.get_connection().commit()
            return f'Rows deleted: {self.__connection.get_cursor().rowcount}'
        except Exception as ex:
            return ex
