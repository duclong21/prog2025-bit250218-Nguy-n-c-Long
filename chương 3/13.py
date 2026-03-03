# Bài 13

chuoi = input("Nhập chuỗi: ")

dao_nguoc = ""
for ky_tu in chuoi:
    dao_nguoc = ky_tu + dao_nguoc

if chuoi == dao_nguoc:
    print("Đây là chuỗi đối xứng (Palindrome)")
else:
    print("Không phải chuỗi đối xứng")