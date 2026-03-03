# Bài 8

nhap = input("Nhập các số (cách nhau dấu cách): ")
chuoi = nhap.split()
danh_sach = [float(x) for x in chuoi]

tim_thay = False
for so in danh_sach:
    if so > 10:
        print("Số đầu tiên lớn hơn 10 là:", so)
        tim_thay = True
        break

if tim_thay == False:
    print("Không có số nào lớn hơn 10")