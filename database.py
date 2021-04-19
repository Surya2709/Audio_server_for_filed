from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()
migrate = Migrate()

Column = database.Column

relation = database.relationship



class CRUDMIXIN(object):
    def create():
        pass
    def update():
        pass
    def save():
        pass
    def delete():
        pass
    
def Model(CRUDMIXIN , database.Model):
    __abstract__ = True

class SurrogatePK(object):
    @classmethod
    def get_by_id():
        pass
    