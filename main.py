from Coinbase import CoinBase

cb = CoinBase()
price = cb.get_price('BTC-USD')
print(price)
