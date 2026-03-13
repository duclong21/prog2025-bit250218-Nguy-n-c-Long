# Bài 2
def tinh_diem_trung_binh():
    diem_sinh_vien = {}

    n = int(input("Nhập số lượng sinh viên: "))

    for i in range(n):
        ten = input("Nhập tên sinh viên thứ " + str(i + 1) + ": ")
        diem = float(input("Nhập điểm của " + ten + ": "))
        diem_sinh_vien[ten] = diem

    tong_diem = 0
    for diem in diem_sinh_vien.values():
        tong_diem = tong_diem + diem

    trung_binh = tong_diem / n

    print("Điểm trung bình của cả lớp =", trung_binh)
    print("Danh sách điểm:", diem_sinh_vien)
tinh_diem_trung_binh()