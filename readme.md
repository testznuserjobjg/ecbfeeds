It is RESTful API for gathering RSS feed from ECB with currency rate.
API has been defined by Swagger. See: ecb_api_swager.yaml

## How to install project

* Clone repo to Ubuntu 17 (only with it tested)
* Run sudo setup.sh - it will take compoments, install virtualenv
* Call src/init.py to initialize DB schema (be sure you do this from venv :) -> source /venv/bin/activate
* Call src/run.py from venv


### How to use it

* First call PUT in API to get RSS feeds to index
* Second use GET to retrieve RSS in JSON format

```
127.0.0.1 - - [23/May/2018 11:57:32] "PUT /ecb HTTP/1.1" 200 -
127.0.0.1 - - [23/May/2018 11:57:39] "GET /ecb?currency=usd HTTP/1.1" 200 -
```

## Unittest
You can run them from src/ecb/api/unittests/api_tests.py

## TODOs
* Getting historical records from ElastiSearch (v-fast aggregation)
* More unittest (for e.g. for model)
* Clean up setup artifacts (ElasticSeach)
* Define schemas and response type in Swagger to get validation response work
