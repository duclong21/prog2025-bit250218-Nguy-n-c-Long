# Bài 3
def kiem_tra_key():
    sinh_vien = {
        "long": 8.5,
        "linh": 7.0,
        "trúc": 9.2,
        "lượng": 6.8
    }

    ten_can_kiem_tra = input("Nhập tên sinh viên cần kiểm tra: ")

    if ten_can_kiem_tra in sinh_vien:
        print(ten_can_kiem_tra, "có trong danh sách")
        print("Điểm của", ten_can_kiem_tra, "là", sinh_vien[ten_can_kiem_tra])
    else:
        print(ten_can_kiem_tra, "không có trong danh sách")
kiem_tra_key()