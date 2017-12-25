import unittest
# import logging
# import sys
import imp
import os
import json


class TestGdaxExAuth(unittest.TestCase):
    def setUp(self):
        self.gdaxauth_lib = imp.load_source(
            'gdaxauth', '../gdaxfun/gdaxfun/gdaxauth.py')
        # Initialize authentication parameters and objects
        self.auth = self.gdaxauth_lib.GdaxExAuth(os.getenv('GDAX_API_KEY', 'missing_value'),
                                                 os.getenv(
                                                     'GDAX_API_SECRET', 'missing_value'),
                                                 os.getenv(
                                                     'GDAX_PASSPHRASE', 'missing_value')
                                                 )
        self.gdaxutils_lib = imp.load_source(
            'gdaxutils', '../gdaxfun/gdaxfun/gdaxutils.py')
        # Initialize https client with authentication parameters in headers, ready to
        # fire off
        self.utils = self.gdaxutils_lib.GdaxUtils(self.auth)
        self.gdaxproducts_lib = imp.load_source(
            'gdaxproducts', '../gdaxfun/gdaxfun/gdaxproducts.py')

        self.product_list = []

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
        predefined_gdaxprod = self.gdaxproducts_lib.GdaxProducts()
        fetched_resp = self.utils.getProducts()
        self.assertTrue(
            fetched_resp.ok, "Failed fetching Gdax Products, seeing return code " + str(fetched_resp.status_code))
        for item in fetched_resp.json():
            dict = json.loads(json.dumps(item))
            self.assertEqual(predefined_gdaxprod.lookUpString(
                predefined_gdaxprod.lookUpInteger(dict['id'])), dict['id'], "Failed to map " + dict['id'] + " in GdaxProducts class, please fix it")
            self.product_list.append(dict['id'])

    def test_gdaxgetticker(self):
        # log = logging.getLogger("TestGdaxExAuth.test_gdaxgetticker")
        for c in self.product_list:
            self.assertEqual(self.utils.getCoinTicker(
                c).status_code, 200, "Failed to lookup coin " + c)

    def test_gdaxgetorderbooklv1(self):
        for c in self.product_list:
            self.assertEqual(self.utils.getOrderBooksLv1(
                c).status_code, 200, "Failed to lookup coin order book " + c)

    def test_gdaxgetorderbooklv2(self):
        for c in self.product_list:
            self.assertEqual(self.utils.getOrderBooksLv2(
                c).status_code, 200, "Failed to lookup coin order book " + c)


if __name__ == '__main__':
    #     logging.basicConfig(stream=sys.stderr)
    #     logging.getLogger(
    #         "TestGdaxExAuth.test_gdaxgetticker").setLevel(logging.DEBUG)
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGdaxExAuth)
    unittest.TextTestRunner(verbosity=2).run(suite)
