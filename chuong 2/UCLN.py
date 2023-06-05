def gcd_euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def main():
    a = abs(int(input('nhap vao so nguyen a: ')))
    b = abs(int(input('nhap vao so nguyen b: ')))
    gcd = gcd_euclid(a, b)
    print("Uoc chung lon nhat cua", a, "va", b, "la", gcd)
if __name__ =="__main__":
    main()
