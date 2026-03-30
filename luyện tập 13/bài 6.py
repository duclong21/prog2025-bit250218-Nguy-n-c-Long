def sap_xep(danh_sach):
    n = len(danh_sach)
    for i in range(n):
        for j in range(0, n - i - 1):
            if danh_sach[j] > danh_sach[j + 1]:
                danh_sach[j], danh_sach[j + 1] = danh_sach[j + 1], danh_sach[j]
    return danh_sach

try:
    day_so = list(map(int, input("Nhập dãy số cách nhau bởi dấu cách: ").split()))
    print("Dãy số ban đầu:", day_so)

    ket_qua = sap_xep(day_so[:])
    print("Dãy số sau khi sắp xếp tăng dần:", ket_qua)
except ValueError:
    print("Lỗi: Vui lòng chỉ nhập các số nguyên cách nhau bởi dấu cách!")