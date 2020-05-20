# database connection class
from conf.connection import DBConnection

db = DBConnection()

# SAMPLES

'''
 Create a table 
 @params  
 connection: DBConnection
 table_name: String
 table_def: String

'''
from  mysql_samples.create_table import CreateTable

name = 'users'
columns_def = '''
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
'''

new_table = CreateTable(db,name, columns_def)
print(new_table.create_table())

'''
 Insert data
 @params  
 connection: DBConnection
 table_name: String
 table_columns: String
 values: []
'''
from mysql_samples.insert_data import InsertData

columns = 'username, password'
values = []

user_name = input('Insert the username:\n')
values.append(user_name)
password = input('Insert the password:\n')
values.append(password)

new_row =  InsertData(db, name, columns, tuple(values))
print(new_row.insert())

'''
Fetch data
 @params  
 connection: DBConnection
 table_name: String
 table_columns: String
 conditions: String
'''
from mysql_samples.fetch_data import FetchData

print(f'-------- *{name.upper()}* --------')
users = FetchData(db, name)
print(users.getRows())

u = users.getRowById(1)
print(f'''
*****  User ****
  id: {u[0]}
  name: {u[1]}
''')

'''
Upadte data
 @params  
 connection: DBConnection
 table_name: String
 conditions: String
 params = String
'''
from mysql_samples.update_row import UpdateData

user_update = UpdateData(db,name, "username='gstef09', password='&hg6t5708RCT'", 'WHERE id=1')
print(user_update.update())


'''
Upadte data
 @params  
 connection: DBConnection
 table_name: String
 conditions: String
'''

from mysql_samples.delete_row import DeleteRow

user_deleted = DeleteRow(db, name, 'WHERE id =1')
print(user_deleted.delete())
    
