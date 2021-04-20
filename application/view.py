from flask import Blueprint, request
from extension import 


blueprint = Blueprint("view", __name__, url_prefix="/")





@blueprint.route("/create", methods=["POST"])
def create_api():
    if request.method == "POST":
        data = request.json
        response = creator.create(data)
        return response
    return "The request is invalid: 400 bad request", 400


@blueprint.route("/update/<audioFileType>/<audioFileID>", methods=["PUT"])
def update_api(audioFileType,audioFileID):
    if request.method == "PUT":
        data = request.json
        response = updater.update(data,audioFileType,audioFileID)
        return response
    return "The request is invalid: 400 bad request", 400



@blueprint.route("/delete/<audioFileType>/<audioFileID>", methods=["DELETE"])
def delete_api(audioFileType, audioFileID):
    if request.method == "DELETE":
        response = deleter.delete(audioFileType,audioFileID)
        return response

    return "The request is invalid: 400 bad request", 400


@blueprint.route(
    "/get/<audioFileType>", methods=["GET"], defaults={"audioFileID": None}
)
@blueprint.route("/get/<audioFileType>/<audioFileID>", methods=["GET"])
def get_api(audioFileType, audioFileID):
    if request.method == "GET":
        response = getter.get(audioFileType,audioFileID)
        return response
    return "The request is invalid: 400 bad request", 400

        

if __name__ == "__main__":
    app.run(debug=True)