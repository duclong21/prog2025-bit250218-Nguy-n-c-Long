n = int(input("Nhập n: "))
tong_le = 0

for i in range(1, n + 1):
    if i % 2 != 0: # Kiểm tra nếu là số lẻ
        tong_le = tong_le + i

print("Tổng các số lẻ là:", tong_le)