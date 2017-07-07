import os


SECRET_KEY = os.environ.get('SECRET_KEY', 's3cr3t')
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/greylist')
