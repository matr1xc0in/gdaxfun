import json, requests

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
        return r.json()

    # https://docs.gdax.com/?python#products
    def getProducts(self):
        r = requests.get(self.api_url + 'products', auth=self.user_auth)
        return r.json()

    # https://docs.gdax.com/?python#get-product-ticker
    def getCoinTicker(self, coin_id):
        r = requests.get(self.api_url + 'products/' + coin_id + '/ticker',
                auth=self.user_auth)
        return r.json()

    # https://docs.gdax.com/?python#get-trades
    # unique key is based on trade_id
    def getTrades(self, coin_id):
        r = requests.get(self.api_url + 'products/' + coin_id + '/trades',
                auth=self.user_auth)
        resp_headers = r.headers
        latest_trade_id = ''
        if 'cb-before' in resp_headers:
            latest_trade_id = resp_headers['cb-before']
        return r.json()
