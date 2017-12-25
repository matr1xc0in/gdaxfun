class GdaxProducts:
    BCH_USD = 1
    BTC_EUR = 2
    BTC_GBP = 3
    BTC_USD = 4
    ETH_BTC = 5
    ETH_EUR = 6
    ETH_USD = 7
    LTC_BTC = 8
    LTC_EUR = 9
    LTC_USD = 10

    _product_mapping = {
        'BCH-USD': 1,
        'BTC-EUR': 2,
        'BTC-GBP': 3,
        'BTC-USD': 4,
        'ETH-BTC': 5,
        'ETH-EUR': 6,
        'ETH-USD': 7,
        'LTC-BTC': 8,
        'LTC-EUR': 9,
        'LTC-USD': 10
    }

    _product_integer_to_info = {
        1: 'BCH-USD',
        2: 'BTC-EUR',
        3: 'BTC-GBP',
        4: 'BTC-USD',
        5: 'ETH-BTC',
        6: 'ETH-EUR',
        7: 'ETH-USD',
        8: 'LTC-BTC',
        9: 'LTC-EUR',
        10: 'LTC-USD'
    }

    def lookUpInteger(self, gdaxproducts_str):
        return self._product_mapping[gdaxproducts_str]

    def lookUpString(self, gdaxproducts_int):
        return self._product_integer_to_info[gdaxproducts_int]
