import pymongo


def create_db():
    print("Welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['HashCode']
    collection = db['User_list']

    dictionary = {'Name_of_user':"ABC",'Bed_time':"11.30PM",'Wake_up_time':"6.30AM",'Hours_of_sleep':"x"} #content of each field
    collection.insert_one(dictionary)

    
create_db()