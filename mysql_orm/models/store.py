from conf.connection import DBConnection
from models.user import User
import datetime
import peewee

db = DBConnection()

class Store(peewee.Model):
    #user = peewee.ForeignKeyField(User, primary_key=True) #One to one ralationship
    user = peewee.ForeignKeyField(User, related_name='stores') #One to many ralationship
    name = peewee.CharField(max_length=50)
    address = peewee.TextField()
    active = peewee.BooleanField(default=True)
    created_date = peewee.DateTimeField(default=datetime.datetime.now())

    class Meta:
        database = db.get_connection()
        db_table = 'stores'