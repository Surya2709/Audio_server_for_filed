import datetime
from application import database
from flask import jsonify
from database import Mongo
from settings import DATABASE_URL,DB_PORT


class CRUD:
    def __init__(self,data=None,audioFileType=None,audioFileID=None):
        self.data = data
        self.audioFileType = audioFileType
        self.audioFileID = audioFileID
        self.port = DB_PORT
        self.host = DATABASE_URL
        self.timeout = 1000
        self.Mongo_instance = Mongo(host=self.host,port=self.port,time_out=self.timeout)
        self.mongo = self.Mongo_instance.create_session()


    def create(self):
        type = self.data.get("audioFileType", None)
        if type is None:
            return "The request is invalid: 400 bad request", 400
        metadata = self.data.get("audioFileMetadata")
        if type == "song":
            try:         
                name = metadata["Name"]
                # check duration time and upload time
                if int(metadata["Duration_time"]) <= 0:
                    metadata["Duration_time"] = 0
                duration = metadata["Duration_time"]
                if len(name)>100 :
                    return "The request is invalid: 400 bad request", 400               
            except:
                    return "The request is invalid: 400 bad request", 400
            uploaded_time  = datetime.datetime.utcnow()
            id = self.mongo.audioserver.Song.count()
            id = id+1
            try:
                self.mongo.audioserver.Song.insert({'ID':id,'Name': name, 'Duration': duration,'Uploaded_time': uploaded_time})
                return "200 ok", 200
            except:
                
                return "Internal server error ", 500

        elif type == "podcast":
            participant_ = ""
            try:
                participants = metadata.get("Participants")
            except:
                participant_ = ""
            if participants is None:
                participant_ = ""
            else:
                if (
                    len(participants) > 10
                    or any(i for i in participants if len(i) > 100)
                ):      
                    return "The request is invalid: 400 bad request", 400
                participant_ = ",".join(participants)
                
                try:
                    host = metadata['Host']
                    name = metadata["Name"]
                    # check duration time and upload time
                    if int(metadata["Duration_time"]) <= 0:
                        metadata["Duration_time"] = 0
                    duration = metadata["Duration_time"]
                    if len(name)>100 :
                        return "The request is invalid: 400 bad request", 400 
                    if len(host)>100 :
                        return "The request is invalid: 400 bad request", 400
                except:
                    return "The request is invalid: 400 bad request", 400
                uploaded_time  = datetime.datetime.utcnow()
                id = self.mongo.audioserver.Podcast.count()
                id = int(id)+1
                
                try:
                    self.mongo.audioserver.Podcast.insert({'ID':id,'Name': name, 'Duration': duration,'Uploaded_time': uploaded_time, 'Host': host, "Participants":participant_})
                    return "200 ok", 200
                except:
                    return "Internal server error ", 500

                
        elif type == "audiobook":

            try:
                title = metadata['Title']
                author = metadata["Author"]
                narrator = metadata["Narrator"]
                # check duration time and upload time
                if int(metadata["Duration_time"]) <= 0:
                    metadata["Duration_time"] = 0
                duration = metadata["Duration_time"]
                if len(title)>100 or len(author) >100 or len(narrator)>100:
                    return "The request is invalid: 400 bad request", 400  
            except:
                return "The request is invalid: 400 bad request", 400

            uploaded_time  = datetime.datetime.utcnow()
            id = self.mongo.audioserver.Audiobooks.count()
            id = int(id)+1
                
            try:
                self.mongo.audioserver.Audiobooks.insert({'ID':id,'Title': title,'Author':author, 'Narrator':narrator,'Duration': duration,'Uploaded_time': uploaded_time })
                return "200 ok", 200
            except:
                return "Internal server error ", 500
        else:
            return "The request is invalid: 400 bad request", 400



    def delete(self):
        if self.audioFileType =="song":
            
            try:
                self.mongo.audioserver.Song.delete_one({"ID":int(self.audioFileID)})
                return "200 ok",200
            except:
                return "Internal server error ", 500

        elif self.audioFileType =="podcast":
        
            try:
                self.mongo.audioserver.Podcast.delete_one({"ID":int(self.audioFileID)})
                return "200 ok",200
            except:
                return "Internal server error ", 500
        elif self.audioFileType =="audiobook":
            
            try:
                self.mongo.audioserver.Audiobooks.delete_one({"ID":int(self.audioFileID)})
                return "200 ok",200
            except:
                return "Internal server error ", 500
        else:
            return "The request is invalid: 400 bad request", 400


    def get(self):
        
        if self.audioFileType=="song":
            try:
                out = []
                if self.audioFileID is not None:
                    songs = self.mongo.audioserver.Song.find({'ID':int(self.audioFileID)})
                    for song in songs:
                        out.append({"Name":song["Name"],"Duration":song["Duration"],"Uploaded_time":song["Uploaded_time"]})
                    response = jsonify({'songs': out })
                    return response, 200

                else : 
                    songs = self.mongo.audioserver.Song.find()
                    for song in songs:
                        out.append({"Name":song["Name"],"Duration":song["Duration"],"Uploaded_time":song["Uploaded_time"]})
                    response = jsonify({'songs': out })
                    return response, 200
            except:
                return "Internal server error ", 500

        elif self.audioFileType=="podcast":
            try:
                out = []
                if self.audioFileID is not None:
                    podcasts = self.mongo.audioserver.Podcast.find({'ID':int(self.audioFileID)})
                    for podcast in podcasts:
                        out.append({"Name":podcast["Name"],"Duration":podcast["Duration"],"Uploaded_time":podcast["Uploaded_time"], "Host":podcast["Host"],"Participants":podcast["Participants"]})
                    response = jsonify({'podcasts': out })
                    return response, 200

                else : 
                    podcasts = self.mongo.audioserver.Podcast.find()
                    for podcast in podcasts:
                        out.append({"Name":podcast["Name"],"Duration":podcast["Duration"],"Uploaded_time":podcast["Uploaded_time"], "Host":podcast["Host"],"Participants":podcast["Participants"]})
                    response = jsonify({'podcasts': out })
                    return response, 200
            except:
                return "Internal server error ", 500

        elif self.audioFileType=="audiobook":
            try:
                out = []
                if self.audioFileID is not None:
                    audiobooks = self.mongo.audioserver.Audiobooks.find({'ID':int(self.audioFileID)})
                    for audiobook in audiobooks:
                        out.append({"Title":audiobook["Title"],"Duration":audiobook["Duration"],"Uploaded_time":audiobook["Uploaded_time"],"Author":audiobook["Author"],"Narrator":audiobook['Narrator']})
                    response = jsonify({'audiobooks': out })
                    return response, 200

                else : 
                    audiobooks = self.mongo.audioserver.Audiobooks.find()
                    for audiobook in audiobooks:
                        out.append({"Title":audiobook["Title"],"Duration":audiobook["Duration"],"Uploaded_time":audiobook["Uploaded_time"],"Author":audiobook["Author"],"Narrator":audiobook['Narrator']})
                    response = jsonify({'audiobooks': out })
                    return response, 200 
            except:
                return "Internal server error ", 500
        else:
            return "The request is invalid: 400 bad request", 400
        return "The request is invalid: 400 bad request", 400




    def update(self):

        metadata = self.data.get("audioFileMetadata")

        if self.audioFileType == "song":
            for item in metadata:
                if item =="Uploaded_time":
                    metadata['Uploaded_time'] = str(datetime.datetime.utcnow())
                if item not in ["Uploaded_time","Duration_time","Name"]:
                    
                    return "The request is invalid: 400 bad request", 400
            try:
                name = metadata["Name"]
                if len(name)>100 :
                    return "The request is invalid: 400 bad request", 400               
    
                duration = metadata["Duration_time"]
                uploaded_time = metadata["Uploaded_time"]

            except:
                return "The request is invalid: 400 bad request", 400
            try: 
                self.mongo.audioserver.Song.update_one({'ID':int(self.audioFileID)},{"$set":{'Name': name,'Duration':duration , 'Uploaded_time':uploaded_time}})
                return "200 ok", 200
            except:
                return "Internal Server Error : 500",500
            

        elif self.audioFileType == "podcast":

            for item in metadata:
                if item =="Uploaded_time":
                    metadata['Uploaded_time'] = str(datetime.datetime.utcnow())
                if item not in ["Uploaded_time","Duration_time","Name","Host","Participants"]:
                    print("here")
                    return "The request is invalid: 400 bad request", 400
            try:
                name = metadata["Name"]
                host = metadata["Host"]
                if len(name)>100 :
                    return "The request is invalid: 400 bad request", 400 
                if len(host)>100 :
                    return "The request is invalid: 400 bad request", 400

                duration = metadata["Duration_time"]
                uploaded_time = metadata["Uploaded_time"]
                    
                participant_ = ""
                try:
                    participants = metadata.get("Participants")
                except:
                    participant_ = ""
                if participants is None:
                    participant_ = ""
                else:
                    if (
                        len(participants) > 10
                        or any(i for i in participants if len(i) > 100)
                    ):
                        
                        return "The request is invalid: 400 bad request", 400
                    participant_ = ",".join(participants)            
            except:
                return "The request is invalid: 400 bad request", 400
            try: 
                self.mongo.audioserver.Podcast.update_one({'ID':int(self.audioFileID)},{"$set":{'Name': name, 'Duration': duration,'Uploaded_time': uploaded_time, 'Host': host, "Participants":participant_}})
                return "200 ok", 200
            except:
                return "Internal Server Error : 500",500

        elif self.audioFileType == "audiobook":
            for item in metadata:
                if item =="Uploaded_time":
                    metadata['Uploaded_time'] = str(datetime.datetime.utcnow())
                if item not in ["Uploaded_time","Duration_time","Title","Author","Narrator"]:
                    
                    return "The request is invalid: 400 bad request", 400
            try:
                title = metadata["Title"]
                author = metadata["Author"]
                narrator = metadata["Narrator"]
                if len(title)>100 or len(author) >100 or len(narrator)>100:
                    return "The request is invalid: 400 bad request", 400 
                duration = metadata["Duration_time"]
                uploaded_time = metadata["Uploaded_time"]
                    
                    
            except:
                return "The request is invalid: 400 bad request", 400
            try: 
                self.mongo.audioserver.Audiobooks.update_one({'ID':int(self.audioFileID)},{"$set":{'Title': title,'Author':author, 'Narrator':narrator,'Duration': duration,'Uploaded_time': uploaded_time }})
                return "200 ok", 200
            except:
                return "Internal Server Error : 500",500
        else:
            return "The request is invalid: 400 bad request", 400
        return "The request is invalid: 400 bad request", 400














