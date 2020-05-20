class UpdateData:

    def __init__(self, connection, table_name,params, conditions=None ):
        self.__connection = connection
        self.__table_name = table_name
        self.__params = params
        self.__conditions = conditions
    
    def update(self):
        stm = f"UPDATE {self.__table_name} SET {self.__params}"
        if self.__conditions: stm+=f" {self.__conditions}"
        
        try:
            self.__connection.connect()
            self.__connection.execute_query(stm)
            self.__connection.get_connection().commit()
            return f'Rows updated: {self.__connection.get_cursor().rowcount}'
        except Exception as ex:
            return ex
        