n = int(input("Nhập n: "))
#hinh 1
print("\nHình 1:")
for i in range(n):
    for j in range(n):
        print(1, end=" ")
    print()
#hinh 2
print("\nHình 2:")
for i in range(n):
    for j in range(1, n+1):
        print(j, end=" ")
    print()
#hinh 3
print("\nHình 3:")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
#hinh 4
print("\nHình 4:")
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
#hình 5
print("\nHình 5:")
for i in range(1, n+1):
    print(" "*(i-1), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()
#hình 6
print("\nHình 6:")
for i in range(n, 0, -1):
    print(" "*(n-i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()
#hình 7
print("\nHình 7:")
for i in range(1, n+1):
    print(" "*(n-i), end="")
    for j in range(1, i+1):
        print(i, end=" ")
    print()
#hinh 8
print("\nHình 8:")
for i in range(1, n+1):
    print(" "*(n-i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    for j in range(i-1, 0, -1):
        print(j, end=" ")
    print()
#hình 9
print("\nHình 9:")
for i in range(1, n+1):
    print(" "*(n-i), end="")
    for j in range(1, i+1):
        print(1, end=" ")
    print()