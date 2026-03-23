def nhap_ma_tran(ten):
    print(f"\nNhập ma trận {ten}:")
    n = int(input("Số hàng/cột (ma trận vuông): "))
    ma_tran = []
    for i in range(n):
        while True:
            hang = input(f"Hàng {i + 1} (cách nhau dấu cách): ").strip()
            if not hang:
                print("Không được để trống! Nhập lại.")
                continue
            try:
                gia_tri = list(map(int, hang.split()))
                if len(gia_tri) != n:
                    print(f"Phải nhập đúng {n} số!")
                    continue
                ma_tran.append(gia_tri)
                break
            except:
                print("Vui lòng chỉ nhập số nguyên!")
    return ma_tran


A = nhap_ma_tran("A")
B = nhap_ma_tran("B")

if len(A) != len(B) or len(A[0]) != len(B[0]):
    print("Hai ma trận không cùng kích thước!")
else:
    n = len(A)
    C = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]

    print("\nMa trận A:")
    for hang in A:
        print(hang)
    print("\nMa trận B:")
    for hang in B:
        print(hang)
    print("\nMa trận C = A + B:")
    for hang in C:
        print(hang)