from sqlalchemy import Column, String, Integer, create_engine, join
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy
import json
import os
from app import app, db

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
