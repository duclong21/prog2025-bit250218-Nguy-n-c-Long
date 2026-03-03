# Bài 10

nhap = input("Nhập các số (cách nhau dấu cách): ")
chuoi = nhap.split()
danh_sach = [int(x) for x in chuoi]

tong_chan = 0
print("Các số chẵn:")
for so in danh_sach:
    if so % 2 == 0:
        print(so)
        tong_chan = tong_chan + so

print("Tổng các số chẵn:", tong_chan)