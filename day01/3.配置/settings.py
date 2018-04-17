#!/usr/bin/python3.5
# Author: xiaojie

class BaseConfig(object):
    DEBUG = False
    SESSION_REFRESH_EACH_REQUEST = True


class TestConfig(BaseConfig):
    DEBUG = True
    secret_key = "helloworld"

class DevConfig(BaseConfig):
    DEBUG = True

class ProdConfig(BaseConfig):
    pass