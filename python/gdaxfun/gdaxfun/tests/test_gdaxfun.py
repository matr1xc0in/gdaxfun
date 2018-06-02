import unittest
import os
import time
import datetime
import simplejson as json
import gdaxfun
import logging
# import sys

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)

class TestGdaxExAuthAndUtils(unittest.TestCase):
    def setUp(self):
        # Initialize authentication parameters and objects
        self.auth = gdaxfun.gdaxauth.GdaxExAuth(os.getenv('GDAX_API_KEY', 'missing_value'),
                                                os.getenv(
                                                    'GDAX_API_SECRET', 'missing_value'),
                                                os.getenv(
                                                    'GDAX_PASSPHRASE', 'missing_value')
                                                )
        # Initialize https client with authentication parameters in headers, ready to
        # fire off
        self.utils = gdaxfun.gdaxutils.GdaxUtils(self.auth)
        self.product_list = []

    def test_gdaxapiurl(self):
        self.assertEqual(self.utils.getAPIUrl(), "https://api.gdax.com/")

    def test_gdaxauthentication(self):
        self.assertEqual(self.utils.getAccount().status_code, 200)

    #=========================================================================
    # We should only see the following IDs. Update this if Gdax has modified them or
    # added new products.
    #
    # "id": "BCH-USD",
    # "id": "LTC-EUR",
    # "id": "LTC-USD",
    # "id": "LTC-BTC",
    # "id": "ETH-EUR",
    # "id": "ETH-USD",
    # "id": "ETH-BTC",
    # "id": "BTC-GBP",
    # "id": "BTC-EUR",
    # "id": "BTC-USD",
    #=========================================================================
    def test_gdaxgetproducts(self):
        predefined_gdaxprod = gdaxfun.gdaxproducts.GdaxProducts()
        fetched_resp = self.utils.getProducts()
        self.assertTrue(
            fetched_resp.ok, "Failed fetching Gdax Products, seeing return code " + str(fetched_resp.status_code))
        for item in fetched_resp.json():
            d = json.loads(json.dumps(item))
            LOGGER.info('Received coin list {}'.format(json.dumps(item)))
            self.assertEqual(predefined_gdaxprod.lookUpString(
                predefined_gdaxprod.lookUpInteger(d['id'])), d['id'], "Failed to map " + d['id'] + " in GdaxProducts class, please fix it")
            self.product_list.append(d['id'])

    def test_gdaxgetticker(self):
        for c in self.product_list:
            LOGGER.info('Fetching ticker for coin {}'.format(c))
            self.assertEqual(self.utils.getCoinTicker(
                c).status_code, 200, "Failed to lookup coin " + c)

    def test_gdaxgetorderbooklv1(self):
        for c in self.product_list:
            LOGGER.info('Fetching orderbook for coin {}'.format(c))
            self.assertEqual(self.utils.getOrderBooksLv1(
                c).status_code, 200, "Failed to lookup coin order book " + c)

    def test_gdaxgetorderbooklv2(self):
        for c in self.product_list:
            LOGGER.info('Fetching orderbook via WebSocket for coin {}'.format(c))
            self.assertEqual(self.utils.getOrderBooksLv2(
                c).status_code, 200, "Failed to lookup coin order book " + c)


if __name__ == '__main__':
    #     logging.basicConfig(stream=sys.stderr)
    #     logging.getLogger(
    #         "TestGdaxExAuth.test_gdaxgetticker").setLevel(logging.DEBUG)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGdaxExAuthAndUtils)
    unittest.TextTestRunner(verbosity=2).run(suite)
