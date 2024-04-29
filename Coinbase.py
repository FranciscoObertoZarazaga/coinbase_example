import cbpro

PASS_PHRASE = ''
SECRET_KEY = ''
PUBLIC_KEY = ''


class CoinBase:

    def __init__(self):
        self.client = cbpro.AuthenticatedClient(PUBLIC_KEY, SECRET_KEY, PASS_PHRASE)

    def get_price(self, symbol):
        order_book = self.client.get_product_order_book(symbol, level=1)
        # return buyPrice, sellPrice
        return order_book['bids'][0][0], order_book['asks'][0][0]
