danh_sach = []
while True:
    print("\n1. Thêm phần tử")
    print("2. Đếm số lần xuất hiện của k")
    print("3. Tính tổng số nguyên tố")
    print("4. Sắp xếp danh sách")
    print("5. Xóa danh sách")
    print("0. Thoát")

    chon = input("Chọn chức năng: ")

    if chon == '1':
        x = int(input("Nhập số: "))
        danh_sach.append(x)
        print("Danh sách hiện tại:", danh_sach)

    elif chon == '2':
        if not danh_sach:
            print("Danh sách rỗng!")
            continue
        k = int(input("Nhập giá trị k: "))
        dem = danh_sach.count(k)
        print(f"Số {k} xuất hiện {dem} lần")

    elif chon == '3':
        def la_nguyen_to(n):
            if n < 2: return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0: return False
            return True


        tong_nt = sum(x for x in danh_sach if la_nguyen_to(x))
        print("Tổng các số nguyên tố:", tong_nt)

    elif chon == '4':
        danh_sach.sort()
        print("Danh sách sau khi sắp xếp:", danh_sach)

    elif chon == '5':
        danh_sach.clear()
        print("Đã xóa danh sách!")

    elif chon == '0':
        break