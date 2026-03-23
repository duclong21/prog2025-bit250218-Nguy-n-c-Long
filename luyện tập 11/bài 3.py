
danh_sach = []
n = int(input("Bạn muốn nhập bao nhiêu số? "))
for i in range(n):
    x = int(input(f"Số thứ {i+1}: "))
    danh_sach.append(x)

so_chan = [x for x in danh_sach if x % 2 == 0]
tong_chan = sum(so_chan)

print("Các số chẵn là :", so_chan)
print("Tổng các số chẵn là"
      " :", tong_chan)