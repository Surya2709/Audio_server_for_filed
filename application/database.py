import pymongo


class Mongo:
    def __init__(self,host,port,time_out):

        self.host = host
        self.port = int(port)
        self.timeout = time_out
    def create_session(self):
        mongo = pymongo.MongoClient(self.host,port=self.port,serverSelectionTimeoutMS=self.timeout)
        mongo.server_info()
        return mongo
    
