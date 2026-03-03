# Bài 11

nhap = input("Nhập các số (cách nhau dấu cách): ")
chuoi = nhap.split()
danh_sach = [int(x) for x in chuoi]

lon_nhat = danh_sach[0]
nho_nhat = danh_sach[0]

for so in danh_sach:
    if so > lon_nhat:
        lon_nhat = so
    if so < nho_nhat:
        nho_nhat = so

print("Số lớn nhất:", lon_nhat)
print("Số nhỏ nhất:", nho_nhat)