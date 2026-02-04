n = int(input("Nhập một số nguyên dương: "))
tong = 0

while n > 0:
    chu_so = n % 10
    tong = tong + chu_so
    n = n // 10

print("Tổng các chữ số là:", tong)