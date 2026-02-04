#bài 1
n = int(input("Nhập một số ngẫu nhiên từ 1 đến 9: "))
for i in range(1, 10):
    print(f"{n} x {i} = {n * i}")
#bài2
n = int(input("Nhập một số dương bất kì : "))
if n < 2:
    print("đây không phải số nguyên tố")
else:
    la_so_nguyen_to = True
    for i in range(2, n):
        if n % i == 0:
            la_so_nguyen_to = False
            break
    if la_so_nguyen_to:
        print("Là số nguyên tố")
    else:
        print("đây ko phải số nguyên tố")
#bài3
    n = int(input("Nhập số n: "))
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
#bài4
n = int(input("Nhập một số bất kì : "))
tong = 0
while n > 0:
    tong += n % 10  # Lấy chữ số cuối
    n = n // 10     # Bỏ chữ số cuối
print("Tổng các chữ số là:", tong)
#bài5
chuoi = input("Nhập chuỗi: ")
ky_tu = input("Nhập ký tự cần đếm: ")
dem = 0
for c in chuoi:
    if c == ky_tu:
        dem += 1
print("Số lần xuất hiện:", dem)
#bài6
def tinh_giai_thua(n):
    if n == 0 or n == 1:
        return 1
    return n * tinh_giai_thua(n - 1)

n = int(input("Nhập n: "))
print("Giai thừa là:", tinh_giai_thua(n))
#bài7
a = int(input("Nhập số thứ nhất cần tìm : "))
b = int(input("Nhập số thứ hai cần tìm : "))
while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a
print("ước chung lớn nhất là:", a)
#bài8
n = int(input("Nhập một số dương: "))
dao_nguoc = 0
while n > 0:
    chu_so_cuoi = n % 10
    dao_nguoc = dao_nguoc * 10 + chu_so_cuoi
    n = n // 10
print("Số đảo ngược của số cần tìm là :", dao_nguoc)
#bài9
n = int(input("Nhập số nguyên dương 5 chữ số: "))
max_chu_so = 0

while n > 0:
    chu_so = n % 10
    if chu_so > max_chu_so:
        max_chu_so = chu_so
    n = n // 10 #

print("Chữ số cần tìm lớn nhất là:", max_chu_so)
#bài10
def tinh_tong(n):
    if n == 1:
        return 1
    return n + tinh_tong(n - 1)

n = int(input("Nhập n: "))
print("Tổng từ 1 đến n là:", tinh_tong(n))
#bài11
diem = float(input("Nhập điểm trung bình: "))

if diem >= 8:
    print("Xếp loại: Giỏi")
elif diem >= 6.5:
    print("Xếp loại: Khá")
elif diem >= 5.0:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")
#bài12
n = int(input("Nhập n: "))
tong_le = 0

for i in range(1, n + 1):
    if i % 2 != 0: # Kiểm tra nếu là số lẻ
        tong_le = tong_le + i

print("Tổng các số lẻ là:", tong_le)
#bài13
mat_khau_dung = "em yêu đại học cmc "
nhap = ""

while nhap != mat_khau_dung:
    nhap = input("Nhập mật khẩu: ")
    if nhap == mat_khau_dung:
        print("Đăng nhập thành công!")
    else:
        print("Sai mật khẩu, vui lòng nhập lại.")
#bài14
n = int(input("Nhập số n: "))

if n < 2:
    print(n, "không phải là số nguyên tố")
else:
    dem = 0
    for i in range(1, n + 1):
        if n % i == 0:
            dem = dem + 1

    if dem == 2:
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")
#bài15
n = int(input("Nhập một số nguyên dương: "))
tong = 0

while n > 0:
    chu_so = n % 10
    tong = tong + chu_so
    n = n // 10

print("Tổng các chữ số là:", tong)