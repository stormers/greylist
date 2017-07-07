import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'secret'
# SQLALCHEMY_DATABASE_URI =  'sqlite:///' + os.path.join(basedir, 'api.sqlite')
# SQLALCHEMY_DATABASE_URI = "mysql://root@localhost/greylist"
# SQLALCHEMY_TRACK_MODIFICATIONS = False
MONGO_URI = 'mongodb://localhost:27017/greylist'
