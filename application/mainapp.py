
from flask import Flask
from flask import request
from application import view


app = Flask(__name__)


def create_app(config_object="application.settings"):


    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)
    register_blueprints(app)

    return app


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(view.blueprint)
    return None


    
application/extension.py
#	application/mainapp.py
#	application/settings.py
#	application/view.py
#