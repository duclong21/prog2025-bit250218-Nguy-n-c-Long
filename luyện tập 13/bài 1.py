
import math

so = float(input("Nhập một số: "))

if so < 0:
    print("Lỗi: Không thể tính căn bậc hai của số âm!")
else:
    can_bac_hai = math.sqrt(so)
    print(f"Căn bậc hai của {so} là: {can_bac_hai:.4f}")
