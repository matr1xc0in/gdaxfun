gdaxfun
=======

Example, assume you have defined a function `get_api_key` in `gdaxfun/gdaxauth.py` python file
and a variable to read API key from a file OR a hardcoded variable for the API key in your code, 
the following code example should print the API key on the screen by invoking the function `show_api_key`
defined in `gdaxfun/gdaxutils.py`.

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

To run the unit test, simply use `python t_gdaxYYYY` in the `tests` directory or run `nosetests` in any directory
e.g.

```
pushd gdaxfun/tests/
python test_gdaxfun.py
python test_gdaxdb.py
popd
```

or in this directory

```
nosetests
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
