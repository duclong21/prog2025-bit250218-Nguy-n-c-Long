chuoi = input("Nhập chuỗi: ")
ky_tu = input("Nhập ký tự cần đếm: ")
dem = 0
for c in chuoi:
    if c == ky_tu:
        dem += 1
print("Số lần xuất hiện:", dem)