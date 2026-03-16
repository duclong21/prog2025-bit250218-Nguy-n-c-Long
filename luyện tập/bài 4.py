# Bài 4:
text = input("Nhập chuỗi bất kỳ: ")

upper = 0
lower = 0
digit = 0
special = 0
space = 0
vowel = 0
consonant = 0

vowels = "aeiouAEIOU"

for char in text:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char.isdigit():
        digit += 1
    elif char.isspace():
        space += 1
    else:
        special += 1

    if char.isalpha():
        if char in vowels:
            vowel += 1
        else:
            consonant += 1

print(f"Chữ cái in hoa     : {upper}")
print(f"Chữ cái in thường   : {lower}")
print(f"Chữ số              : {digit}")
print(f"Ký tự đặc biệt      : {special}")
print(f"Khoảng trắng        : {space}")
print(f"Nguyên âm           : {vowel}")
print(f"Phụ âm              : {consonant}")