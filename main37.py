class AttributePrinterMixin:
    def print_attributes(self):
        attributes = vars(self)
        class_name = type(self).__name__
        attributes_str = ""
        for key, value in attributes.items():
            if key.startswith('_'):
                key = key.split('_')[-1]
            attributes_str += f"\t{key}: {value}\n"
        print(f"{class_name}: {{\n{attributes_str}}}")


class Order(AttributePrinterMixin):
    def __init__(self, order_id, article, price):
        self.order_id = order_id
        self.article = article
        self.__price = price
        self._client = "Hillel"

class InnerOrder(Order):
    def __init__(self, order_id, article, price, netto_price):
        super().__init__(order_id, article, price)
        self.netto_price = netto_price


order = Order(1, 'HUT1GT', 3000)
innerorder = InnerOrder(1, 'HUT1GT', 3000, 2000)

order.print_attributes()
innerorder.print_attributes()
