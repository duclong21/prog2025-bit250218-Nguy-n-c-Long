def tinh_giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * tinh_giai_thua(n - 1)

n = int(input("Nhập n: "))
print("Giai thừa là:", tinh_giai_thua(n))