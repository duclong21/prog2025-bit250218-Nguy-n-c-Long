# Bài 7

nhap = input("Nhập các số (cách nhau dấu cách): ")
chuoi = nhap.split()
danh_sach = [int(x) for x in chuoi]

tim = int(input("Nhập số cần tìm: "))

tim_thay = False
for i in range(len(danh_sach)):
    if danh_sach[i] == tim:
        print("Tìm thấy số", tim, "ở vị trí", i)
        tim_thay = True
        break

if tim_thay == False:
    print("Không tìm thấy số", tim)