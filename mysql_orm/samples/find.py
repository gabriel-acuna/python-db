from models.user import User
#1
user1 = User.get_by_id(1)
print(user1)
query = User.update(active=False).where(User.id == 1)
query.execute()

# 2 
user2 = User.get(User.username =='Elizabeth')
print(user2)

user2.email = 'ely17@mail.com'
user2.save()

users_no_email = User.select().where(User.email >> None)
print('\n\n')
for u in users_no_email:
    print(u)


user = User.get_by_id(4)
print(f'\n\n User: {user.username} \nStores')
for store in user.stores:
    print(store.name)