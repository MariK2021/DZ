class Client:
    def __init__(self, name):
        self.name = name
        self._list_of_orders = []

    def make_order(self, order):
        self._list_of_orders.append(order)

    def __str__(self):
        return f"Your items are: {self._list_of_orders}"
