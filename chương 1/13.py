mat_khau_dung = "em yêu đại học cmc "
nhap = ""

while nhap != mat_khau_dung:
    nhap = input("Nhập mật khẩu: ")
    if nhap == mat_khau_dung:
        print("Đăng nhập thành công!")
    else:
        print("Sai mật khẩu, vui lòng nhập lại.")
