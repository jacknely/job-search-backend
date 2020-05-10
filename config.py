class Config(object):
    SECRET_KEY = "XXXXXXXTYUIO"


class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False


class DevConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    DB_ADDR = 'https://oe9tdngv19.execute-api.eu-west-1.amazonaws.com/dev'
