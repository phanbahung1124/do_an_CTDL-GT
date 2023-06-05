def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Nhap so nguyen duong n: "))
print("Giai thua cua", n, "la", factorial(n))
