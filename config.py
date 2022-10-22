import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SSL_REDIRECT = False



class ProdConfig(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SSL_REDIRECT = True
    

        


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False