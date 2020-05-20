from mysql_samples.fetch_data import FetchData
class InsertData:

    def __init__(self, connection, table_name, colums, *values):
        self.__connection = connection
        self.__table_name = table_name
        self.__table_colums = colums
        self.__values = values
    
    def insert(self):
        try:
            self.__connection.connect()
            stmt = f'''
                INSERT INTO  {self.__table_name} 
                    ({self.__table_colums})
                    values
                        {self.__values[0]}
                    
            '''
            self.__connection.execute_query(stmt)
            self.__connection.get_connection().commit()
            return f'\nThis row: {self.__values[0]} has been inserted'
        
           
        except Exception as ex:
            return ex
