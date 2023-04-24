def hanoi(n, cotdau, cotgiua, cotdich):
    if n == 1:
        print("Dia 1 tu", cotdau, "sang", cotdich)
        return
    hanoi(n - 1, cotdau, cotdich, cotgiua)
    print("Dia", n, "tu", cotdau, "sang", cotdich)
    hanoi(n - 1, cotgiua, cotdau, cotdich)


def main():
    n = abs(int(input("Nhap so dia n: ")))
    hanoi(n, "A", "B", "C")
    print("So buoc:", 2**n - 1)


if __name__ == "__main__":
    main()