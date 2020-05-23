from models.user import User
from models.store import Store
from models.products import Product
from models.category import Category, CategoriesProducts

if CategoriesProducts.table_exists:
    CategoriesProducts.drop_table()

if Category.table_exists():
    Category.drop_table()

if Product.table_exists():
    Product.drop_table()

if Store.table_exists():
    Store.drop_table()

if User.table_exists():
    User.drop_table()

User.create_table()
Store.create_table()
Product.create_table()
Category.create_table()
CategoriesProducts.create_table()

# Insert data

# 1
user1 = User()
user1.username = 'Gabriel'
user1.password = 'xfT66v5ii'
user1.email = 'g.1000@mail.com'
user1.save()

# 2
user = User(username='Mariana', password='Qdytu64', email='mary762@mail.com')
user.save()

# 3
user = {'username': 'Jesenia', 'password': 'M8y7tbd'}
user = User(**user)
user.save()

# 4
user = User.create(username='Stefano', password='JCXS34y99')
store1 = Store.create(name='StefTech', adddress='S/N', user=user)
store2 = Store.create(name='M & G Store', adddress='S/N', user=user)
print(store1.name, store2.name)

Product.create(store_id=1, name='SSD',
               description='SSD Kingston 500 GB', price=360.8, stock=50)
Product.create(store_id=1, name='Hard Disk',
               description='HDD Toshiba 2 TB', price=280, stock=100)
Product.create(store_id=1, name='USB Memory',
               description='USB Memmory Kingston 64 GB', price=32.9, stock=80)
Product.create(store_id=1, name='Enclosure hdd',
               description='Enclosure hdd 2.5 USB 3.0', price=12.9, stock=80)

Product.create(store_id=2, name='T-Shirt',
               description='Custom T-Shirt', price=10.0, stock=50)
Product.create(store_id=2, name='Cap',
               description='Custom Cup', price=20.5, stock=100)
Product.create(store_id=2, name='Portrait',
               description='Custom Portrait', price=29, stock=80)
Product.create(store_id=2, name='Key Chain',
               description='Custom Key Chain', price=4.9, stock=80)

# 5
query = User.insert(username='Elizabeth', password='N7yg5r55dd')
query.execute()

# Create categories

Category.create(name='Storage', description='Storage')
Category.create(name='Kingstong', description='Kingstong')
Category.create(name='Toshiba', description='Toshiba')
Category.create(name='Accesory', description='Accesory')
Category.create(name='Custom', description='Custom')
Category.create(name='Clothes', description='Clothes')

CategoriesProducts.create(product=1, category=1)
CategoriesProducts.create(product=1, category=2)
CategoriesProducts.create(product=2, category=1)
CategoriesProducts.create(product=2, category=3)
CategoriesProducts.create(product=3, category=1)
CategoriesProducts.create(product=3, category=2)
CategoriesProducts.create(product=1, category=1)
CategoriesProducts.create(product=4, category=1)
CategoriesProducts.create(product=4, category=4)

CategoriesProducts.create(product=5, category=5)
CategoriesProducts.create(product=5, category=6)
CategoriesProducts.create(product=6, category=4)
CategoriesProducts.create(product=6, category=5)
CategoriesProducts.create(product=7, category=4)
CategoriesProducts.create(product=7, category=5)
CategoriesProducts.create(product=8, category=4)
CategoriesProducts.create(product=8, category=5)






