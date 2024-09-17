class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name

    def orders(self):
        from order import Order  # Move import here to avoid circular import
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        if self.num_orders() == 0:
            return 0
        prices = sum(order.price for order in self.orders())
        return prices / self.num_orders()
