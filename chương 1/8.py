n = int(input("Nhập một số dương: "))
dao_nguoc = 0
while n > 0:
    chu_so_cuoi = n % 10
    dao_nguoc = dao_nguoc * 10 + chu_so_cuoi
    n = n // 10
print("Số đảo ngược của số cần tìm là :", dao_nguoc)