import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://usuario:password@localhost/imc_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)