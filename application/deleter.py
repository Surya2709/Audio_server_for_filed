import datetime
from application import database


mongo = database.mongo

def delete(audioFileType,audioFileID):
    if audioFileType =="song":
        
        try:
            mongo.audioserver.Song.delete_one({"ID":int(audioFileID)})
            return "200 ok",200
        except:
            return "Internal server error ", 500

    elif audioFileType =="podcast":
        id = str(audioFileID)
        try:
            mongo.audioserver.Podcast.delete_one({"ID":int(audioFileID)})
            return "200 ok",200
        except:
            return "Internal server error ", 500
    elif audioFileType =="audiobook":
        id = str(audioFileID)
        try:
            mongo.audioserver.Audiobooks.delete_one({"ID":int(audioFileID)})
            return "200 ok",200
        except:
            return "Internal server error ", 500
    else:
        return "The request is invalid: 400 bad request", 400

