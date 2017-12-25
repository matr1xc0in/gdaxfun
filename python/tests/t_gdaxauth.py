import unittest
import imp
import os


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

    def test_gdaxapiurl(self):
        self.assertEqual(self.utils.getAPIUrl(), "https://api.gdax.com/")

    def test_gdaxauthentication(self):
        self.assertEqual(self.utils.getAccount().status_code, 200)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGdaxExAuth)
    unittest.TextTestRunner(verbosity=2).run(suite)
