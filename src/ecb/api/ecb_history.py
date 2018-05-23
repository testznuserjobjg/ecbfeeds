# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource
from .. import schemas

'''
API for showing history of currency rate
'''
class EcbHistory(Resource):

    def get(self):
        '''
        GET history per country currency code (histogram)
        :return:
        '''

        print(g.args)
        # TODO: here function to get aggregation of history from ElastiSearch

        return None, 200, None