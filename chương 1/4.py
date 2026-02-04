n = int(input("Nhập một số bất kì : "))
tong = 0
while n > 0:
    tong += n % 10  # Lấy chữ số cuối
    n = n // 10     # Bỏ chữ số cuối
print("Tổng các chữ số là:", tong)