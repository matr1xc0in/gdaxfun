import unittest
import imp
import os
import time
import datetime
import simplejson as json


class TestGdaxDBSQLite(unittest.TestCase):

    test_records = [
        '{"trade_id": 30499319, "size": "0.00010000", "side": "sell", "price": "15586.37000000", "time": "2017-12-26T06:36:53.21Z"}',
        '{"trade_id": 30499255, "size": "0.10000000", "side": "buy", "price": "15561.93000000", "time": "2017-12-26T06:35:59.661Z"}'
    ]
    # This follows the order from above records. This represent the epoch time
    # after the 'time' field is converted.
    test_expected_results = [1514270213, 1514270159]

    db_config = {'sqlite': {'file_path': os.path.join(os.getcwd(), 'sqlite_test.db')},
                 'mysql': {},  # put mysql configurations here
                 'postgres': {}  # put postgrresql configuration here
                 }

    def setUp(self):
        self.curr_dir = os.getcwd()
        self.gdaxdb_lib = imp.load_source(
            'gdaxdb', '../gdaxfun/gdaxfun/gdaxdb.py')
        # Initialize authentication parameters and objects
        self.gdaxdb = self.gdaxdb_lib.GdaxDB(
            self.gdaxdb_lib.GdaxDBLabel.SQLITE, **self.db_config)
        self.sqlite_config = self.db_config['sqlite']
        self.gdaxdb.initdb()

    def tearDown(self):
        if os.path.isfile(self.sqlite_config['file_path']):
            os.remove(self.sqlite_config['file_path'])

    def test_initdb(self):
        self.assertTrue(os.path.isfile(
            self.sqlite_config['file_path']), 'Database file ' + self.sqlite_config['file_path'] + ' isn\'t created')

    def test_insert2records(self):
        for r in self.test_records:
            d = json.loads(r)
            d['productid'] = 'BTC-USD'
            # Convert string time format to integer epoch format
            t = time.strptime(d['time'], '%Y-%m-%dT%H:%M:%S.%fZ')
            d['time'] = int((datetime.datetime(t[0], t[1], t[2], t[3], t[4], t[5]) -
                             datetime.datetime(1970, 1, 1, 0, 0, 0)).total_seconds())
            self.assertIn(d['time'], self.test_expected_results,
                          'Epoch time conversion is incorrect, check the APIs you are using')
            self.gdaxdb.insert_record(d)
            tid_dict = self.gdaxdb.query_record(d['trade_id'])
            self.assertEqual(d['trade_id'], tid_dict['trade_id'])
            self.assertEqual(d['productid'], tid_dict['productid'])
            self.assertEqual(d['side'], tid_dict['side'])
            self.assertEqual(d['time'], tid_dict['time'])
            self.assertEqual(d['price'], str(tid_dict['price']))
            self.assertEqual(d['size'], str(tid_dict['size']))
            self.gdaxdb.delete_record(d['trade_id'])

    def test_insertfromfile(self):
        testf = open(os.path.join(self.curr_dir, 'btcusd_trades.txt'), 'r')
        rec = testf.readline()
        rec_cnt = 0
        while rec != "":
            # convert input json formatter string to Dictionary
            d = json.loads(rec)
            d['productid'] = 'BTC-USD'
            # Convert string time format to integer epoch format
            t = time.strptime(d['time'], '%Y-%m-%dT%H:%M:%S.%fZ')
            d['time'] = int((datetime.datetime(t[0], t[1], t[2], t[3], t[4], t[5]) -
                             datetime.datetime(1970, 1, 1, 0, 0, 0)).total_seconds())
            print json.dumps(d)
            self.gdaxdb.insert_record(d)
            tid_dict = self.gdaxdb.query_record(d['trade_id'])
            self.assertEqual(d['trade_id'], tid_dict['trade_id'])
            self.assertEqual(d['productid'], tid_dict['productid'])
            self.assertEqual(d['side'], tid_dict['side'])
            self.assertEqual(d['time'], tid_dict['time'])
            self.assertEqual(d['price'], str(tid_dict['price']))
            self.assertEqual(d['size'], str(tid_dict['size']))
            rec = testf.readline()
            rec_cnt += 1
        testf.close()
        fetched_cnt = self.gdaxdb.count_records()
        self.assertEqual(rec_cnt, fetched_cnt, 'Inserted record counts ' + str(rec_cnt) +
                         ' from test file is not the same from the test database ' + str(fetched_cnt))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGdaxDBSQLite)
    unittest.TextTestRunner(verbosity=2).run(suite)
