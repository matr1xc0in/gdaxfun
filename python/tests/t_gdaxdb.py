import unittest
import imp
import os
import json
import time
import datetime


class TestGdaxDBSQLite(unittest.TestCase):

    db_config = {'sqlite': {'file_path': os.getcwd() + "/sqlite_test.db"},
                 'mysql': {},
                 'postgres': {}
                 }

    def setUp(self):
        self.gdaxdb_lib = imp.load_source(
            'gdaxdb', '../gdaxfun/gdaxfun/gdaxdb.py')
        # Initialize authentication parameters and objects
        self.gdaxdb = self.gdaxdb_lib.GdaxDB(
            self.gdaxdb_lib.GdaxDBLabel.SQLITE, **self.db_config)
        self.sqlite_config = self.db_config['sqlite']
        self.gdaxdb.initdb()

    def test_initdb(self):
        self.assertTrue(os.path.isfile(
            self.sqlite_config['file_path']), "Database file " + self.sqlite_config['file_path'] + " isn't created")

    def test_insertrecords(self):
        rec0 = '{"trade_id": 30499319, "size": "0.00010000", "side": "sell", "price": "15586.37000000", "time": "2017-12-26T06:36:53.21Z"}'
        rec1 = '{"trade_id": 30499255, "size": "0.10000000", "side": "buy", "price": "15561.93000000", "time": "2017-12-26T06:35:59.661Z"}'
        dict0 = json.loads(rec0)
        dict1 = json.loads(rec1)
        dict0['productid'] = 'BTC-USD'
        dict1['productid'] = 'BTC-USD'
        t0 = time.strptime(dict0['time'], "%Y-%m-%dT%H:%M:%S.%fZ")
        # 1514270213
        dict0['time'] = int((datetime.datetime(t0[0], t0[1], t0[2], t0[3], t0[4], t0[5]) -
                             datetime.datetime(1970, 1, 1, 0, 0, 0)).total_seconds())
        # 1514270159
        t1 = time.strptime(dict1['time'], "%Y-%m-%dT%H:%M:%S.%fZ")
        dict1['time'] = int((datetime.datetime(t1[0], t1[1], t1[2], t1[3], t1[4], t1[5]) -
                             datetime.datetime(1970, 1, 1, 0, 0, 0)).total_seconds())
        self.gdaxdb.insert_record(dict0)
        self.gdaxdb.insert_record(dict1)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGdaxDBSQLite)
    unittest.TextTestRunner(verbosity=2).run(suite)
