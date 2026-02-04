a = int(input("Nhập số thứ nhất cần tìm : "))
b = int(input("Nhập số thứ hai cần tìm : "))
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print("ước chung lớn nhất là:", a)