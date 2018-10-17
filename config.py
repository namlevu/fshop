import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'bshop-app.db')

    #CONNECTION_STRING = "mongodb://username:password@mshop-shard-00-00-wuufk.gcp.mongodb.net:27017,mshop-shard-00-01-wuufk.gcp.mongodb.net:27017,mshop-shard-00-02-wuufk.gcp.mongodb.net:27017/test?ssl=true&replicaSet=mshop-shard-0&authSource=admin&retryWrites=true"
    MONGODB_DB = "test"
    MONGODB_HOST = "mshop-shard-00-00-wuufk.gcp.mongodb.net,mshop-shard-00-01-wuufk.gcp.mongodb.net,mshop-shard-00-02-wuufk.gcp.mongodb.net"
    MONGODB_PORT = 27017
    MONGODB_USERNAME = "username"
    MONGODB_PASSWORD = "password"
