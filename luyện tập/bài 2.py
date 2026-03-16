# Bài 2
number = input("Nhập một số: ").strip()

if not number.isdigit():
    print("phải nhập số nguyên dương!")
else:
    total = 0
    for char in number:
        total += int(char)
    print(f"Tổng các chữ số: {total}")