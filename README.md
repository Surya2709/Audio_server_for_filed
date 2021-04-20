# Audio_server_for_filed
Web API that simulates the behavior of an audio file  server while using a MongoDB / SQL database.

code info:

    FrameWork = Flask
    Database = MongoDB





1. Setup codebase

<ul>


<li> clone the code in a directory : https://github.com/Surya2709/Audio_server_for_filed.git</li>

<li> go in the directory cd Audio_server_for_filed-main </li>
<li> install all project requirements, pip install -r requirements.txt </li>
<li> set up flask env variable, run commands
        
            export FLASK_APP=main.py
            export FLASK_ENV=developement
</li>


</ul>

2.  Create database : 

    >  Donwload and install mongodb in local system and create a database named "audioserver"


3. To run :

            set FLASK_ENV = development
            set FLASK_APP = app.py 
            flask run



4. Check running status
    
            > check if the server is running goto localhost:5000/ you will get a server running message


<h2> <b>How to Test the API</b></h2>
<h6><i>The Test api structure is given in documentation. </i> </h6>

<b> API's End point </b>


    The API has 4 End Point.

<b>1. Create</b>  


        url = /api/create 
        method = Post
        content-type=application/json

    structure:

        song :
            request body:

                        {
                        "audioFileType":"song",
                        "audioFileMetadata":{
                            "Uploaded_time":"0",
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
                                        "Narrator":"linkin park - surya R <3"
                                }
                            }





 <b>2. Update</b>

        url = /api/update/<audioFileType>/<audioFileID> 
        method = PUT
        content-type=application/json


        song :
                url : /api/update/song/1
                request body : 

                                {
                                "audioFileType":"song",
                                "audioFileMetadata":{
                                    "Uploaded_time":"0",
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


<b>3.  Delete </b>

url = /api/delete/<audioFileType>/<audioFileID>
method = DELETE
content-type = application/json

song
url: /api/delete/song/1 - deletes the record present at id 1
podcast
url: /api/delete/podcast/1 - deletes the record present at id 1
audiobook
url : /api/delete/audiobook/1 - deletes the  record present at id 1


<b> 4.Get </b>
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

<b><h3> Response for the Request: </h3> </b>

        - Action is successful: <b>200 OK </b>
        - The request is invalid: <b> 400 bad request </b>
        - Any error: <b> 500 internal server error </b>