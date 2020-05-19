class CreateTable:
    
    def __init__(self, connection, table_name, table_def):
      
        self.connection = connection
        self.table_name = table_name
        self.table_def = table_def
    
    
    def create_table(self):
        try:
            self.connection.connect()
            self.connection.execute_query(f'DROP TABLE IF EXISTS {self.table_name}')
            self.connection.execute_query(f'''
                CREATE TABLE {self.table_name} (
                    {self.table_def}
                )
            ''')
            self.connection.execute_query('SHOW TABLES')
            tables = self.connection.get_cursor().fetchall()
            for table in tables:
                print(table)

            print(f'the table {self.table_name} has been created')
        except Exception as ex:
            print(ex)
