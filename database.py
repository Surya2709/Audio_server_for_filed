
from flask import Flask
import pymongo

import datetime

mongo = pymongo.MongoClient("localhost",port=27017,serverSelectionTimeoutMS=1000)
db =mongo
mongo.server_info()


class AudioBook(db.Song):
    __tablename__ = "audiobook"
    uploaded_time = Column(
        db.DateTime, default=db.func.now(), nullable=False, onupdate=datetime.utcnow()
    )
    duration_time = Column(db.Integer, default=0, nullable=False)
    title = Column(db.String(100), nullable=False)
    author = Column(db.String(100), nullable=False)
    narrator = Column(db.String(100), nullable=False)

class Podcast():
    uploaded_time = Column(
        db.DateTime, default=db.func.now(), nullable=False, onupdate=datetime.utcnow()
    )
    duration_time = Column(db.Integer, default=0, nullable=False)
    __tablename__ = "podcast"
    name = Column(db.String(100), nullable=False)
    host = Column(db.String(100), nullable=False)
    participents = Column(db.Text, nullable=False)


class Song(db.audioserver.Song):
    name = 
    uploaded_time = 
    duration_time =
    