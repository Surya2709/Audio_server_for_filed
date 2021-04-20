# Audio_server_for_filed
Web API that simulates the behavior of an audio file  server while using a MongoDB / SQL database.




create api 


            song :

            {
            "audioFileType":"song",
            "audioFileMetadata":{
                "Uploaded_time":"100",
                "Duration_time":"100",
                "Name":"hello hello"
                }
            }


            podcast : 

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





update api : /update/<audioFileType>/<audioFileID>




            song :

            {
            "audioFileType":"song",
            "audioFileMetadata":{
                "Uploaded_time":"100",
                "Duration_time":"100",
                "Name":"hello hello"
                }
            }


            audio book :

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


