import datetime
from application import database


mongo = database.mongo

def delete(audioFileType,audioFileID):
    if audioFileType =="song":
        id = str(audioFileID)
        try:
            mongo.audioserver.Song.delete_one({"ID": id})
            return "200 ok",200
        except:
            return "The request is invalid: 400 bad request", 400

    elif audioFileType =="podcast":
        id = str(audioFileID)
       try:
            mongo.audioserver.Podcast.delete_one({"ID":id})
            return "200 ok",200
        except:
            return "The request is invalid: 400 bad request", 400

    elif audioFileType =="audiobook":
        id = str(audioFileID)
        try:
            mongo.audioserver.Audiobooks.delete_one({"ID":id})
            return "200 ok",200
        except:
            return "The request is invalid: 400 bad request", 400
    else:
        return "The request is invalid: 400 bad request", 400

