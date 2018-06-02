gdaxfun
=======

The module wraps the Gdax RESTFul APIs into functions so you can apply them directly.

* `gdaxauth.py` - Initiate the authentication protocol and embed the necessary access key
                 and secret key, etc. into the HTTP/HTTPS Request headers.
* `gdaxutils.py` - The wrapper function that invokes RESTFul APIs and pass the results to
                 the caller.
* `gdaxdb.py` - A set of wrapper functions to interact with a database. Currently, we only
                 use SQLIte, but it can be exapanded to other databases with minimal changes.
* `gdaxtables.py` - Defines the tables for the database.
* `gdaxproducts.py` - Define a list of products provided by Gdax. You need to udpate this if
                 Gdax offers new products.

A example pn how to use the module,

```
    #!/usr/bin/env python

    import gdaxfun

    mygauth = gdaxfun.gdaxauth.GdaxExAuth(os.getenv('GDAX_API_KEY', 'missing_value'),
                        os.getenv('GDAX_API_SECRET', 'missing_value'),
                        os.getenv('GDAX_PASSPHRASE', 'missing_value')
                        )
    # Initialize https client with authentication parameters in headers from above
    # and ready to fire off
    myutils = gdaxfun.gdaxutils.GdaxUtils(mygauth)
```


Test Cases
==========

There are 2 major test cases that covers all functions.

* `gdaxfun/tests/test_gdaxfun.py`
* `gdaxfun/tests/test_gdaxdb.py`

In the `tests` directory, the file with prefix `test_gdaxYYYY` where `YYYY` presents the module name
(e.g. `gdaxauth`, `gdaxutils`, `gdaxdb`, etc) are the test files that include examples how to use the APIs respectively.

```
.
├── btcusd_trades.txt
├── __init__.py
├── test_gdaxfun.py
└── test_gdaxdb.py
```

To run the unit test, you will need to use `nosetests` or the `setup.py` to run them.
The filename `test_gdaxYYYY` where `gdaxYYYY` refers to the module we are testing. Some modules
are combined into one test file such as `test_gdaxdb.py`.
e.g.

```
python setup.py test
```

or in this same directory

```
nosetests -vv --logging-level=DEBUG
```

If you run into the following errors, that means you didn't initialize the envrionment variables

* `GDAX_PASSPHRASE`
* `GDAX_API_KEY`
* `GDAX_API_SECRET`

```
....F....
======================================================================
FAIL: test_gdaxauthentication (gdaxfun.tests.test_gdaxfun.TestGdaxExAuthAndUtils)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/banana/Documents/github/mikeandyrocks/python/gdaxfun/gdaxfun/tests/test_gdaxfun.py", line 29, in test_gdaxauthentication
    self.assertEqual(self.utils.getAccount().status_code, 200)
AssertionError: 400 != 200
-------------------- >> begin captured logging << --------------------
urllib3.connectionpool: DEBUG: Starting new HTTPS connection (1): api.gdax.com
urllib3.connectionpool: DEBUG: https://api.gdax.com:443 "GET /accounts HTTP/1.1" 400 29
--------------------- >> end captured logging << ---------------------
```
