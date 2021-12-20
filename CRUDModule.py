from pymongo import MongoClient
from pprint import pprint
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password, database):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        self.username = username
        self.password = password
        self.client = MongoClient('mongodb://%s:%s@localhost:33360/%s' % (username, password, database))
        self.database = self.client['AAC']

# C (Create) method in CRUD
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary
            return print("True")
        else:
            raise Exception('Nothing to save, because data parameter is empty')
            
 # R (Read) method in CRUD
    def read(self, data):
        array = list(self.database.animals.find(data, {"_id":False}))
        if len(array) == 0:
            print("No matches were found")
        else:
            #print(self.database.animals.find(data))
            return self.database.animals.find(data, {"_id":False})
        
 # U (Update) method in CRUD
    def update(self, query, data):
        x = self.database.animals.update_many(query, data)
        if x.modified_count == 0:
            print("Did not find any search results with that query.")
        else:
            print(x.modified_count, "documents updated.")
            
 # D (Delete) method in CRUD
    def delete(self, data):
        x = self.database.animals.delete_many(data)
        if x.deleted_count == 0:
            print("Did not find any search results with that query to delete.")
        else:
            print(x.deleted_count, "documents deleted.")
  
            