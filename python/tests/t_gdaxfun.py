import imp
import os
import json

# Reformat JSON Content to a more readable fashion
prettyp = True


def prettyprint(dict):
    if prettyp == True:
        print json.dumps(dict.json(), indent=2, sort_keys=True)
    else:
        print dict.json()


api_url = 'https://api.gdax.com/'

ga = imp.load_source('gdaxauth', '../gdaxfun/gdaxfun/gdaxauth.py')
gu = imp.load_source('gdaxutils', '../gdaxfun/gdaxfun/gdaxutils.py')

# Initialize authentication parameters and objects
mygauth = ga.GdaxExAuth(os.getenv('GDAX_API_KEY', 'missing_value'),
                        os.getenv('GDAX_API_SECRET', 'missing_value'),
                        os.getenv('GDAX_PASSPHRASE', 'missing_value')
                        )

# Initialize https client with authentication parameters in headers, ready to
# fire off
myutils = gu.GdaxUtils(mygauth)

prettyprint(myutils.getAccount())
prettyprint(myutils.getProducts())
prettyprint(myutils.getCoinTicker('BTC-USD'))

# The following returns a Dictionary for fast lookup and traverse. Do NOT parse JSON since
# it is not necessary.
trade_http_resp = myutils.getTrades('BTC-USD')
for tentry in trade_http_resp.json():
    dict = json.loads(json.dumps(tentry))
    print(dict)


prettyprint(myutils.getOrderBooksLv1('BTC-USD'))
prettyprint(myutils.getOrderBooksLv2('BTC-USD'))
