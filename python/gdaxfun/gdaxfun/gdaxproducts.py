class GdaxProducts:
    BCH_USD = 1
    BCH_BTC = 2
    BCH_EUR = 3
    BTC_EUR = 4
    BTC_GBP = 5
    BTC_USD = 6
    ETH_BTC = 7
    ETH_EUR = 8
    ETH_USD = 9
    LTC_BTC = 10
    LTC_EUR = 11
    LTC_USD = 12

    _product_mapping = {
        'BCH-USD': 1,
        'BCH-BTC': 2,
        'BCH-EUR': 3,
        'BTC-EUR': 4,
        'BTC-GBP': 5,
        'BTC-USD': 6,
        'ETH-BTC': 7,
        'ETH-EUR': 8,
        'ETH-USD': 9,
        'LTC-BTC': 10,
        'LTC-EUR': 11,
        'LTC-USD': 12
    }

    _product_integer_to_info = {
        1: 'BCH-USD',
        2: 'BCH-BTC',
        3: 'BCH-EUR',
        4: 'BTC-EUR',
        5: 'BTC-GBP',
        6: 'BTC-USD',
        7: 'ETH-BTC',
        8: 'ETH-EUR',
        9: 'ETH-USD',
        10: 'LTC-BTC',
        11: 'LTC-EUR',
        12: 'LTC-USD'
    }

    def lookUpInteger(self, gdaxproducts_str):
        return self._product_mapping[gdaxproducts_str]

    def lookUpString(self, gdaxproducts_int):
        return self._product_integer_to_info[gdaxproducts_int]
