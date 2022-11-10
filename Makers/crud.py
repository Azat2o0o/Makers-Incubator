discont = 10
class Products:
    def __init__(self):
        self.orders = []
        self.products = Product()
        self.product.post(title= 'Iphone 5s', descriptions='The best phone in world', qty=5, price=25000)
        self.product.post(title= 'Nokia 2700', descriptions='The best phone', qty=3, price= 12000)

    def create_order(self, objects):
        ls = []
        for item in objects:
            for product in self.product.objects:
                if item['id'] == product['id']:
                    self.subract_qty(item, product)
                    ls.append(product)
        self.orders.append(ls)
        money = self.total_count(ls)
        return {'order': ls, 'total sum': money}

    def total_count(self, objects):
        total_count = 0
        for product in objects:
            price = product['price']
            total_count += self.make_discount(price, self.discount)
        return total_count

    def subract_qty(self, item, product):
        result = product['qty'] - item['qty']
        if result < 0:
            raise Exception('Too many qty of product!')
        product['qty'] = result

    def make_discount(self, price, percent):
        return price - (price / 100 * percent)
    
phone = Odrder()
print('Before: ', orders.product.objects())
Products = [{'id': 1, 'qty': 3}, {'id': 2, 'qty': 2}]
print(orders.create_order(products))
print('After: ', orders.product.objects)