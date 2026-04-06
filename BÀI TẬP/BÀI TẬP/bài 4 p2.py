class Book:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    # getter
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    # setter
    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price

book = Book("Book A", 50000)

print("Giá của sách:", book.get_price())