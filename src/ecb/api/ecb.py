# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
from flask import request, g
from . import Resource
from .. import schemas
import  feedparser
import json
import hashlib
from  ecb import db
from ..models.ecb_model import Currency
from elasticsearch import Elasticsearch

# Available currencies
currencies = ['usd', 'jpy', 'bgn', 'czk', 'dkk', 'eek', 'gbp', 'huf', 'pln', 'ron', 'sek', 'chf', 'isk', 'nok', 'hrk', 'rub', 'try',
              'aud', 'brl', 'cad', 'cny', 'hkd', 'idr', 'inr', 'krw', 'mxn', 'myr', 'nzd', 'php', 'sgd', 'thb', 'zar' ]


index_name = 'test-index'

'''
API for indexing currency rates feeds from ECB
'''
class Ecb(Resource):

    def get(self):
        '''
        Gets currency feed 1:1 in json by currency ISO code
        :return: Status HTTP code
        '''
        row = Currency.query.filter_by(currency=g.args['currency']).first()
        if row is None:
            return None, 204, None

        return row.get_map(), 200, None

    def put(self):
        '''
        Invokes refreshing feeds from ECB. Store results to Elasticsearch for future usage
        :return: HTTP Stauts code
        '''

        # index in Elasticsearch
        es = Elasticsearch(
            ['localhost:9200'],
            # http_auth=('user', 'secret'),
            # port=443
            # use_ssl=True
        )

        if not es.indices.exists(index_name):

            # create index
            es.indices.create(index_name, ignore=400)
        else:
            es.indices.delete(index=index_name, ignore=[400, 404])
            es.indices.create(index_name, ignore=400)

        for curr in currencies:
            url = 'https://www.ecb.europa.eu/rss/fxref-%s.html' % (curr)

            # get rss feed
            feed = feedparser.parse(url)
            json_rss = json.dumps(feed)

            # calculate hash to check if already exists
            m = hashlib.md5(json_rss.encode('utf-8'))
            hash_code = m.hexdigest()

            # delete old
            row_to_delete = Currency.query.filter_by(currency=curr).first()
            if row_to_delete is not None:
                db.session.delete(row_to_delete)
                db.session.commit()

            # add new
            new_currency = Currency(curr, json_rss, hash_code)
            db.session.add(new_currency)
            db.session.commit()


            body_to_index = json.dumps(new_currency.history())
            es.index(index=index_name, doc_type="text", body=body_to_index.encode('utf-8'))

        return None, 200, None