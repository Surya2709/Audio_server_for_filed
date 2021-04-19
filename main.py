
from flask import Flask, render_template, redirect
from flask import Blueprint, request, jsonify




app = Flask(__name__)


blueprint = Blueprint("main", __name__, url_prefix="/")


@blueprint.route("/")
def home():
    return "We are live !"\


@blueprint.route("/create")
def create_api():
    return "create API"

@blueprint.route("/update")
def update_api():
    return "update API"

@blueprint.route("/delete")
def delete_api():
    return "delete API"

@blueprint.route("/get")
def get_api():
    return "get API"




if __name__ == "__main__":
    app.register_blueprint(blueprint)
    app.run(debug=True)