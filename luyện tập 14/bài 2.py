n = int(input("Nhập n: "))

#hinh 1
print("\nHình 1:")
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

# hình 2
print("\nHình 2:")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# hình 3
print("\nHình 3:")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# hình 4
print("\nHình 4:")
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()

# hình 5
print("\nHình 5:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# hình 6
print("\nHình 6:")
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        if k == 1 or k == i or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# hình 7
print("\nHình 7:")
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == n or j == n - i + 1 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# hình 8
print("\nHình 8:")
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()

# hình 9
print("\nHình 9:")
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# hình 10
print("\nHình 10:")
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1 or i == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()