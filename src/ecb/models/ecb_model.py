# -*- coding: utf-8 -*-
import json
from  ecb import db

'''
ORM model for Currency
'''
class Currency(db.Model):

    def __init__(self, local_currency, local_feed, local_hash):
        self.currency = local_currency
        self.feed = local_feed
        self.hash = local_hash

    def get_map(self):
        '''
        Bundle data for API output
        :return: data tree
        '''
        ret = dict()
        ret['currency'] = self.currency
        ret['feed'] = json.loads(self.feed)
        ret['hash'] = self.hash     # TODO: use it to reduce insertions to DB
        return ret

    def history(self):
        '''
        Gets history values for currency rate - data shaping
        :return: date tree
        '''
        ret = dict()
        ret['currency'] = self.currency
        feed = json.loads(self.feed)
        ret['history'] = list()
        for entry in feed['entries']:
            history_date = entry['updated']
            history_rate = float(entry['cb_exchangerate'][:-4])
            ret['history'].append({'date' : history_date, 'rate' : history_rate})

        return ret

    # fields definition
    currency = db.Column(db.String(3), primary_key=True)
    feed = db.Column(db.String(20*1024))
    hash = db.Column(db.String(64))



