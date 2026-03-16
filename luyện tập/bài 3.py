# Bài 3
full_name = input("Nhập họ và tên: ").strip()

words = full_name.split()
normalized = " ".join(word.capitalize() for word in words)

print("Tên chuẩn hóa:", normalized)