# Refer to https://docs.gdax.com/?python#signing-a-message
# Create custom authentication for Exchange, re-written to enhance it
import time, hashlib, hmac, base64, requests
from requests.auth import AuthBase

class GdaxExAuth(AuthBase):
    def __init__(self, api_key, secret_key, passphrase):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase

    def __call__(self, request):
        timestamp = str(time.time())
        message = timestamp + request.method + request.path_url + (request.body or '')
        hmac_key = base64.b64decode(self.secret_key)
        signature = hmac.new(hmac_key, message.encode('ascii'), hashlib.sha256)
        signature_b64 = base64.b64encode(signature.digest())

        request.headers.update({
          'CB-ACCESS-SIGN': signature_b64,
          'CB-ACCESS-TIMESTAMP': timestamp,
          'CB-ACCESS-KEY': self.api_key,
          'CB-ACCESS-PASSPHRASE': self.passphrase,
          'Content-Type': 'application/json'
        })
        return request
