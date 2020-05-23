from conf.connection import DBConnection
import datetime
import peewee

db = DBConnection()
class User(peewee.Model):
    username = peewee.CharField(unique=True, max_length=50, index=True)
    password = peewee.CharField(max_length=50)
    email = peewee.CharField(max_length=50, null=True)
    active = peewee.BooleanField(default=True)
    created_at = peewee.DateTimeField(default=datetime.datetime.now())

    class Meta:
        database = db.get_connection()
        db_table = 'users'
    
    def __str__(self):
        return self.username