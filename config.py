import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
  'sqlite:///' + os.path.join(basedir, 'bshop-app.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  #MONGO_URI = "mongodb://dbadmin:conmeo123@ds215709.mlab.com:15709/mshop"
  MONGOALCHEMY_DATABASE = "mshop"
  MONGOALCHEMY_SERVER = "ds215709.mlab.com"
  MONGOALCHEMY_PORT = 15709
  MONGOALCHEMY_USER = "dbadmin"
  MONGOALCHEMY_PASSWORD = "conmeo123"
