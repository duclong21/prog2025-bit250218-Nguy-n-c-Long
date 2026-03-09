#bài 1
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

print("Ba hệ số vừa nhập là:")
print("a =", a)
print("b =", b)
print("c =", c)

max_num = max(a, b, c)
min_num = min(a, b, c)

print("Số lớn nhất là:", max_num)
print("Số nhỏ nhất là:", min_num)
import math

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("Phương trình có 2 nghiệm:")
    print("x1 =", x1)
    print("x2 =", x2)

elif delta == 0:
    x = -b / (2*a)
    print("Phương trình có nghiệm kép:")
    print("x =", x)

else:
    print("Phương trình vô nghiệm")