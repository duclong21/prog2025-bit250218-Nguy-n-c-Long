# Bài 4
class Hoa:
    def __init__(self, ten, mau):
        self.ten = ten
        self.mau = mau

    def in_thong_tin(self):
        print("Tên hoa:", self.ten)
        print("Màu sắc:", self.mau)

hoa1 = Hoa("tulip", "hồng")
hoa1.in_thong_tin()

print("---")

hoa2 = Hoa("vanila", "Vàng")
hoa2.in_thong_tin()