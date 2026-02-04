n = int(input("Nhập số nguyên dương 5 chữ số: "))
max_chu_so = 0

while n > 0:
    chu_so = n % 10
    if chu_so > max_chu_so:
        max_chu_so = chu_so
    n = n // 10 #

print("Chữ số cần tìm lớn nhất là:", max_chu_so)