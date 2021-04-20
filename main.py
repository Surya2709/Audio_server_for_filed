from flask import Flask
from flask import request
from application import creator,updater


app = Flask(__name__)



@app.route("/create", methods=["POST"])
def create_api():
    if request.method == "POST":
        data = request.json
        response = creator.create(data)
        return response
    return "The request is invalid: 400 bad request", 400


@app.route("/update/<audioFileType>/<audioFileID>", methods=["POST"])
def update_api(audioFileType,audioFileID):
    if request.method == "POST":
        data = request.json
        response = updater.update(data,audioFileType,audioFileID)
        return response
    return "The request is invalid: 400 bad request", 400



if __name__ == "__main__":
    app.run(debug=True)