
from flask import Flask, render_template, redirect
import os



app = Flask(__name__)


@app.route('/')
def home():
    return "you are up"


if __name__ == "__main__":
    app.run(debug=True)