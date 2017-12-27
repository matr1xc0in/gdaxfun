import simplejson as json
import requests

#=========================================================================
# DISCLAIMER: This class is provided as-is and does not guarantee any reliable
# functionality nor liability of any monetary damage. Use it as your own risk.
#
# This class wrap up the function we need for each APIs.
# We use coin_id interchangeable with product_id in this class.
# To update this class, please refer to https://docs.gdax.com
#=========================================================================


class GdaxUtils():

    def __init__(self, auth):
        self.user_auth = auth
        self.api_url = "https://api.gdax.com/"

    def setAPIUrl(self, api_url):
        self.api_url = api_url

    def getAPIUrl(self):
        return self.api_url

    def getAccount(self):
        r = requests.get(self.api_url + 'accounts', auth=self.user_auth)
        return r

    # https://docs.gdax.com/?python#products
    def getProducts(self):
        r = requests.get(self.api_url + 'products', auth=self.user_auth)
        return r

    # https://docs.gdax.com/?python#get-product-ticker
    # coid_id = product_id
    def getCoinTicker(self, coin_id):
        r = requests.get(self.api_url + 'products/' + coin_id + '/ticker',
                         auth=self.user_auth)
        return r

    # https://docs.gdax.com/?python#get-trades
    # unique key is based on trade_id
    #
    # The trade 'side' indicates the maker order side. The maker order is the
    # order that was open on the order book. 'buy' side indicates a down-tick
    # because the maker was a buy order and their order was removed.
    # Conversely, 'sell' side indicates an up-tick.
    # e.g.
    # [{
    #     "time": "2014-11-07T22:19:28.578544Z",
    #     "trade_id": 74,
    #     "price": "10.00000000",
    #     "size": "0.01000000",
    #     "side": "buy"
    # }, {
    #     "time": "2014-11-07T01:08:43.642366Z",
    #     "trade_id": 73,
    #     "price": "100.00000000",
    #     "size": "0.01000000",
    #     "side": "sell"
    # }]
    def getTrades(self, coin_id):
        r = requests.get(self.api_url + 'products/' + coin_id + '/trades',
                         auth=self.user_auth)
        resp_headers = r.headers
        latest_trade_id = ''
        if 'cb-before' in resp_headers:
            latest_trade_id = resp_headers['cb-before']
        return r

    #=========================================================================
    # Reference: https://docs.gdax.com/?python#get-product-order-book
    #
    # Get a list of open orders for a product. The amount of detail shown can be
    # customized with the level parameter.
    # This request is NOT paginated. The entire book is returned in one response.
    #
    # HTTP REQUEST
    # GET /products/<product-id>/book
    # GET /products/<product-id>/book?level=2
    #
    # DETAILS By default, only the inside (i.e. best) bid and ask are returned.
    # This is equivalent to a book depth of 1 level. If you would like to see a
    # larger order book, specify the level query parameter. If a level is not
    # aggregated, then all of the orders at each price will be returned.
    # Aggregated levels return only one size for each active price (as if there
    # was only a single order for that size at the level).
    #
    # LEVELS
    #========================================
    # Level    Description
    # 1    Only the best bid and ask
    # 2    Top 50 bids and asks (aggregated)
    # 3    Full order book (non aggregated) - We DON'T Support this in this class
    #========================================
    #
    # Levels 1 (default) and level 2 are aggregated and return the number of
    # orders at each level. Level 3 is non- aggregated and returns the entire
    # order book.
    #=========================================================================
    def getOrderBooksLv1(self, coin_id):
        r = requests.get(self.api_url + 'products/' + coin_id + '/book',
                         auth=self.user_auth)
        return r

    def getOrderBooksLv2(self, coin_id):
        r = requests.get(self.api_url + 'products/' + coin_id + '/book?level=2',
                         auth=self.user_auth)
        return r