danh_sach_nguoi = {}

n = int(input("Nhập số người: "))
for _ in range(n):
    ten = input("Tên: ").strip()
    tuoi = int(input("Tuổi: "))
    danh_sach_nguoi[ten] = tuoi

if danh_sach_nguoi:
    tuoi_tb = sum(danh_sach_nguoi.values()) / len(danh_sach_nguoi)
    print(f"Tuổi trung bình: {tuoi_tb:.1f}")
else:
    print("Không có ai.")

items = list(danh_sach_nguoi.items())

for i in range(len(items)):
    max_idx = i
    for j in range(i+1, len(items)):
        if items[j][1] > items[max_idx][1]:
            max_idx = j
    items[i], items[max_idx] = items[max_idx], items[i]

print("\nDanh sách sau khi sắp xếp tuổi giảm dần:")
for ten, tuoi in items:
    print(f"{ten}: {tuoi} tuổi")