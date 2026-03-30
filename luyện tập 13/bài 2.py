chuoi = input("Nhập một chuỗi: ")

do_dai = len(chuoi)
so_ky_tu_a = chuoi.lower().count('a')

print(f"Chiều dài chuỗi: {do_dai}")
print(f"Số ký tự 'a' (không phân biệt hoa thường): {so_ky_tu_a}")