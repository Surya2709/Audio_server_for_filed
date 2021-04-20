import datetime
from application import database


mongo = database.mongo


def create(data):
    type = data.get("audioFileType", None)
    if type is None:
        return "The request is invalid: 400 bad request", 400
    metadata = data.get("audioFileMetadata")
    if type == "song":
        try:         
            name = metadata["Name"]
            # check duration time and upload time
            if int(metadata["Duration_time"]) <= 0:
                metadata["Duration_time"] = 0
            duaration = metadata["Duration_time"]
            if len(name)>100 :
                return "The request is invalid: 400 bad request", 400               
        except:
                return "The request is invalid: 400 bad request", 400
        uploaded_time  = datetime.datetime.utcnow()
        id = mongo.audioserver.Song.count()
        id = id+1
        try:
            mongo.audioserver.Song.insert({'ID':id,'Name': name, 'Duration': duaration,'Uploaded_time': uploaded_time})
            return "200 ok", 200
        except:
            
            return "The request is invalid: 400 bad request", 400

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
                duaration = metadata["Duration_time"]
                if len(name)>100 :
                    return "The request is invalid: 400 bad request", 400 
                if len(host)>100 :
                    return "The request is invalid: 400 bad request", 400
            except:
                return "The request is invalid: 400 bad request", 400


            uploaded_time  = datetime.datetime.utcnow()
            id = mongo.audioserver.Podcast.count()
            id = int(id)+1
            
            try:
                mongo.audioserver.Podcast.insert({'ID':id,'Name': name, 'Duration': duaration,'Uploaded_time': uploaded_time, 'Host': host, "Participants":participant_})
                return "200 ok", 200
            except:
                return "The request is invalid: 400 bad request", 400

            
    elif type == "audiobook":

        try:
            title = metadata['Title']
            author = metadata["Author"]
            narrator = metadata["Narrator"]
            # check duration time and upload time
            if int(metadata["Duration_time"]) <= 0:
                metadata["Duration_time"] = 0
            duaration = metadata["Duration_time"]
            if len(title)>100 or len(author) >100 or len(narrator)>100:
                return "The request is invalid: 400 bad request", 400 
            
        except:
            return "The request is invalid: 400 bad request", 400

        uploaded_time  = datetime.datetime.utcnow()
        id = mongo.audioserver.Audiobooks.count()
        id = int(id)+1
            
        try:
            mongo.audioserver.Audiobooks.insert({'ID':id,'Title': title,'Author':author, 'Narrator':narrator,'Duration': duaration,'Uploaded_time': uploaded_time })
            return "200 ok", 200
        except:
            
            return "The request is invalid: 400 bad request", 400
    else:
        return "The request is invalid: 400 bad request", 400
