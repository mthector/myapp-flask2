import os

secret_key = '1234'
PWD = os.path.abspath(os.curdir)

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password1@localhost:3306/mibd'
SQLALCHEMY_TRACK_MODIFICATIONS = False
