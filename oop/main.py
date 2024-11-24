# class Item:
#     def calculate_total_price(self, x, y):
#         return x * y


# item1 = Item()
# item1.price = 100
# item1.quantity = 5
# print(item1.calculate_total_price(item1.price, item1.quantity))

class Item:
    def __init__(self, price: int, quantity: int) -> int:
        assert price >= 0, f"Price {price} should positive number"
        assert quantity >= 0
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item(100, 5)
print(item1.calculate_total_price())
