from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()
migrate = Migrate()

Column = database.Column

relation = database.relationship