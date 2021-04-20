from flask import Flask
import pymongo
from flask import Flask, render_template, redirect
from flask import Blueprint, request, jsonify
import datetime
app = Flask(__name__)


try:
    mongo = pymongo.MongoClient("localhost",port=27017,serverSelectionTimeoutMS=1000)

    mongo.server_info()

except:
    print( " ERROR - can't connect to db")


@app.route("/create", methods=["POST"])
def create_api():

    if request.method == "POST":
        data = request.json
        type = data.get("audioFileType", None)
        if type is None:
            return "The request is invalid: 400 bad request", 400
        metadata = data.get("audioFileMetadata")
        if type == "song":
            try:         
                name = metadata["name"]
                # check duration time and upload time
                if int(metadata["duration_time"]) <= 0:
                    metadata["duration_time"] = 0
                duaration = metadata["duration_time"]
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
                participants = metadata.get("participants")
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
                    host = metadata['host']
                    name = metadata["name"]
                    # check duration time and upload time
                    if int(metadata["duration_time"]) <= 0:
                        metadata["duration_time"] = 0
                    duaration = metadata["duration_time"]
                    if len(name)>100 :
                        return "The request is invalid: 400 bad request", 400 
                    if len(host)>100 :
                        return "The request is invalid: 400 bad request", 400
                except:
                    return "The request is invalid: 400 bad request", 400


                uploaded_time  = datetime.datetime.utcnow()
                id = mongo.audioserver.Podcast.estimated_document_count()
                id = int(id)+1
               
                try:
                    mongo.audioserver.Podcast.insert({'ID':id,'Name': name, 'Duration': duaration,'Uploaded_time': uploaded_time, 'Host': host, "Participants":participant_})
                    return "200 ok", 200
                except:
                    return "The request is invalid: 400 bad request", 400

               
        elif type == "audiobook":

            try:
                title = metadata['title']
                author = metadata["author"]
                narrator = metadata["narrator"]
                # check duration time and upload time
                if int(metadata["duration_time"]) <= 0:
                    metadata["duration_time"] = 0
                duaration = metadata["duration_time"]
                if len(title)>100 or len(author) >100 or len(narrator)>100:
                    return "The request is invalid: 400 bad request", 400 
                
            except:
                return "The request is invalid: 400 bad request", 400

            uploaded_time  = datetime.datetime.utcnow()
            id = mongo.audioserver.Audiobook.estimated_document_count()
            id = int(id)+1
               
            try:
                mongo.audioserver.Audiobooks.insert({'ID':id,'Title of the audiobook': title,'Author of the title':author, 'Narrator':narrator,'Duration': duaration,'Uploaded_time': uploaded_time })
                return "200 ok", 200
            except:
                
                return "The request is invalid: 400 bad request", 400
        else:
            return "The request is invalid: 400 bad request", 400


    return "The request is invalid: 400 bad request", 400

            

if __name__ == "__main__":
    app.run(debug=True)