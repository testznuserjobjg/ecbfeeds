import unittest
import os
import json
from flask_sqlalchemy import SQLAlchemy
import tempfile
from ecb import db, app

config_name = 'TestingConfig'

'''
Testing API - just presentatnion the Unittest of ervice
'''
class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        """Define test variables and initialize app."""

        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        basedir = tempfile.gettempdir()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'data_test.sqlite')       # use different DB
        db.session.close()
        db.drop_all()
        db.create_all()
        self.app = app.test_client()

    def test_hello_world(self):

        response =  self.app.get('/ecb?currency=usd')
        self.assertEqual(204, response.status_code)

        response = self.app.put('/ecb')
        self.assertEqual(200, response.status_code)

        response = self.app.get('/ecb?currency=usd')
        self.assertEqual(200, response.status_code)

if __name__ == "__main__":
    unittest.main()