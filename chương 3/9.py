# Bài 9

nhap = input("Nhập các số (cách nhau dấu cách): ")
chuoi = nhap.split()
danh_sach = [int(x) for x in chuoi]

print("Các số lẻ:")
for so in danh_sach:
    if so % 2 != 0:
        print(so)