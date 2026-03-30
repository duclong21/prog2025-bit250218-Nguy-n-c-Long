def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giai_thua(n - 1)


# Chương trình chính
try:
    so = int(input("Nhập số nguyên không âm để tính giai thừa: "))
    if so < 0:
        print("Lỗi: Giai thừa chỉ định nghĩa cho số không âm!")
    else:
        ket_qua = giai_thua(so)
        print(f"{so}! = {ket_qua}")
except ValueError:
    print("Lỗi: Vui lòng nhập số nguyên!")