# Bài 6

nhap = input("Nhập các số nguyên (cách nhau dấu cách): ")
chuoi = nhap.split()
so = []
for x in chuoi:
    so.append(int(x))

print("Trước:", so)

dem_hoan_doi = 0
n = len(so)

for i in range(n-1):
    for j in range(n-1-i):
        if so[j] > so[j+1]:

            tam = so[j]
            so[j] = so[j+1]
            so[j+1] = tam
            dem_hoan_doi = dem_hoan_doi + 1

print("Sau khi sắp xếp:", so)
print("Số lần hoán đổi:", dem_hoan_doi)