from models.products import Product
from models.store import Store
from models.user import User
from models.category import *

query = (
    Product.select()
    .join(Store)
    .join(User)
    .where(User.id==4)
    .order_by(Product.price.desc())

)

for p in query:
    print(p)

print('\n','*'*10,' Categories ', '*'*10)
categories = Category.select()
for c in categories:
    print('\t *',c)
    for product in c.products:
        print('\t\t *',product)