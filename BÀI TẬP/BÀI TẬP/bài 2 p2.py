ds = []

for i in range(5):
    ten = input(f"Nhập tên người thứ {i+1}: ")
    ds.append(ten)

print("Danh sách ban đầu:", ds)

del ds[1]

print("Danh sách sau khi xóa:", ds)