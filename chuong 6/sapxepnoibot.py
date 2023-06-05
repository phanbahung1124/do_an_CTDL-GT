def bubble_sort(array, ascending):
    for i in range(len(array) - 1):  # Thu hẹp dần phạm vi duyệt khi ta đẩy được số lớn nhất/nhỏ nhất về bên phải cùng
        for j in range(0, len(array) - i - 1):  # Duyệt từng phần tử trong phạm vi duyệt từ trái -> phải
            if ascending is True:  # Sắp xếp tăng dần
                if array[j] > array[j + 1]:  # Nếu phần tử trước lớn hơn phần tử sau
                    array[j], array[j + 1] = array[j + 1], array[j]  # Hoán đổi
                    print("(Đổi chỗ:", array[j+1], str(array[j]) + ")", end = " ")
            else:  # Tương tự ngược lại
                if array[j] < array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    print("(Đổi chỗ:", array[j+1], str(array[j]) + ")", end=" ")
            print(array)  # In bước


if __name__ == "__main__":
    n = abs(int(input("Nhap so phan tu n: ")))
    arr = []
    for i in range(n):
        x = int(input("Nhap phan tu thu " + str(i + 1) + ": "))
        arr.append(x)
    is_asc = input("Sap xep theo thu tu tang dan? (True/False): ")
    if is_asc == "True":
        bubble_sort(arr, True)
    elif is_asc == "False":
        bubble_sort(arr, False)