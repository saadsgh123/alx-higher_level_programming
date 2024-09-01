import os


class Config:
    SECRET_KEY = "os.environ.get('SECRET_KEY') or a_secret_key"
    SQLALCHEMY_DATABASE_URI = ('mysql+mysqldb://{}:{}@{}/{}'
                               .format("root", "anasaad", "localhost", "authan"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
