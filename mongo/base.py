import pymongo

def create_collection(database, name):
    return database[name]

def create_database(client, name):
    return client[name]

def connect():
    client =  pymongo.MongoClient("mongodb://localhost:27017/")
    return client

def collection_exits(database, name):
    if name in database.list_collection_names():
        print ("Collection Exists") 

def database_exists(client, name):
    if name in client.list_database_name():
        print ("Database Exists")

def delete_all(collection):
    return collection.delete_many({})

def find_one(collection):
    print (collection.find_one())

def find_all(collection):
    for x in collection.find().sort():
        print (x)     

def find_some(collection, data):
    results =  collection.find(data)
    for result in results:
        print (result) 

def insert_many_collection(collection, data):
    return collection.insert_many(data)

def insert_one_collection(collection, data):
    return collection.insert_one(data)

def log_exists(collection, data):
    return  collection.find(data).count()

def show_collections(database):
    return database.list_collection_names()

def show_databases(client):
    for database in client.list_database_names():
        print("database: " + database)

def show_last(collection):
    for x in collection.find().sort("timestamp", -1).limit(1):
        print (x)

def sort_collection(collection):
    for x in collection.find().sort('timestamp'):
        print (x)
        

        


