from pymongo import MongoClient
import re

client = MongoClient()

db = client['py_mongo_workshop']

if __name__  == '__main__':
    users = [
        {
        'username':'g.acuna00',
        'first_name': 'Gabriel',
        'last_name':'Acuña',
        'email':'g.acuna@mail.com'
    },
    {
        'username':'m.cob15',
        'first_name': 'Mariana',
        'last_name':'Cobeña',
        'email':'m.cobena@mail.com'
    }
    ]

    db.users.drop()
    db.users.insert_many(users)

  
    rgx = re.compile('G')
    user = db.users.find_one({'first_name':rgx})
    print('\n'*2, user)

    # update 
    import datetime
    db.users.update_one({'username': 'm.cob15'}, {'$set' : { 'birth_date' : datetime.datetime(1992,7,15)}  })

    

    #delete 
    db.users.delete_one({'username':'g.acuna93'})

    for user in db.users.find():
        print(user)