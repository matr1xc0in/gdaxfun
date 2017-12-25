import imp
import os
import json

# Reformat JSON Content to a more readible fashion
prettyp = True


def prettyprint(json_content):
    if prettyp == True:
        print json.dumps(json_content, indent=2, sort_keys=True)
    else:
        print json_content


api_url = 'https://api.gdax.com/'

ga = imp.load_source('gdaxauth', '../gdaxfun/gdaxfun/gdaxauth.py')
gu = imp.load_source('gdaxutils', '../gdaxfun/gdaxfun/gdaxutils.py')

# Init authentication parameters and objects
mygauth = ga.GdaxExAuth(os.getenv('GDAX_API_KEY', 'missing_value'),
                        os.getenv('GDAX_API_SECRET', 'missing_value'),
                        os.getenv('GDAX_PASSPHRASE', 'missing_value')
                        )

# Init https client with authentication parameters in headers, ready to
# fire off
myutils = gu.GdaxUtils(mygauth)

prettyprint(myutils.getAPIUrl())
prettyprint(myutils.getAccount())
prettyprint(myutils.getProducts())
prettyprint(myutils.getCoinTicker('BTC-USD'))
prettyprint(myutils.getTrades('BTC-USD'))
