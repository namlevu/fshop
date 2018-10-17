import os
basedir = os.path.abspath(os.path.dirname(__file__))

from configparser import ConfigParser

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'bshop-app.db')
    appconfig = ConfigParser()
    appconfig.read('config.ini')
    if 'PRODUCTION' in appconfig:
        print('Production configuration load success')
        MONGODB_DB = appconfig['PRODUCTION']['mongodb_db']
        MONGODB_HOST = appconfig['PRODUCTION']['mongodb_host']
        MONGODB_PORT = int(appconfig['PRODUCTION']['mongodb_port'])
        MONGODB_USERNAME = appconfig['PRODUCTION']['mongodb_username']
        MONGODB_PASSWORD = appconfig['PRODUCTION']['mongodb_password']
    elif 'DEV' in appconfig:
        print('Development configuration load success')
        MONGODB_DB = appconfig['DEV']['mongodb_db']
        MONGODB_HOST = appconfig['DEV']['mongodb_host']
        MONGODB_PORT = int(appconfig['DEV']['mongodb_port'])
        MONGODB_USERNAME = appconfig['DEV']['mongodb_username']
        MONGODB_PASSWORD = appconfig['DEV']['mongodb_password']
    else:
        print('Load configuration error')
