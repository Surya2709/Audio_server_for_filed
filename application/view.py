from flask import Blueprint, request
from application.extension import CRUD



blueprint = Blueprint("view", __name__, url_prefix="/")



@blueprint.route("/create", methods=["POST"])
def create_api():
    if request.method == "POST":
        data = request.json
        obj = CRUD(data=data)
        response = obj.create()
        return response
    return "The request is invalid: 400 bad request", 400


@blueprint.route("/update/<audioFileType>/<audioFileID>", methods=["PUT"])
def update_api(audioFileType,audioFileID):
    if request.method == "PUT":
        data = request.json
        obj = CRUD(data=data,audioFileID=audioFileID,audioFileType=audioFileType)
        response = obj.update()
        return response
    return "The request is invalid: 400 bad request", 400

@blueprint.route("/delete/<audioFileType>/<audioFileID>", methods=["DELETE"])
def delete_api(audioFileType, audioFileID):
    if request.method == "DELETE":

        obj = CRUD(audioFileType=audioFileType,audioFileID=audioFileID)
        response = obj.delete()
        return response
    return "The request is invalid: 400 bad request", 400

@blueprint.route(
    "/get/<audioFileType>", methods=["GET"], defaults={"audioFileID": None}
)
@blueprint.route("/get/<audioFileType>/<audioFileID>", methods=["GET"])
def get_api(audioFileType, audioFileID):
    if request.method == "GET":
        obj = CRUD(audioFileID=audioFileID,audioFileType=audioFileType)
        response = obj.get()
        return response
    return "The request is invalid: 400 bad request", 400

    