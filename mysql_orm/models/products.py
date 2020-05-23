import datetime
import peewee
from conf.connection import DBConnection
from models.store import Store
db = DBConnection()

class Product(peewee.Model):
    name = peewee.CharField(max_length=100)
    description = peewee.TextField()
    store = peewee.ForeignKeyField(Store, related_name='products') #ForeignKeyField allows for a backreferencing property to be bound to the target model. Implicitly, this property will be named classname_set, where classname is the lowercase name of the class, but can be overridden via the parameter related_name:
    price = peewee.DecimalField(max_digits=5, decimal_places=2) #100.00
    stock = peewee.IntegerField()
    created_date = peewee.DateTimeField(default=datetime.datetime.now)
  
    class Meta:
        database = db.get_connection()
        db_table = 'products'

    def __str__(self):
        return '{name} - ${price}'.format(name=self.name, price=self.price)
