class Order:
  def __init__(self,items = [],quantity = [],prices =[],status = "open") -> None:
    self.items = items
    self.quantity = quantity
    self.prices = prices
    self.status = status
  def add_item(self,item,quantity,price):
    self.items.append(item)
    self.quantity.append(quantity)
    self.prices.append(price)
  def get_total(self):
    sum = 0
    for price in self.prices:
      sum +=price
    return sum
class Payment:
  def pay(self, order:Order, paymentType : str, code):
    order.status = 'paid'
    print(f'Payment method: {paymentType}  code : {code}')
    print(f'Order total: {order.get_total()}')
order = Order()
order.add_item(item = 'iPhone',quantity = 1,price = 1000)
pay = Payment()
pay.pay(order = order,paymentType = 'card',code = '1234')
print(order.status)
    