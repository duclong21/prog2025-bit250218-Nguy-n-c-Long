class Product:
    def __init__(self, price=0):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, gia):
        if gia > 0:
            self._price = gia
        else:
            raise ValueError("Giá sản phẩm phải lớn hơn 0!")

    def __str__(self):
        return f"Product - Giá: {self._price:,} VND"

try:
    sp1 = Product(150000)
    print(sp1)

    sp2 = Product(-5000)
except ValueError as e:
    print("Lỗi:", e)