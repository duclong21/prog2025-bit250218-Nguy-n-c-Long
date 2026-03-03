# Bài 12

print("Nhập ma trận A (mỗi dòng cách nhau dấu cách):")
A = []
for i in range(2):   # ví dụ 2x3
    hang = [int(x) for x in input().split()]
    A.append(hang)

print("Nhập ma trận B:")
B = []
for i in range(2):
    hang = [int(x) for x in input().split()]
    B.append(hang)

print("Kết quả C = A + B:")
for i in range(2):
    for j in range(3):
        tong = A[i][j] + B[i][j]
        print(tong, end=" ")
    print()