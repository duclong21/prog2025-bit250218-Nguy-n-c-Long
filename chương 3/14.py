# Bài 14

def count_vowels(s):
    s = s.lower()
    dem = 0
    nguyen_am = "aeiou"
    for ky_tu in s:
        if ky_tu in nguyen_am:
            dem = dem + 1
    return dem

chuoi = input("Nhập chuỗi: ")
print("Số nguyên âm:", count_vowels(chuoi))