
from flask import Flask, render_template, redirect
from flask import Blueprint, request, jsonify




app = Flask(__name__)


blueprint = Blueprint("main", __name__, url_prefix="/")


@blueprint.route("/")
def home():
    return "We are live !"

if __name__ == "__main__":
    app.register_blueprint(blueprint)
    app.run(debug=True)