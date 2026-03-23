import csv

nhan_vien = []
n = int(input("Nhập số nhân viên: "))
for i in range(n):
    ten = input(f"Tên NV {i+1}: ").strip()
    tuoi = input(f"Tuổi: ").strip()
    id_nv = input(f"ID: ").strip()
    nhan_vien.append({"ten": ten, "tuoi": tuoi, "id": id_nv})

with open("nhanvien.txt", "w", encoding="utf-8") as f:
    for nv in nhan_vien:
        f.write(f"{nv['ten']},{nv['tuoi']},{nv['id']}\n")

with open("nhanvien.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["ten", "tuoi", "id"])
    writer.writeheader()
    writer.writerows(nhan_vien)

print("Đã lưu vào nhanvien.txt và nhanvien.csv")
print("Bạn có thể mở 2 file trên để kiểm tra nội dung.")