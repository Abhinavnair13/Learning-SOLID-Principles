from abc import ABC, abstractmethod



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
  @abstractmethod
  def pay(self, order:Order, paymentType : str, code,status: str):
    ...

class Paypal(Payment):
  def pay(self, order:Order, paymentType : str, code,status: str):
    print("Paying with Paypal")
    print(f"Order: {order.items}")
    print(f"Total: {order.get_total()}")
    print(f"Payment Type: {True}")
    print(f"Code: {code}")
    print(f"Status: {status}")
order = Order()
order.add_item(item = 'iPhone',quantity = 1,price = 1000)
paypal = Paypal()
paypal.pay(order = order,paymentType ='card',code = '1234',status = 'paid')
print(order.status)

    