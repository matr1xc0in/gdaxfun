import imp
import os
import simplejson as json

# Reformat JSON Content to a more readable fashion
prettyp = True


# This method takes in a requests.Response object and utilize the json() method
# that returns a Dictionary from the Response object that contains all the body
# messages (JSON Format). Printing a Dictionary object directly, you will see a
# prefixed 'u' in front of all key-value pairs. Use json.dumps() method to print
# out pure ASCII/text JSON content from a Dictionary object.
def prettyprint(http_response):
    if prettyp == True:
        print json.dumps(http_response.json(), indent=2, sort_keys=True)
    else:
        print http_response.json()


api_url = 'https://api.gdax.com/'

ga = imp.load_source('gdaxauth', '../gdaxfun/gdaxfun/gdaxauth.py')
gu = imp.load_source('gdaxutils', '../gdaxfun/gdaxfun/gdaxutils.py')

# Initialize authentication parameters and objects
mygauth = ga.GdaxExAuth(os.getenv('GDAX_API_KEY', 'missing_value'),
                        os.getenv('GDAX_API_SECRET', 'missing_value'),
                        os.getenv('GDAX_PASSPHRASE', 'missing_value')
                        )
# Initialize https client with authentication parameters in headers from above
# and ready to fire off
myutils = gu.GdaxUtils(mygauth)

#=========================================================================
# Calling some APIs exercise begin
#=========================================================================
# Fetch our Account info from GDAX and print it out in JSON format
prettyprint(myutils.getAccount())

# Fetch all Products provided by GDAX exchange and print it out in JSON format
prod_http_resp = myutils.getProducts()
for pentry in prod_http_resp.json():
    print(json.dumps(pentry))

# Get ticker for specific product 'BTC-USD' and 'ETH-USD' from GDAX and print
# it out from the Dictionary object derived from the requests.Response object
ticker_http_resp = myutils.getCoinTicker('BTC-USD')
ticker_dict = ticker_http_resp.json()
print('BTC-USD pass 24hrs ticker shows: price closed at ' +
      ticker_dict['price'] + ' with size ' + ticker_dict['size'] +
      ' and volume ' + ticker_dict['volume'] + ' at time ' + ticker_dict['time'])

ticker_http_resp = myutils.getCoinTicker('ETH-USD')
ticker_dict = ticker_http_resp.json()
print('ETH-USD pass 24hrs ticker shows: price closed at %s with size %s and volume %s at time %s' %
      (ticker_dict['price'], ticker_dict['size'],
       ticker_dict['volume'], ticker_dict['time'])
      )


# The following returns a Dictionary for fast lookup and traverse. Do NOT parse JSON since
# it is not necessary.
trade_http_resp = myutils.getTrades('BTC-USD')
for tentry in trade_http_resp.json():
    print('Dumping Dictionary object via json.dumps on trade_id=%d at time %s' %
          (tentry['trade_id'], tentry['time'])
          )
    print(json.dumps(tentry))

# Level 1 Order Book, best bid and ask provided only
prettyprint(myutils.getOrderBooksLv1('BTC-USD'))

# Level 2 Order Book, all bid and ask provided at current time when API invoked.
# A List is provided for each 'ask', 'bid', and a unique 'sequence' ID.
orderbook_lv2_http_resp = myutils.getOrderBooksLv2('BTC-USD')
orderbook_dict = orderbook_lv2_http_resp.json()
print('Sequence ID for this batch is = %d' % orderbook_dict['sequence'])
print('Total asks records = %d' % len(orderbook_dict['asks']))
for ob in orderbook_dict['asks']:
    print(ob)

print('Total bids records = %d' % len(orderbook_dict['bids']))
for ob in orderbook_dict['bids']:
    print(ob)
