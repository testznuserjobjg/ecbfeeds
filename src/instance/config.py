# -*- coding: utf-8 -*-
import os
import tempfile

'''
Configuration sets per env.
'''
class Config(object):
    """Parent configuration class."""
    DEBUG = False
    # CSRF_ENABLED = True
    #SECRET = os.getenv('SECRET')
    basedir = tempfile.gettempdir()
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(basedir, 'data.sqlite')

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True

class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    basedir = tempfile.gettempdir()
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(basedir, 'data_test.sqlite')
    DEBUG = True

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}