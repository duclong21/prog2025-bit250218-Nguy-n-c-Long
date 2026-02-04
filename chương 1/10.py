def tinh_tong(n):
    if n == 1:
        return 1
    return n + tinh_tong(n - 1)

n = int(input("Nhập n: "))
print("Tổng từ 1 đến n là:", tinh_tong(n))