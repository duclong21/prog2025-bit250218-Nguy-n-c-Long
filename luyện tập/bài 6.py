# Bài 6:
class Product:
    def __init__(self, price=0.0):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Giá phải lớn hơn 0!")
        self._price = value

    def __str__(self):
        return f"Product(price={self.price:.2f} VND)"



p = Product(250000)
print(p)


p.price = 299000
print(p)