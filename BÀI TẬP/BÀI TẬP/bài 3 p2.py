
n = int(input("Nhập số phần tử: "))
arr = []

for i in range(n):
    x = int(input(f"Nhập phần tử {i+1}: "))
    arr.append(x)

so_le = []
for x in arr:
    if x % 2 != 0:
        so_le.append(x)

print("Các số lẻ:", so_le, "- Số lượng:", len(so_le))

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

so_nt = []
for x in arr:
    if la_so_nguyen_to(x):
        so_nt.append(x)

print("Các số nguyên tố:", so_nt)