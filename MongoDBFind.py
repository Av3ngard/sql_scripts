from pymongo import MongoClient
#Step 1: Connect to MongoDB - Note: Change connection string as needed where "mongodb://youruser:password@instanceip:port/"
client = MongoClient("mongodb://user:password@host:port/")
for iter in range(100000):
    db=client.test
    test=db.test
    #Step 2: Find data
    for test in test.find():
        print(test)
client.close()