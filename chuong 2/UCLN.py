def UCLN(a, b):
    if b == 0:
        return a
    else:
        if b > a:
            b, a = a, b
        return UCLN(b, a % b)

def main():
    a = abs(int(input("Nhap so a: ")))
    b = abs(int(input("Nhap so b: ")))
    kq = UCLN(a, b)
    print("UCLN cua 2 so la:", kq)


if __name__ == "__main__":
    main()