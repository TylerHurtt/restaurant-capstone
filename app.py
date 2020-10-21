#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json
import dateutil.parser
import babel
import sys
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify, abort
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from flask_migrate import Migrate
from datetime import date, datetime
from sqlalchemy import Column, Integer, String, join
from sqlalchemy.orm import sessionmaker


#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
# app.config.from_object('config')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = False

# app = Flask(__name__)

# app.config.from_object('config')
# app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://Tyler:Pesthlos!2772@localhost:5432/fyyur'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.debug = True

db = SQLAlchemy(app)

# TODO: connect to a local postgresql database

migrate = Migrate(app, db)


#----------------------------------------------------------------------------#
# Models
#----------------------------------------------------------------------------#

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


@app.route('/')
def index():
    print('hello world')
    return 'hello world'


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
