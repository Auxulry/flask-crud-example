import os
# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'test')
    ENV = 'production'
    TESTING = False
    DEBUG = "production"


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'user.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'user.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
