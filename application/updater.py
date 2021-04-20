import datetime
from application import database


mongo = database.mongo

def update(data,audioFileType,audioFileID):

    metadata = data.get("audioFileMetadata")


    if audioFileType == "song":
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
            mongo.audioserver.Song.update_one({'ID':int(audioFileID)},{"$set":{'Name': name,'Duration':duration , 'Uploaded_time':uploaded_time}})
            return "200 ok", 200
        except:
            return "Internal Server Error : 500",500
        

    elif audioFileType == "podcast":

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
            mongo.audioserver.Podcast.update_one({'ID':int(audioFileID)},{"$set":{'Name': name, 'Duration': duration,'Uploaded_time': uploaded_time, 'Host': host, "Participants":participant_}})
            return "200 ok", 200
        except:
            return "Internal Server Error : 500",500

    elif audioFileType == "audiobook":
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
            mongo.audioserver.Audiobooks.update_one({'ID':int(audioFileID)},{"$set":{'Title': title,'Author':author, 'Narrator':narrator,'Duration': duration,'Uploaded_time': uploaded_time }})
            return "200 ok", 200
        except:
            return "Internal Server Error : 500",500
    else:
        return "The request is invalid: 400 bad request", 400
    return "The request is invalid: 400 bad request", 400

