# Bài 1
weight = float(input("Nhập cân nặng (kg): "))
height = float(input("Nhập chiều cao (m): "))

if height <= 0:
    print("Chiều cao không hợp lệ!")
else:
    bmi = weight / (height * height)
    print(f"BMI của bạn là: {bmi:.2f}")