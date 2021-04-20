import pymongo


try:
    mongo = pymongo.MongoClient("localhost",port=27017,serverSelectionTimeoutMS=1000)

    mongo.server_info()
except:
    print( " ERROR - can't connect to db ")
