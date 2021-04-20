# Audio_server_for_filed
Web API that simulates the behavior of an audio file  server while using a MongoDB / SQL database.


FrameWork = Flask
Database = MongoDB



Setup codebase

clone the code in a directory

https://github.com/Surya2709/Audio_server_for_filed.git

go in the directory cd filed_audio_file_server

install all project requirements, use command python -m pipenv install -r requirements.txt


set up flask env variable, run commands

export FLASK_APP=main.py
export FLASK_ENV=developement


to run  in cmd:

    set FLASK_ENV = development

    set FLASK_APP = app.py 

    flask run

Create database

Donwload and install mongodb in local system and create a database named "audioserver"


Run the command     flask run

check if the server is running goto localhost:5000/ you will get a server running message


How to TEST APIS
The Test api structure is given in documentation.

API's End point 
The API has 4 End Point.

1. create api 


        url = /api/create 
        method = Post
        content-type=application/json

    structure:

        song :
            request body:

                        {
                        "audioFileType":"song",
                        "audioFileMetadata":{
                            "Uploaded_time":"100",
                            "Duration_time":"100",
                            "Name":"hello hello"
                            }
                        }


        podcast : 
            request body:


                            {
                                "audioFileType":"podcast",
                                "audioFileMetadata":{
                                        "Uploaded_time":"0",
                                        "Duration_time":102,
                                        "Name":"in the end.mp4",
                                        "Host":"linkin park - arizona park",
                                        "Participants":["linkin park","us","american band"]
                                }
                            }     


        audio book :
            request body:

                            {
                                "audioFileType":"audiobook",
                                "audioFileMetadata":{
                                        "Uploaded_time":"0",
                                        "Duration_time":108,
                                        "Title":"Ambulance hit",
                                        "Author":"linkin park",
                                        "Narrator":"linkin park - surya v"
                                }
                            }





2. Update

        url = /api/update/<audioFileType>/<audioFileID> 
        method = PUT
        content-type=application/json


        song :
                url : /api/update/song/1
                request body : 

                                {
                                "audioFileType":"song",
                                "audioFileMetadata":{
                                    "Uploaded_time":"100",
                                    "Duration_time":"100",
                                    "Name":"hello hello"
                                    }
                                }


        audio book :
                url : /api/update/audiobook/1
                request body:
                                {
                                    "audioFileType":"audiobook",
                                    "audioFileMetadata":{
                                            "Uploaded_time":"0",
                                            "Duration_time":108,
                                            "Title":"Ambulance hit",
                                            "Author":"linkin park",
                                            "Narrator":"linkin park - surya v"
                                    }
                                }


        podcast : 
                url : /api/update/podcast/1
                request body :

                                {
                                    "audioFileType":"podcast",
                                    "audioFileMetadata":{
                                            "Uploaded_time":"0",
                                            "Duration_time":102,
                                            "Name":"in the end.mp4",
                                            "Host":"linkin park - arizona park",
                                            "Participants":["linkin park","us","american band"]
                                    }
                                }     


3. Delete

url = /api/delete/<audioFileType>/<audioFileID>
method = DELETE
content-type = application/json

song
url: /api/delete/song/1 - deletes the record present at id 1
podcast
url: /api/delete/podcast/1 - deletes the record present at id 1
audiobook
url : /api/delete/audiobook/1 - deletes the  record present at id 1


4. Get 
    url: /api/<audioFileType>
    description: get all the data present in <audioFileType> database 2.- url: /api/<audioFileType>/<audioFileID>
    description: get all data present in <audioFileType> database having id audioFileID`


    urls
    song,

    url1 = `/api/get/song` - get all song in database
    url2 = `/api/get/song/1` - get song having id 1       
    podcast

    url1 = `/api/get/podcast` - get all data in podcast in database
    url2 = `/api/get/podcast/1` - get song having id 1
    audiobook

    url1 = `/api/get/audiobook` - get all data in audiobook in database
    url2 = `/api/get/audiobook/1` - get data having id 1

Response for the Request:

- Action is successful: 200 OK
- The request is invalid: 400 bad request
- Any error: 500 internal server error