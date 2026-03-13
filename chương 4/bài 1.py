# Bài 1
def xu_ly_tuple_so_nguyen(day_so):

    tong = 0
    gia_tri_lon_nhat = day_so[0]
    gia_tri_nho_nhat = day_so[0]

    for so in day_so:
        tong = tong + so

        if so > gia_tri_lon_nhat:
            gia_tri_lon_nhat = so

        if so < gia_tri_nho_nhat:
            gia_tri_nho_nhat = so

    print("Tổng =", tong)
    print("Giá trị lớn nhất =", gia_tri_lon_nhat)
    print("Giá trị nhỏ nhất =", gia_tri_nho_nhat)

    return tong, gia_tri_lon_nhat, gia_tri_nho_nhat

numbers = (56, 162, -83, 28, 0, 195, 87)
xu_ly_tuple_so_nguyen(numbers)