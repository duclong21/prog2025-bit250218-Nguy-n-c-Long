du_lieu = {"long": 10, "thảo linh": 9, "lượng": 36, "trúc": 8}

key = input("Nhập key cần kiểm tra: ").strip()

if key in du_lieu:
    print(f"Tìm thấy! {key}: {du_lieu[key]}")
else:
    print("Không tìm thấy key này.")