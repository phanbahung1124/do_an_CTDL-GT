def partition(array, low, high, ascending):
    # Có một số cách để chọn một phần tử chốt
    # Ở đây ta sẽ chỉ chọn phần tử nằm tận cùng bên phải
    pivot = array[high]

    # Trỏ vào phần tử lớn hơn
    i = low - 1

    # Duyệt từng phần tử trong list
    # Với mỗi phần tử so sánh nó với phần tử chốt
    for j in range(low, high):
        if ascending:
            if array[j] <= pivot:
                # Nếu tìm thấy phần tử nhỏ hơn phần tử chốt
                # Xáo nó với phần tử lớn hơn trỏ bởi i
                i = i + 1

                # Xáo phần tử i với phần tử j
                (array[i], array[j]) = (array[j], array[i])
                print(array)
        else:
            if array[j] >= pivot:
                # Nếu tìm thấy phần tử lớn hơn phần tử chốt
                # Xáo nó với phần tử lớn hơn trỏ bởi i
                i = i + 1

                # Xáo phần tử i với phần tử j
                (array[i], array[j]) = (array[j], array[i])
                print(array)

    # Xáo phần tử chốt với phần tử lớn hơn trỏ bởi i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    print(array)

    # Trả về vị trí tách đôi mảng
    return i + 1


# Hàm quicksort
def quick_sort(array, low, high, ascending):
    # Kiểm tra nếu mảng có ít nhất 2 phần tử
    if low < high:
        # Tìm vị trí phần tử chốt sau khi di chuyển
        # để thực hiện quick sort vào 2 mảng con
        pi = partition(array, low, high, ascending)

        # quick sort mảng bên trái
        quick_sort(array, low, pi - 1, ascending)

        # quick sort mảng bên phải
        quick_sort(array, pi + 1, high, ascending)


if __name__ == "__main__":
    n = abs(int(input("Nhap so phan tu n: ")))
    arr = []
    for i in range(n):
        x = int(input("Nhap phan tu thu " + str(i + 1) + ": "))
        arr.append(x)
    is_asc = input("Sap xep theo thu tu tang dan? (True/False): ")
    if is_asc == "True":
        quick_sort(arr, 0, n - 1, True)
    elif is_asc == "False":
        quick_sort(arr, 0, n - 1, False)