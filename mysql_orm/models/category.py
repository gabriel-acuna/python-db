import datetime
import peewee
from conf.connection import DBConnection
from models.products import Product
db = DBConnection()


class Category(peewee.Model):
    name = peewee.CharField(max_length=100)
    description = peewee.TextField()
    created_date = peewee.DateTimeField(default=datetime.datetime.now)
  
    class Meta:
        database = db.get_connection()
        db_table = 'categories'

    def __str__(self):
        return f'{self.name}'


class CategoriesProducts(peewee.Model):
    product = peewee.ForeignKeyField(Product, related_name='categories')
    category = peewee.ForeignKeyField(Category, related_name='products')

    class Meta:
        database = db.get_connection()
        bd_table = 'categories_products'

    def __str__(self):
        return f'{self.product} - {self.category}'