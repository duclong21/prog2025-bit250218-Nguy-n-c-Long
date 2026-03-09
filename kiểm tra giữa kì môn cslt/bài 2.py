for i in range(111, 16, -2):
    print(i)
for n in range(17, 112):
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n)