import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgres://eqilwyxeajquxm: 4071fa93ffa7ee28ffd6c490b386dcd70eeab0fa1cce23afa64c93fd4ade1940@ec2-54-158-222-248.compute-1.amazonaws.com: 5432/d670enjhnd0lir'
