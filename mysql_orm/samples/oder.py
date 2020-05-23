from models.user import User
# count
count = User.select().count()
print(count, '\n\n')

#order
users = User.select().order_by(User.username.asc())
for user in users:
    print(user)

#handle exceptions 

try:
    user = User.get(User.id==8)
except User.DoesNotExist as e:
    print('User doesn\'t exist ')