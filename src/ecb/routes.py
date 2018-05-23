# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.ecb import Ecb
from .api.ecb_history import EcbHistory


routes = [
    dict(resource=Ecb, urls=['/ecb'], endpoint='ecb'),
    dict(resource=EcbHistory, urls=['/ecb/history'], endpoint='ecb_history'),
]