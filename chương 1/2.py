n = int(input("Nhập một số dương bất kì : "))
if n < 2:
    print("đây không phải số nguyên tố")
else:
    la_so_nguyen_to = True
    for i in range(2, n):
        if n % i == 0:
            la_so_nguyen_to = False
            break
    if la_so_nguyen_to:
        print("Là số nguyên tố")
    else:
        print("đây ko phải số nguyên tố")
