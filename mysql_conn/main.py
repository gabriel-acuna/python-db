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
try:
    new_table = CreateTable(db,name, columns_def)
    new_table.create_table()
except  Exception as ex:
    print(ex)







    
