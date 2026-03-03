# Bài 15

chuoi = input("Nhập chuỗi: ")

# Cách 1
print("Cách 1 (slicing):", chuoi[::-1])

# Cách 2
dao = ""
for ky_tu in chuoi:
    dao = ky_tu + dao
print("Cách 2 (vòng lặp):", dao)