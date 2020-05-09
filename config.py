import os


class Config(object):
    SECRET_KEY = "XXXXXXXTYUIO"


class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False


class DevConfig(Config):
    DEBUG = True
    LOCATION = "TEST"