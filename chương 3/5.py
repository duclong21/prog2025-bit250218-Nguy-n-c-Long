# Bài 5

nhap = input("Nhập các số (cách nhau bởi dấu cách): ")
chuoi = nhap.split()
danh_sach = []
for x in chuoi:
    danh_sach.append(float(x))

print("Trước khi sắp xếp:", danh_sach)

n = len(danh_sach)
for i in range(1, n):
    key = danh_sach[i]
    j = i - 1
    while j >= 0 and danh_sach[j] < key:
        danh_sach[j + 1] = danh_sach[j]
        j = j - 1
    danh_sach[j + 1] = key

print("Sau khi sắp xếp giảm dần:", danh_sach)