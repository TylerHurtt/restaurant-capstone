from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import os

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


'''
Wait staff
'''


class Staff(db.Model):
    __tablename__ = 'Staff'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    position = Column(String)
    # availability = ##something

    def __init__(self, name, position=""):
        self.name = name
        self.position = position

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'position': self.position}


'''
Shifts
'''


class Shift(db.Model):
    __tablename__ = 'Shifts'

    id = Column(Integer, primary_key=True)
    # employeeID = Column(String)
    position = Column(String)
    # time = Column(Datetime)
    # day = Column(string)
    # dateTime = day & time

    def __init__(self, name, position=""):
        self.name = name
        self.position = position

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'position': self.position}
